//
//  ViewController.swift
//  tabBarController
//
//  Created by Akash Jagannathan on 3/31/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class FirstViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        print("FirstViewController viewDidLoad")
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        print("FirstViewController viewWillAppear")
    }
}

