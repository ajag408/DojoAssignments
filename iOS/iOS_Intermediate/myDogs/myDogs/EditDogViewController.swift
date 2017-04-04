//
//  EditDogViewController.swift
//  myDogs
//
//  Created by Akash Jagannathan on 4/2/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class EditDogViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate{
    
    weak var delegate: EditDogViewControllerDelegate?
    
    var index: NSIndexPath?
    
    @IBOutlet weak var name: UITextField!
    var OGname: String?
    
    @IBOutlet weak var color: UITextField!
    var OGcolor: String?
    
    @IBOutlet weak var treat: UITextField!
    var OGtreat: String?
    
    @IBOutlet weak var currentPicture: UIImageView!
    var OGpic: UIImage?
    
    @IBAction func cancelButtonPressed(_ sender: UIBarButtonItem) {
        delegate?.editDogViewController(by: self, didPressCancelButton: sender)
    }
    
    @IBAction func doneButtonPressed(_ sender: Any) {
        delegate?.editDogViewController(by: self, name: name.text, color: color.text, treat: treat.text, picture: currentPicture.image, indexPath: index!)
    }
    
    var imagePicker = UIImagePickerController()
    
    @IBAction func changePicButtonPressed(_ sender: UIButton) {
        if UIImagePickerController.isSourceTypeAvailable(.savedPhotosAlbum){
            
            
            imagePicker.delegate = self
            imagePicker.sourceType = .savedPhotosAlbum;
            imagePicker.allowsEditing = false
            
            self.present(imagePicker, animated: true, completion: nil)
        }
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) {
        if let image = info[UIImagePickerControllerOriginalImage] as? UIImage {
            currentPicture.image = image
        } else{
            print("Something went wrong")
        }
        
        self.dismiss(animated: true, completion: nil)
    }
    
    @IBAction func deleteButtonPressed(_ sender: UIButton) {
        delegate?.editDogViewController(by: self, indexPath: index!)
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        name.text = OGname
        color.text = OGcolor
        treat.text = OGtreat
        currentPicture.image = OGpic
        
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
