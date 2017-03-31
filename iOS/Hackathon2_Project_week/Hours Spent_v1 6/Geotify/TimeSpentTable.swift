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
  
  
  var notes: [String: Any] = [:]
  var note_append: [Int: [String:Any]] = [:]

  
    @IBAction func backButtonPressed(_ sender: UIBarButtonItem) {
        delegate?.timeSpentTableDelegate(by: self, didPressCancelButton: sender)
    }
    
    
  override func viewDidLoad() {
    super.viewDidLoad()
    var stored_visits = UserDefaults.standard.dictionaryRepresentation()
    for (key, value) in stored_visits{
      let vA = value as? String
      if vA == "Curry Up Now" || vA == "Park N' Ride"{
    
        notes[key] = vA
        for i in 0..<notes.count{
          note_append[i] = [key: vA]
        }
        stored_visits[key] = nil
        
      }
    }
    
    print(note_append)
    

    

    // Do any additional setup after loading the view, typically from a nib.
    
  }
  
  override func didReceiveMemoryWarning() {
    super.didReceiveMemoryWarning()
    // Dispose of any resources that can be recreated.
  }
  
  override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
    return notes.count
  }
//
//  override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
//    
//  }
  
  override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "ListitemCell", for: indexPath)
    
    
    
    return cell
  }
}
