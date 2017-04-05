function VehicleConstructor(name,numWheels,numPassengers,speed){

    var distance_traveled = 0;
    var updateDistanceTraveled = function(){
      distance_traveled = distance_traveled + speed;
    };

      this.name = name;
      this.numWheels = numWheels;
      this.numPassengers = numPassengers;
      this.makeNoise = function(noiseYouWant){
        console.log(noiseYouWant);
      };
      this.speed = speed;
      this.move = function(){
        updateDistanceTraveled();
        this.makeNoise();
      };
      this.checkMiles = function(){
        console.log(distance_traveled);
      };

}




var bike = new VehicleConstructor("lucy", 2, 1, 15);
bike.checkMiles();
bike.move();
bike.move();
bike.checkMiles();
