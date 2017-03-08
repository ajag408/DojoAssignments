//: Playground - noun: a place where people can play

import UIKit

struct Card{
    var value: String
    var Suit: String
    var numerical_value: Int
}

var values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
var Suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
var numerical_values = [1,2,3,4,5,6,7,8,9,10,11,12,13]


class Deck {
    var cards: [Card] = [Card]()
    init(){
        for i in 0...3{
            let this_Suit = Suits[i]
            for j in 0...12{
                let this_value = values[j]
                let this_num = numerical_values[j]
                let this_card = Card(value: this_value, Suit: this_Suit, numerical_value: this_num)
                cards.append(this_card)
            }
        }
    }

    func deal(current_deck: Deck = Deck())->Card{
        let select = cards.remove(at: cards.count - 1)
        return select
    }
    
    func reset(){
        for i in 0...3{
            let this_Suit = Suits[i]
            for j in 0...12{
                let this_value = values[j]
                let this_num = numerical_values[j]
                let this_card = Card(value: this_value, Suit: this_Suit, numerical_value: this_num)
                cards.append(this_card)
            }
        }
    }
    
    func shuffle(){
        for _ in 1...100{
            let rand1 = Int(arc4random_uniform(51))
            let rand2 = Int(arc4random_uniform(51))
        
            let temp = cards[rand1]
        
            cards[rand1] = cards[rand2]
            cards[rand2] = temp
        
        }
    }
}






class Player {
    var name: String
    var hand: [Card]
    init(name: String, hand: [Card]){
        self.name = name
        self.hand = hand
    }
    
    
    func draw(current_deck: Deck = Deck()) -> Card{
        let drawn = current_deck.deal()
        hand.append(drawn)
        return drawn
    }

    
    func discard(this_card: Card) -> Bool{
        var checker = 0
        for i in 0..<hand.count{
            if this_card.value == hand[i].value && this_card.Suit == hand[i].Suit && this_card.numerical_value == hand[i].numerical_value{
                hand.remove(at: i)
                checker += 1
                return true
            }
        }
        if checker == 0{
            return false
        }
    }
}

