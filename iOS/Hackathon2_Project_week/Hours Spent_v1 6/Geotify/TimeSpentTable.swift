//
//  TimeSpentTable.swift
//  Hours Spent
//
//  Created by Akash Jagannathan on 3/27/17.
//  Copyright © 2017 Ryan Munguia. All rights reserved.
//

import UIKit

class TimeSpentTable: UITableViewController{

  weak var delegate: TimeSpentTableDelegate?
  
  var geotifications: [String] = []
  
    @IBAction func backButtonPressed(_ sender: UIBarButtonItem) {
        delegate?.timeSpentTableDelegate(by: self, didPressCancelButton: sender)
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
