//function that takes quarters
//1 in 100 chance to win slot machine
  //winning gives rand(50-100)


//if user still has quarters left
  //play
  //did they win?
    //reward them between 50-100 quarters
  //increment down by 1 quarters

// when quarters are 0, return 0

function slot(quarters){
  while(quarters>0){    //while the user still has quarters
    quarters--;  //fee of 1 quarter to play
    console.log("you have " + quarters + " quarters left");
    var arr=[];
    for(var x =1; x<=100; x++){ //creates an array of numbers from 1-100, incremented by 1
      arr.push(x);
    }
      var y = Math.floor(Math.random()*99); //sets variable y to a random number between 0-99
    var user_number = arr[y]; //user_number is a randomly selected number between 1-100;
    if(user_number === 76){ //76 is the arbitrarily chosen winning number, giving the chance of winning a 1/100 prob.
      console.log("you won");
      var rewards = (Math.floor(Math.random() *50)) + 51
      console.log("you have gained " + rewards + " quarters");
      quarters += rewards;  //grants user a reward of between 51-100 coins
      console.log("your total is now " + quarters + " quarters");
    }
  }
  console.log("You have no quarters left");
  return 0;
}
