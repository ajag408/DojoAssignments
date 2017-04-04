//
//  AddDogViewControllerDelegate.swift
//  myDogs
//
//  Created by Akash Jagannathan on 3/31/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

protocol AddDogViewControllerDelegate: class{
    func addDogViewController(by controller: AddDogViewController, name: String?, color: String?, treat: String?, picture: UIImage)
}
