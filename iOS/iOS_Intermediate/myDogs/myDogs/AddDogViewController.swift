//
//  AddDogViewController.swift
//  myDogs
//
//  Created by Akash Jagannathan on 3/31/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class AddDogViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate{
    
    weak var delegate: AddDogViewControllerDelegate?
    
    @IBOutlet weak var nameInput: UITextField!
    
    @IBOutlet weak var colorInput: UITextField!
    
    @IBOutlet weak var treatInput: UITextField!
    
    @IBOutlet weak var dogPhotoPreview: UIImageView!
    
    
    var imagePicker = UIImagePickerController()

    @IBAction func addPhotoPressed(_ sender: UIButton) {

        
        if UIImagePickerController.isSourceTypeAvailable(.savedPhotosAlbum){
           
            
            imagePicker.delegate = self
            imagePicker.sourceType = .savedPhotosAlbum;
            imagePicker.allowsEditing = false
            
            self.present(imagePicker, animated: true, completion: nil)
        }

    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) {
        if let image = info[UIImagePickerControllerOriginalImage] as? UIImage {
            dogPhotoPreview.image = image
        } else{
            print("Something went wrong")
        }
        
        self.dismiss(animated: true, completion: nil)
    }

//    func imagePickerController(picker: UIImagePickerController!, didFinishPickingImage image: UIImage!, editingInfo: NSDictionary!){
//        self.dismiss(animated: true, completion: { () -> Void in
//            
//        })
//        
//        dogPhotoPreview.image = image
//    }
    
    @IBAction func addDogPressed(_ sender: UIButton) {
        delegate?.addDogViewController(by: self, name: nameInput.text, color: colorInput.text, treat: treatInput.text, picture: dogPhotoPreview.image!)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
