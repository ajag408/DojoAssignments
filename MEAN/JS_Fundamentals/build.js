function runningLogger(){
  console.log('I am running!');
}

runningLogger();

function multiplyByTen(num){
  result = num * 10;
  return result;
}
multiplyByTen(5);
console.log(result);


function stringReturnOne(){
  return "string1";
}

function stringReturnTwo(){
  return "string2";
}

function caller(arg){
  if(typeof(arg) == "function"){
    arg()
  }
}

caller(stringReturnOne);

function myDoubleConsoleLog(p1, p2){
  if(typeof(p1) == "function" && typeof(p2) == "function"){
    console.log(p1());
    console.log(p2());
  }
}

myDoubleConsoleLog(stringReturnOne, stringReturnTwo);

function caller2(param){
  console.log('starting');
  setTimeout(function(){
    if(typeof(param) == "function"){
      param()
    }
  }, 2000);
  console.log('ending');
  return "interesting";
}

caller2(stringReturnOne);
