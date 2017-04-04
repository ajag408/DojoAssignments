function personConstructor(name){
  var person = {

      name: name,
      distance_traveled: 0,
      say_name: function(){
        console.log(person.name);
      },
      say_something: function(param1){
        console.log(person.name + " says " + param1);
      },
      walk: function(){
        console.log(person.name + " is walking");
        person.distance_traveled = person.distance_traveled + 3;
      },
      run: function(){
        console.log(object.name + " is running");
        person.distance_traveled = person.distance_traveled + 10;
      },
      crawl: function(){
        console.log(person.name + " is crawling");
        person.distance_traveled = person.distance_traveled + 1;
      }

  }
  return person;
}

function ninjaConstructor(name, cohort){
  var ninja = {
    name: name,
    cohort: cohort,
    belt_level: "yellow",
    levelUp: function(belt_level){
      if(belt_level === "yellow"){
        ninja.belt_level = "red";
      } else if(belt_level === "red"){
        ninja.belt_level = "black";
      }
    }
  }
  return ninja;
}

var akash = ninjaConstructor("James", "Spring 17");
console.log(akash.belt_level);
akash.levelUp(akash.belt_level);
akash.levelUp(akash.belt_level);
console.log(akash.belt_level);
