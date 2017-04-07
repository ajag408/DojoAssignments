function Card(value, suit){
  this.value = value;
  this.suit = suit;
}

var values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
var Suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
var numerical_values = [1,2,3,4,5,6,7,8,9,10,11,12,13]

function deckConstructor(){

  function makeDeck(){
    var deck = [];
    for(var i = 0; i<4; i++){
      this_suit = Suits[i];
      for(var j =0; j<13; j++){
        this_value = values[j];
        this_card = new Card(this_value, this_suit);
        deck.push(this_card);
      }
    }
    return deck;
  }
  this.deck = makeDeck();
  // var newDeck = makeDeck();
  // this.deck = newDeck;
  this.shuffle = function(){
    var m = this.deck.length, t, i;
    while(m){
      i = Math.floor(Math.random() * m--);
      t = this.deck[m];
      this.deck[m] = this.deck[i];
      this.deck[i] = t;
    }
    return this.deck;
  };
  this.reset = function(){
    this.deck = makeDeck();
  };
  this.deal = function(){
    var currLen = this.deck.length;
    var index = Math.floor(Math.random() * (currLen-1)) + 1;
    var one = this.deck[index];
    this.deck.splice(index, 1);
    return one;
  };
}

function playerConstructor(name){
  this.name = name;
  this.hand = [];
  this.draw = function(deck){
    var pick = deck.deal();
    this.hand.push(pick);
  };
  this.discard = function(index){
    if(index >= 0 && index < this.hand.length){
      this.hand.splice(index);
      return this.hand;
    } else {
      console.log("be true foo");
    }
  }
}

var player1 = new playerConstructor("TimmyJ");
var newDeck = new deckConstructor();
console.log(newDeck.deck.length);
newDeck.shuffle();
player1.draw(newDeck);
console.log(player1.hand);
