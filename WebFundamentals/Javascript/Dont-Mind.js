function time(hour, minutes, period){
  if(minutes<30 && hour<=12){
    console.log("It's just after " + hour + " in the " + period);
  }
  else if(minutes>=30 && minutes <= 60 && hour<=12){
    console.log("It's almost " + hour + " in the " + period);
  }
  else{
    console.log("Time value must be in the range of 1 through 12, and the minutes must be between 1-60");
  }
}
