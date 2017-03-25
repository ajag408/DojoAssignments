//
//  ViewController.swift
//  toDoList
//
//  Created by Akash Jagannathan on 3/23/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class AddItemViewController: UIViewController {
    
    @IBOutlet weak var ItemTitleInput: UITextField!
    
    @IBOutlet weak var ItemInfoInput: UITextField!
    
    @IBOutlet weak var UserDateChoice: UIDatePicker!
    
    weak var delegate: AddItemViewControllerDelegate?

    @IBAction func AddItemButtonPressed(_ sender: UIButton) {
        delegate?.addItemViewController(by: self, itemTitle: ItemTitleInput.text!, itemDescription: ItemInfoInput.text!, completionDate: UserDateChoice.date as NSDate)
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

