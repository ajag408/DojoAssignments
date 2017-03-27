//
//  ViewController.swift
//  cold_call
//
//  Created by Akash Jagannathan on 3/9/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var nameView: UILabel!
    @IBOutlet weak var numberView: UILabel!

    var names = [("Johnny", "1"), ("BehenChoth","2"), ("T-Bone","3"), ("Jerm","4"), ("Face","5")]
    
    @IBAction func coldCallPressed(_ sender: UIButton) {
        numberView.isHidden = false
        let randIndex = arc4random_uniform(UInt32(names.count))
        
        let numRand = Int(randIndex)
        print(numRand)
        nameView.text = names[numRand].0
        numberView.text = names[numRand].1
        let checker = (numberView.text)!
        if checker == "1" || checker == "2"{
            numberView.textColor = UIColor.red
        }
        else if checker == "3" || checker == "4"{
            numberView.textColor = UIColor.orange
        }
        else{
            numberView.textColor = UIColor.green
        }
      
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        nameView.text = "Ready?"
        numberView.isHidden = true

        // Do any additional setup after loading the view, typically from a nib.
    }
    
//    func updateUI(){
//        let rand1 = arc4random_uniform(UInt32(names.count)) - 1
//        nameView.text = names[Int(rand1)]
//    }
//
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

