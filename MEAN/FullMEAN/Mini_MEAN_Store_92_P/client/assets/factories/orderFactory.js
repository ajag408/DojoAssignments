
app.factory('orderFactory', ['$http', function($http) {
  var factory = {};
  factory.index = function(callback) {
      //call this method if you want to update or set the friends variable
      $http.get('/orders').then(function(returned_data){
        callback(returned_data.data.orders);
      });
  }

  factory.create = function(neworder) {
      $http.post('/orders', neworder).then(function(returned_data){
        console.log(returned_data);
      });
  }

  return factory;
}]);
