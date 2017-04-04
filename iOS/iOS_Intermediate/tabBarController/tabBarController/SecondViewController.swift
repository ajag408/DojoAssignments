//
//  SecondViewController.swift
//  tabBarController
//
//  Created by Akash Jagannathan on 3/31/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit
class SecondViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        print("SecondViewController viewDidLoad")
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        print("SecondViewController viewWillAppear")
    }
}
