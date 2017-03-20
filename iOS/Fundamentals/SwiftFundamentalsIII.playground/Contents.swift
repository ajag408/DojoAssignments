//: Playground - noun: a place where people can play

import UIKit

var init_array: [String] = [String]()
for i in 1...255{
    init_array.append(String(i))
}



//for j in 1...100{
//var rand1 = Int(arc4random_uniform(256)) - 1
//var rand2 = Int(arc4random_uniform(256)) - 1
//
//var temp = init_array[rand1]
//    
//init_array[rand1] = init_array[rand2]
//init_array[rand2] = temp
//
//}

init_array.remove(at: 41)
init_array.insert("We found the answer to the Ultimate Question of Life, the Universe, and Everything at index 41", at: 41)