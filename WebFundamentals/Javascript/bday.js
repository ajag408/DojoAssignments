//starting from current day,
  // print how many days from bday there is
  //print state of mind based on above
  //increment down day by days



  function countdown(days){
    for(var x = days; x>=0; x--){
      console.log("Days until my bday " + x);
      if(x<=365 && x>30){
        console.log("I'm sad, can't wait till my bday, only " + x + " days left...");
      }
      else if(x<=30 && x>5){
        console.log("Woo less than " + x + " days till my bday");
      }
      else if(x<=5 && x>0){
        console.log("I'm screaming, my bday is less than 5 days");
      }
      else if (x===0){
        console.log("Today");
      }
    }
  }

  countdown(50);
