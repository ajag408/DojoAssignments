//
//  ViewController.swift
//  Tipster
//
//  Created by Akash Jagannathan on 3/9/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var Total: UILabel!
    @IBOutlet weak var LowP: UILabel!
    @IBOutlet weak var LowTi: UILabel!
    @IBOutlet weak var LowTo: UILabel!
    @IBOutlet weak var MidP: UILabel!
    @IBOutlet weak var MidTi: UILabel!
    @IBOutlet weak var MidTo: UILabel!
    @IBOutlet weak var HiP: UILabel!
    @IBOutlet weak var HiTi: UILabel!
    @IBOutlet weak var HiTo: UILabel!
    
    @IBOutlet weak var gs: UISlider!
    @IBOutlet weak var gsLabel: UILabel!
    
    @IBAction func LabelAnnotate(_ sender: UISlider) {
        gsLabel.text = "Group Size: " + String(format: "%.0f", gs.value)
    }
    
    @IBAction func numPad(_ sender: UIButton) {
        if sender.tag == 1{
            Total.text?.append("1")
        }
        if sender.tag == 2{
            Total.text?.append("2")
        }
        if sender.tag == 3{
            Total.text?.append("3")
        }
        if sender.tag == 4{
            Total.text?.append("4")
        }
        if sender.tag == 5{
            Total.text?.append("5")
        }
        if sender.tag == 6{
            Total.text?.append("6")
        }
        if sender.tag == 7{
            Total.text?.append("7")
        }
        if sender.tag == 8{
            Total.text?.append("8")
        }
        if sender.tag == 9{
            Total.text?.append("9")
        }
        if sender.tag == 0{
            Total.text?.append("0")
        }
        if sender.tag == -2{
            Total.text?.append(".")
        }
        if sender.tag == -1{
            Total.text?.removeAll()
        }
        
    }
 
    
    @IBAction func tip(_ sender: UISlider) {
        let total = Float(Total.text!)
        LowP.text = String(format: "%.0f", sender.value) + "%"
        MidP.text = String(format: "%.0f", sender.value + 5) + "%"
        HiP.text = String(format: "%.0f", sender.value + 10) + "%"
        LowTi.text = String(format: "%.2f",(sender.value/100) * (total!/gs.value))
        MidTi.text = String(format: "%.2f",((sender.value + 5)/100) * (total!/gs.value))
        HiTi.text = String(format: "%.2f",((sender.value + 10)/100) * (total!/gs.value))
        LowTo.text = String(format: "%.2f", (total!/gs.value) + Float(LowTi.text!)!)
        MidTo.text = String(format: "%.2f", (total!/gs.value) + Float(MidTi.text!)!)
        HiTo.text = String(format: "%.2f", (total!/gs.value) + Float(HiTi.text!)!)
    }
    

    
  
    
//    @IBOutlet weak var Total: UILabel!
//    @IBOutlet weak var LowP: UILabel!
//    @IBOutlet weak var LowTi: UILabel!
//    @IBOutlet weak var LowTo: UILabel!
//    @IBOutlet weak var MidP: UILabel!
//    @IBOutlet weak var MidTi: UILabel!
//    @IBOutlet weak var MidTo: UILabel!
//    @IBOutlet weak var HiP: UILabel!
//    @IBOutlet weak var HiTi: UILabel!
//    @IBOutlet weak var HiTo: UILabel!

    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        Total.text = ""
        LowP.text = "0"
        LowTi.text = "0"
        LowTo.text = "0"
        MidP.text = "0"
        MidTi.text = "0"
        MidTo.text = "0"
        HiP.text = "0"
        HiTi.text = "0"
        HiTo.text = "0"
        gsLabel.text = "Group Size:"
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

