//
//  ViewController.swift
//  Hours Spent
//
//  Created by Ryan Munguia on 3/16/17.
//  Copyright © 2017 Ryan Munguia. All rights reserved.
//

import UIKit
import MapKit
import CoreLocation

struct PreferencesKeys {
  static let savedItems = "savedItems"
}

class GeotificationsViewController: UIViewController, TimeSpentTableDelegate {
  
  let spots = ["Home","Dojo","Gym"]
  
  @IBOutlet weak var mapView: MKMapView!
  
  var geotifications: [Geotification] = []
  let locationManager = CLLocationManager() /// This is here in order to set up a Location Manager instance and request the appropriate permissions.
  
  override func viewDidLoad() {
    super.viewDidLoad()
    // 1
    locationManager.delegate = self
    // 2
    locationManager.requestAlwaysAuthorization() //this line in particular is for the request authorization prompt to user
    // 3
    loadAllGeotifications()
//
    
    
    //loads them into a local geotifications array. The method also loads the geotifications as annotations on the map view.
  }
  
  override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
    if segue.identifier == "addGeotification" {
      let navigationController = segue.destination as! UINavigationController
      let vc = navigationController.viewControllers.first as! AddGeotificationViewController
      vc.delegate = self
    } else if segue.identifier == "viewTimeStamp"{
      let navigationController = segue.destination as! UINavigationController
      let vc = navigationController.topViewController as! TimeSpentTable
      vc.delegate = self
      for location in geotifications{
        vc.geotifications.append(location.note)
      }
      
    }
  }
  //Core Location requires each geofence to be represented as a CLCircularRegion instance before it can be registered for monitoring
  func region(withGeotification geotification: Geotification) -> CLCircularRegion {
    // 1 - You initialize a CLCircularRegion with the location of the geofence, the radius of the geofence and an identifier that allows iOS to distinguish between the registered geofences of a given app.
    let region = CLCircularRegion(center: geotification.coordinate, radius: geotification.radius, identifier: geotification.identifier)
    // 2 - These flags specify whether geofence events will be triggered when the device enters and leaves the defined geofence, respectively.    region.notifyOnEntry = (geotification.eventType == .onEntry)
    region.notifyOnExit = !region.notifyOnEntry
    return region
  }
  
  // Is a method to start monitoring a given geotification whenever the user adds one.
  func startMonitoring(geotification: Geotification) {
    // 1 - determines if the device has the required hardware to support the monitoring of geofences.
    if !CLLocationManager.isMonitoringAvailable(for: CLCircularRegion.self) {
      showAlert(withTitle:"Error", message: "Geofencing is not supported on this device!")
      return
    }
    // 2 - Next, you check the authorization status to ensure that the app has also been granted the required permission to use Location Services. If the app isn’t authorized, it won’t receive any geofence-related notifications.
    if CLLocationManager.authorizationStatus() != .authorizedAlways {
      showAlert(withTitle:"Warning", message: "Your geotification is saved but will only be activated once you grant Geotify permission to access the device location.")
    }
    // 3
    let region = self.region(withGeotification: geotification)
    // 4
    locationManager.startMonitoring(for: region)
  }
  
  // This method simply instructs the locationManager to stop monitoring the CLCircularRegion associated with the given geotification.
  func stopMonitoring(geotification: Geotification) {
    for region in locationManager.monitoredRegions {
      guard let circularRegion = region as? CLCircularRegion, circularRegion.identifier == geotification.identifier else { continue }
      locationManager.stopMonitoring(for: circularRegion)
    }
  }
  
  // MARK: Loading and saving functions
  func loadAllGeotifications() {
    geotifications = []
    guard let savedItems = UserDefaults.standard.array(forKey: PreferencesKeys.savedItems) else { return }
    for savedItem in savedItems {
      guard let geotification = NSKeyedUnarchiver.unarchiveObject(with: savedItem as! Data) as? Geotification else { continue }
      add(geotification: geotification)
    }
  }
  
  func saveAllGeotifications() {
    var items: [Data] = []
    for geotification in geotifications {
      let item = NSKeyedArchiver.archivedData(withRootObject: geotification)
      items.append(item)
    }
    UserDefaults.standard.set(items, forKey: PreferencesKeys.savedItems)
  }
  
  // MARK: Functions that update the model/associated views with geotification changes
  func add(geotification: Geotification) {
    geotifications.append(geotification)
    mapView.addAnnotation(geotification)
    addRadiusOverlay(forGeotification: geotification)
    updateGeotificationsCount()
  }
  
  func remove(geotification: Geotification) {
    if let indexInArray = geotifications.index(of: geotification) {
      geotifications.remove(at: indexInArray)
    }
    mapView.removeAnnotation(geotification)
    removeRadiusOverlay(forGeotification: geotification)
    updateGeotificationsCount()
  }
  
  func updateGeotificationsCount() {
    title = "Geotifications (\(geotifications.count))"
    navigationItem.rightBarButtonItem?.isEnabled = (geotifications.count < 20)
    //
  }
  
  // MARK: Map overlay functions
  func addRadiusOverlay(forGeotification geotification: Geotification) {
    mapView?.add(MKCircle(center: geotification.coordinate, radius: geotification.radius))
  }
  
  func removeRadiusOverlay(forGeotification geotification: Geotification) {
    // Find exactly one overlay which has the same coordinates & radius to remove
    guard let overlays = mapView?.overlays else { return }
    for overlay in overlays {
      guard let circleOverlay = overlay as? MKCircle else { continue }
      let coord = circleOverlay.coordinate
      if coord.latitude == geotification.coordinate.latitude && coord.longitude == geotification.coordinate.longitude && circleOverlay.radius == geotification.radius {
        mapView?.remove(circleOverlay)
        break
      }
    }
  }
  
  // MARK: Other mapview functions
  @IBAction func zoomToCurrentLocation(sender: AnyObject) {
    mapView.zoomToUserLocation()
  }
  
  func timeSpentTableDelegate(by controller: TimeSpentTable, didPressCancelButton button: UIBarButtonItem) {
    dismiss(animated: true, completion: nil)
  }
  
}

// AddGeotificationViewControllerDelegate

//
extension GeotificationsViewController: AddGeotificationsViewControllerDelegate {
  
  func addGeotificationViewController(controller: AddGeotificationViewController, didAddCoordinate coordinate: CLLocationCoordinate2D, radius: Double, identifier: String, note: String, eventType: EventType) {
    controller.dismiss(animated: true, completion: nil)
    // 1
    let clampedRadius = min(radius, locationManager.maximumRegionMonitoringDistance)
    let geotification = Geotification(coordinate: coordinate, radius: clampedRadius, identifier: identifier, note: note, eventType: eventType)
    add(geotification: geotification)
    // 2
    startMonitoring(geotification: geotification)
    saveAllGeotifications()
  }
  
}

// MARK: - Location Manager Delegate
extension GeotificationsViewController: CLLocationManagerDelegate {
  func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
    mapView.showsUserLocation = (status == .authorizedAlways)
    //to check if the app is authorized. If it is, you enable the map view to show the user’s current location.
  }
  func locationManager(_ manager: CLLocationManager, monitoringDidFailFor region: CLRegion?, withError error: Error) {
    print("Monitoring failed for region with identifier: \(region!.identifier)")
  }
  
  func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
    print("Location Manager failed with the following error: \(error)")
  }
}

//!definitely want to handle these errors more robustly in your production apps. For example, instead of failing silently, you could inform the user what went wrong.
  

// MARK: - MapView Delegate
extension GeotificationsViewController: MKMapViewDelegate {
  
  func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation) -> MKAnnotationView? {
    let identifier = "myGeotification"
    if annotation is Geotification {
      var annotationView = mapView.dequeueReusableAnnotationView(withIdentifier: identifier) as? MKPinAnnotationView
      if annotationView == nil {
        annotationView = MKPinAnnotationView(annotation: annotation, reuseIdentifier: identifier)
        annotationView?.canShowCallout = true
        let removeButton = UIButton(type: .custom)
        removeButton.frame = CGRect(x: 0, y: 0, width: 23, height: 23)
        removeButton.setImage(UIImage(named: "DeleteGeotification")!, for: .normal)
        annotationView?.leftCalloutAccessoryView = removeButton
      } else {
        annotationView?.annotation = annotation
      }
      return annotationView
    }
    return nil
  }
  
  
  func mapView(_ mapView: MKMapView, rendererFor overlay: MKOverlay) -> MKOverlayRenderer {
    if overlay is MKCircle {
      let circleRenderer = MKCircleRenderer(overlay: overlay)
      circleRenderer.lineWidth = 1.0
      circleRenderer.strokeColor = .purple
      circleRenderer.fillColor = UIColor.purple.withAlphaComponent(0.4)
      return circleRenderer
    }
    return MKOverlayRenderer(overlay: overlay)
  }
  
  func mapView(_ mapView: MKMapView, annotationView view: MKAnnotationView, calloutAccessoryControlTapped control: UIControl) {
    // Delete geotification
    let geotification = view.annotation as! Geotification
    stopMonitoring(geotification: geotification)
    remove(geotification: geotification)
    saveAllGeotifications()
  }
  
}
extension GeotificationsViewController: UITableViewDataSource {
  func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    
    print("hello world")
    return spots.count
    
 
  }
  func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    
    let cell = tableView.dequeueReusableCell(withIdentifier: "spottable", for: indexPath)
    
    cell.textLabel?.text = self.spots[indexPath.row]
  
    return cell
  
  }
  

}


