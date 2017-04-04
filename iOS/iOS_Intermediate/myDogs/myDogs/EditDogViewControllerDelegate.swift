//
//  EditDogViewControllerDelegate.swift
//  myDogs
//
//  Created by Akash Jagannathan on 4/2/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

protocol EditDogViewControllerDelegate: class{
    func editDogViewController(by controller: EditDogViewController, didPressCancelButton: UIBarButtonItem)
    func editDogViewController(by controller: EditDogViewController, name: String?, color: String?, treat: String?, picture: UIImage?, indexPath: NSIndexPath)
    func editDogViewController(by controller: EditDogViewController, indexPath: NSIndexPath)

}
