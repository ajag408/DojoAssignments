//
//  ViewController.swift
//  rainbowRoad
//
//  Created by Akash Jagannathan on 3/15/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITableViewDataSource {

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
        return 6
    }
    
    // How should I create each cell?
    func tableView(_ hazeusView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = hazeusView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath)
        
        if indexPath.row == 0 {
            cell.backgroundColor = UIColor.red
        }
        
        if indexPath.row == 1 {
            cell.backgroundColor = UIColor.orange
        }
        
        if indexPath.row == 2 {
            cell.backgroundColor = UIColor.yellow
        }
        
        if indexPath.row == 3 {
            cell.backgroundColor = UIColor.green
        }
        
        if indexPath.row == 4 {
            cell.backgroundColor = UIColor.blue
        }
        
        if indexPath.row == 5 {
            cell.backgroundColor = UIColor.purple
        }
        
        return cell
    }



}

