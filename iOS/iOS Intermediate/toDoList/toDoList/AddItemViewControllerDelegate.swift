//
//  AddItemViewControllerDelegate.swift
//  toDoList
//
//  Created by Akash Jagannathan on 3/23/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

protocol AddItemViewControllerDelegate: class{
    func addItemViewController(by controller: AddItemViewController, itemTitle: String, itemDescription: String, completionDate: NSDate)
}
