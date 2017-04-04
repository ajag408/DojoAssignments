//
//  ViewController.swift
//  myDogs
//
//  Created by Akash Jagannathan on 3/31/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit
import CoreData

class CollectionViewController: UICollectionViewController, AddDogViewControllerDelegate, EditDogViewControllerDelegate{
    
    let managedObjectContext = (UIApplication.shared.delegate as! AppDelegate).persistentContainer.viewContext
    
    var dogs = [Dog]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        FetchAllItems()
        print(dogs)
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return dogs.count
    }

    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "dogView", for: indexPath) as! DogCell
        
        cell.name.text = dogs[indexPath.row].name
        
        let pictureData = dogs[indexPath.row].image
        let picture = UIImage(data: pictureData as! Data)
        cell.pic.image = picture
        
        
        return cell
    }
    
    override func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        performSegue(withIdentifier: "edit", sender: indexPath)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let sender = sender as? NSIndexPath{
            let navigationController = segue.destination as! UINavigationController
            let controller = navigationController.topViewController as! EditDogViewController
            controller.delegate = self
            let indexPath = sender as! NSIndexPath
            controller.index = indexPath
            controller.OGname = dogs[indexPath.row].name
            controller.OGcolor = dogs[indexPath.row].color
            controller.OGtreat = dogs[indexPath.row].treat
            let pictureData = dogs[indexPath.row].image
            let picture = UIImage(data: pictureData as! Data)
            controller.OGpic = picture
            
        } else {
            let controller = segue.destination as! AddDogViewController
            controller.delegate = self
        }
    }
    
    func FetchAllItems(){
        let request = NSFetchRequest<NSFetchRequestResult>(entityName: "Dog")
        do{
            let results = try managedObjectContext.fetch(request)
            dogs = results as! [Dog]
        } catch {
            print(error)
        }
    }
    func addDogViewController(by controller: AddDogViewController, name: String?, color: String?, treat: String?, picture: UIImage){
        let newDog = Dog(context: managedObjectContext)
        newDog.name = name
        newDog.color = color
        newDog.treat = treat
        let imageData = NSData(data: UIImageJPEGRepresentation(picture, 1.0)!)
        newDog.image = imageData
        do{
            try managedObjectContext.save()
        }catch{
            print(error)
        }
        FetchAllItems()
        collectionView?.reloadData()
        navigationController?.popViewController(animated: true)
    }
    
    func editDogViewController(by controller: EditDogViewController, didPressCancelButton: UIBarButtonItem){
        dismiss(animated: true, completion: nil)
    }
    
    func editDogViewController(by controller: EditDogViewController, name: String?, color: String?, treat: String?, picture: UIImage?, indexPath: NSIndexPath){
        dogs[indexPath.row].name = name
        dogs[indexPath.row].color = color
        dogs[indexPath.row].treat = treat
        let imageData = NSData(data: UIImageJPEGRepresentation(picture!, 1.0)!)
        dogs[indexPath.row].image = imageData
        do{
            try managedObjectContext.save()
        }catch{
            print(error)
        }
        FetchAllItems()
        collectionView?.reloadData()
        dismiss(animated: true, completion: nil)
    }
    
    func editDogViewController(by controller: EditDogViewController, indexPath: NSIndexPath){
        managedObjectContext.delete(dogs[indexPath.row])
        do{
            try managedObjectContext.save()
        }catch{
            print(error)
        }
        FetchAllItems()
        collectionView?.reloadData()
        dismiss(animated: true, completion: nil)    
    }
}
