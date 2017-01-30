// given an array of random values, return a new array of only numbers

function arraysifter(arr){
  var arrnew = []
  for(var x = 0; x<arr.length; x++){       //loops through the passed array
    if(typeof arr[x] === "number"){          //checks if the current array value is a number
      arrnew.push(arr[x]);
    }
  }
  return arrnew;
  console.log(arrnew);
}
