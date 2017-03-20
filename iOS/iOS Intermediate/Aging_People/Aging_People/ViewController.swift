//
//  ViewController.swift
//  Aging_People
//
//  Created by Akash Jagannathan on 3/15/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITableViewDataSource{
    

    
    var people = ["Kennedy", "Viz", "Shah", "Ryan", "Jackie", "Basila", "God", "Sam", "Project Pat", "Pat-man", "Zoolander", "Ka$h Money"]
    
    @IBOutlet weak var hazeusView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        hazeusView.dataSource = self
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func tableView(_ hazeusView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return people.count
    }
    
    // How should I create each cell?
    func tableView(_ hazeusView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = hazeusView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath)
        
        cell.textLabel?.text = people[indexPath.row]
        
        let random_age = arc4random_uniform(91) + 5
        
        cell.detailTextLabel?.text = String(random_age) + " years old"
        
        return cell
    }


}

