//
//  ViewController.swift
//  ninjaGold
//
//  Created by Akash Jagannathan on 3/9/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var totalScore: UILabel!
    @IBOutlet weak var farmRes: UILabel!
    @IBOutlet weak var caveRes: UILabel!
    @IBOutlet weak var houseRes: UILabel!
    @IBOutlet weak var casinoRes: UILabel!
    
    var score = 0
    
    func resetBuild(){
        farmRes.isHidden = true
        caveRes.isHidden = true
        houseRes.isHidden = true
        casinoRes.isHidden = true
    }
    
    func resetAll(){
        score = 0
        totalScore.text = "Score: 0"
        farmRes.isHidden = true
        caveRes.isHidden = true
        houseRes.isHidden = true
        casinoRes.isHidden = true
    }

    @IBAction func buildingButtonPressed(_ sender: UIButton) {
        if sender.tag == 1{
            resetBuild()
            farmRes.isHidden = false
            let farmEarnings = arc4random_uniform(11)+10
            farmRes.text = "You Earned \(farmEarnings)!"
            score = score + Int(farmEarnings)
            totalScore.text = "Score: \(score)"
        }
        else if sender.tag == 2{
            resetBuild()
            caveRes.isHidden = false
            let caveEarnings = arc4random_uniform(6)+5
            caveRes.text = "You Earned \(caveEarnings)!"
            score = score + Int(caveEarnings)
            totalScore.text = "Score: \(score)"
        }
        else if sender.tag == 3{
            resetBuild()
            houseRes.isHidden = false
            let houseEarnings = arc4random_uniform(4)+2
            houseRes.text = "You Earned \(houseEarnings)!"
            score = score + Int(houseEarnings)
            totalScore.text = "Score: \(score)"
        }
        else if sender.tag == 4{

            resetBuild()
            casinoRes.isHidden = false
            let casinoEarnings = arc4random_uniform(51)
            let luckSelect = arc4random_uniform(2)
            if luckSelect == 0{
                let neg = Int(casinoEarnings)
                let neg2 = neg * -1
                casinoRes.text = "You Lost \(neg2)!"
                score = score + neg2
                totalScore.text = "Score: \(score)"
            }else{
                casinoRes.text = "You Earned \(casinoEarnings)!"
                score = score + Int(casinoEarnings)
                totalScore.text = "Score: \(score)"
            }
        }
    }
    
    
    @IBAction func resetButtonPressed(_ sender: UIButton) {
        resetAll()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        resetAll()
        // Do any additional setup after loading the view, typically from a nib.
    }



    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

