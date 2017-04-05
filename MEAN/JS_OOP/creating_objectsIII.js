function VehicleConstructor(name,numWheels,numPassengers,speed){

    var distance_traveled = 0;
    var updateDistanceTraveled = function(){
      distance_traveled = distance_traveled + speed;
    };

      this.name = name;
      this.numWheels = numWheels;
      this.numPassengers = numPassengers;
      this.speed = speed;
      this.move = function(noiseYouWant){
        updateDistanceTraveled();
        this.makeNoise(noiseYouWant);
      };
      this.checkMiles = function(){
        console.log(distance_traveled);
      };

}

VehicleConstructor.prototype.makeNoise = function(noiseYouWant){
  console.log(noiseYouWant);
};

VehicleConstructor.prototype.VIN = Math.floor(Math.random()*1000000 + 6000000);

var ninjaBoatCruiser = new VehicleConstructor('jimm', 5, 15, 25);
console.log(ninjaBoatCruiser.VIN);
