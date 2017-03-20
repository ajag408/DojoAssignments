//: Playground - noun: a place where people can play

import UIKit

func tossCoin() -> String{
    print("Tossing a Coin!")
    let select = Int(arc4random_uniform(1))
    var result = String()
    if select == 1{
        result = "Heads"
        print(result)
        return result
    }
    else{
        result = "Tails"
        print(result)
        return result
    }
}

func tossMultipleCoins(iters: Int) -> Double{
    var headCount = 0
    var tailCount = 0
    for _ in 1...iters{
        if tossCoin() == "Heads"{
            headCount += 1
        }else{
            tailCount += 1
        }
    }
    let ratio: Double = Double(headCount)/Double(tailCount)
    return ratio
}


