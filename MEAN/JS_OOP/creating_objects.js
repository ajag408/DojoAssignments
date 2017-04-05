function VehicleConstructor(name, numWheels, numPassengers){
  var vehicle = {
    name: name,
    numWheels: numWheels,
    numPassengers: numPassengers,
    makeNoise: function(noiseYouWant){
      console.log(noiseYouWant);
    }

  }
  return vehicle;
}

var bike = VehicleConstructor("lucy", 2, 1);
bike.makeNoise("ring ring!");
var sedan = VehicleConstructor("sed", 4, 4);
sedan.makeNoise("honk honk!");
var bus = VehicleConstructor("bo", 18, 18);
bus.pickup = function(numPassengers2Pick){
  bus.numPassengers = bus.numPassengers + numPassengers2Pick;
}

console.log(bus.numPassengers);
bus.pickup(15);
console.log(bus.numPassengers);
