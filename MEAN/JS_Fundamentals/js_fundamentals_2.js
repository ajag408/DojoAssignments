var papa = function(x,y){
  for(var i = x; i<=y; i++){
    sum = sum + i;
  }
  console.log(sum)
}

var behen = function(arr){
  var min = arr[0];
  for(var i = 0; i<arr.length; i++){
    if(arr[i]<min){
      min = arr[i];
    }
  }
  return min;
}

var maki = function(arr){
  var total = 0;
  for(var i = 0; i<arr.length; i++){
    total = total + minmaxArr[i];
  }
  var avg = total/arr.length
  return avg;
}

var object = {
  papaFunc: function(x,y){
    for(var i = x; i<=y; i++){
      sum = sum + i;
    }
    console.log(sum)
  },

  behenFunc: function(arr){
    var min = arr[0];
    for(var i = 0; i<arr.length; i++){
      if(arr[i]<min){
        min = arr[i];
      }
    }
    return min;
  },

  makiFunc: function(arr){
    var total = 0;
    for(var i = 0; i<arr.length; i++){
      total = total + minmaxArr[i];
    }
    var avg = total/arr.length
    return avg;
  }
}

var person = {
  name: "Akash",
  distance_traveled: 0,
  say_name: function(){
    console.log(this.name);
  },
  say_something: function(param1){
    console.log(this.name + " says " + param1);
  },
  walk: function(){
    console.log(this.name + " is walking");
    this.distance_traveled = this.distance_traveled + 3;
  },
  run: function(){
    console.log(this.name + " is running");
    this.distance_traveled = this.distance_traveled + 10;
  },
  crawl: function(){
    console.log(this.name + " is crawling");
    this.distance_traveled = this.distance_traveled + 1;
  }
}
