//
//  AppDelegate.swift
//  Hours Spent
//
//  Created by Ryan Munguia on 3/16/17.
//  Copyright © 2017 Ryan Munguia. All rights reserved.
//

import CoreLocation
import UIKit
import CoreData


extension AppDelegate: CLLocationManagerDelegate {
  //when the device enters a CLRegion, while you fire locationManager(_:didExitRegion:) when the device exits a CLRegion.
  func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion) {
    if region is CLCircularRegion {
       
      handleEvent(forRegion: region)
//      notes[note(fromRegionIdentifier: region.identifier)] = timeTest()

    }
  }
  
  func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion) {
    if region is CLCircularRegion {
      handleEvent(forRegion: region)
    }
  }
}

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate{
  
  var window: UIWindow?
  
  let locationManager = CLLocationManager()
  
  
  
  func handleEvent(forRegion region: CLRegion!) {
    // Show an alert if application is active
    if UIApplication.shared.applicationState == .active {
      guard let message = note(fromRegionIdentifier: region.identifier) else { return }
      window?.rootViewController?.showAlert(withTitle: nil, message: message)
    } else {
      // Otherwise present a local notification
      let notification = UILocalNotification()
      notification.alertBody = note(fromRegionIdentifier: region.identifier)
      notification.soundName = "Default"
      UIApplication.shared.presentLocalNotificationNow(notification)
    }
  }
  
//  var test = note(fromRegionIdenti)
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
    locationManager.delegate = self
    locationManager.requestAlwaysAuthorization()
    application.registerUserNotificationSettings(UIUserNotificationSettings(types: [.sound, .alert, .badge], categories: nil)) //The code you’ve added prompts the user for permission to enable notifications for this app.
    UIApplication.shared.cancelAllLocalNotifications()
    return true
    
  }
  //This helper method retrieves the geotification note from the persistent store, based on its identifier, and returns the note for that geotification.
  func note(fromRegionIdentifier identifier: String) -> String? {
    let savedItems = UserDefaults.standard.array(forKey: PreferencesKeys.savedItems) as? [NSData]
    let geotifications = savedItems?.map { NSKeyedUnarchiver.unarchiveObject(with: $0 as Data) as? Geotification }
    let index = geotifications?.index { $0?.identifier == identifier }
    let date = Date()
    let calendar = Calendar.current
    let hour = calendar.component(.hour, from: date)
    let minutes = calendar.component(.minute, from: date)
    //let seconds = calendar.component(.second, from: date)

    return index != nil ? geotifications?[index!]?.note : nil
  }
  
    func timeTest() -> String{
    let date = Date()
    let calendar = Calendar.current
    let hour = calendar.component(.hour, from: date)
    let minutes = calendar.component(.minute, from: date)
    let seconds = calendar.component(.second, from: date)
    var currentTime = "\(hour):\(minutes):\(seconds)"
    return currentTime
    
  }
  


  
}
  
  


