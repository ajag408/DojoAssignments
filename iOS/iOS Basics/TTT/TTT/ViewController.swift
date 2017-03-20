//
//  ViewController.swift
//  TTT
//
//  Created by Akash Jagannathan on 3/9/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var winner: UILabel!
    
    var gameOn = true
    var counter = 0
    var dict = [Int:String]()
    var sender1: [UIButton] = []
    @IBAction func buttonClick(_ sender: UIButton){
        sender1.append(sender)
        if gameOn == true && (dict[sender.tag] != "red" || dict[sender.tag] != "blue"){
            if counter%2 == 0{
                dict[sender.tag] = "red"
                sender.backgroundColor = UIColor.red
                counter = counter+1
            }else{
                dict[sender.tag] = "blue"
                sender.backgroundColor = UIColor.blue
                counter = counter+1
            }
            if counter>=3{
                if checkRows()==true || checkCols() == true || checkDiag()==true {
                    gameOn = false
                }
            }
        }
        if gameOn == true && counter == 9{
            winner.isHidden = false
            winner.text = "Stalemate"
            gameOn = false
        }
    }
    
    
    
    @IBAction func resetButtonClick(_ sender: UIButton) {
        Reset()
    }
    
    
    
    func checkRows() -> Bool{
        if dict[1] == "red" && dict[2] == "red" && dict[3] == "red"{
            winner.isHidden = false
            winner.text = "Congrats red won!"
            return true
        }
        else if dict[4] == "red" && dict[5] == "red" && dict[6] == "red"{
            winner.isHidden = false
            winner.text = "Congrats red won!"
            return true
        }
        else if dict[7] == "red" && dict[8] == "red" && dict[9] == "red"{
            winner.isHidden = false
            winner.text = "Congrats red won!"
            return true
        }
        else if dict[1] == "blue" && dict[2] == "blue" && dict[3] == "blue"{
            winner.isHidden = false
            winner.text = "Congrats blue won!"
            return true
        }
        else if dict[4] == "blue" && dict[5] == "blue" && dict[6] == "blue"{
            winner.isHidden = false
            winner.text = "Congrats blue won!"
            return true
        }
        else if dict[7] == "blue" && dict[8] == "blue" && dict[9] == "blue"{
            winner.isHidden = false
            winner.text = "Congrats blue won!"
            return true
        }else{
            return false
        }
    }
    
    func checkCols() -> Bool{
        if dict[1] == "red" && dict[4] == "red" && dict[7] == "red"{
            winner.isHidden = false
            winner.text = "Congrats red won!"
            return true
        }
        else if dict[2] == "red" && dict[5] == "red" && dict[9] == "red"{
            winner.isHidden = false
            winner.text = "Congrats red won!"
            return true
        }
        else if dict[3] == "red" && dict[6] == "red" && dict[9] == "red"{
            winner.isHidden = false
            winner.text = "Congrats red won!"
            return true
        }
        else if dict[1] == "blue" && dict[4] == "blue" && dict[7] == "blue"{
            winner.isHidden = false
            winner.text = "Congrats blue won!"
            return true
        }
        else if dict[2] == "blue" && dict[5] == "blue" && dict[8] == "blue"{
            winner.isHidden = false
            winner.text = "Congrats blue won!"
            return true
        }
        else if dict[3] == "blue" && dict[6] == "blue" && dict[9] == "blue"{
            winner.isHidden = false
            winner.text = "Congrats blue won!"
            return true
        }else{
            return false
        }
    }
    
    func checkDiag() -> Bool{
        if dict[1] == "red" && dict[5] == "red" && dict[9] == "red"{
            winner.isHidden = false
            winner.text = "Congrats red won!"
            return true
        }
        else if dict[3] == "red" && dict[5] == "red" && dict[7] == "red"{
            winner.isHidden = false
            winner.text = "Congrats red won!"
            return true
        }
        else if dict[1] == "blue" && dict[5] == "blue" && dict[9] == "blue"{
            winner.isHidden = false
            winner.text = "Congrats blue won!"
            return true
        }
        else if dict[3] == "blue" && dict[5] == "blue" && dict[7] == "blue"{
            winner.isHidden = false
            winner.text = "Congrats blue won!"
            return true
        }else{
            return false
        }
    }
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        winner.isHidden = true
        // Do any additional setup after loading the view, typically from a nib.
    }
    

    
    func Reset(){
        counter = 0
        winner.isHidden = true
        gameOn = true
        dict = [Int:String]()
        for b in sender1{
            b.backgroundColor = UIColor.white
        }
        sender1 = []
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

