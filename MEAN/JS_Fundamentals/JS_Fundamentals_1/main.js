var x = [3.5, "Dojo", "rocks", "Michael", "Sensei"];
for(var i = 0; i<x.length; i++){
  console.log(x[i]);
}
x.push(100);

x.push(["hello","world","JavaScript is Fun"]);

var sum = 0;

for(var i = 1; i<=500; i++){
  sum = sum + i;
}

console.log(sum)

var minmaxArr = [1,5,90,25,-3,0];

var min = minmaxArr[0];

for(var i = 0; i<minmaxArr.length; i++){
  if(minmaxArr[i]<min){
    min = minmaxArr[i];
  }
}
console.log(min);

var total = 0;

for(var i = 0; i<minmaxArr.length; i++){
  total = total + minmaxArr[i];
}

var avg = total/minmaxArr.length

console.log(avg)

var newNinja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
}

for (var key in newNinja){
  console.log(key, newNinja[key]);
}
