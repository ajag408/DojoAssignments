//: Playground - noun: a place where people can play

import UIKit

class Animal{
    var name : String
    var health = 100
    init(name: String){
        self.name = name
    }
    
    func displayHealth(){
        print(health)
    }
}

class Cat: Animal{
    func growl(){
        print("Rawr!")
    }
    
    
    init(name: String, health: Int){
        super.init(name:name)
        self.health = 150
    }

    
    func run(){
        if health == 0{
            print("Can't run")
        }else{
            print("Running")
            health = health - 10
        }

    }
}

class Lion: Cat{
    override func growl(){
        print("ROAR!!!! I am the King of the Jungle")
    }
    
    override init(name: String, health: Int){
        super.init(name:name, health:health)
        self.health = 200
    }
}

class Cheetah: Cat{
    override init(name: String, health: Int){
        super.init(name:name, health: health)
        self.health = 200
    }
    override func run(){
        print("Running Fast")
        health = health - 50
    }
    
    func sleep(){
        if(health<150){
            health = health + 50
        }
        else if health>150 && health<200{
            health = 200
        }
    }
}

var cheetah = Cheetah(name:"Cheat", health: 0)
cheetah.run()
cheetah.run()
cheetah.run()
cheetah.run()
cheetah.displayHealth()

var lion = Lion(name: "Ly", health: 0)
lion.run()
lion.run()
lion.run()
lion.growl()
