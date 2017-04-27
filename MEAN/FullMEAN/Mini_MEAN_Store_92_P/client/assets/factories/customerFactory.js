
app.factory('customerFactory', ['$http', function($http) {
  var factory = {};
  factory.index = function(callback) {
      //call this method if you want to update or set the friends variable
      $http.get('/customers').then(function(returned_data){
        for(var i = 0; i<returned_data.data.customers.length; i++){
          console.log(returned_data.data.customers[i].createdAt)
        }

        callback(returned_data.data.customers);
      });
  }
  factory.create = function(newcustomer) {
      $http.post('/customers', newcustomer).then(function(returned_data){
        console.log(returned_data.data)
      });
  }

  factory.delete = function(id) {
      $http.delete('/customers/'+id).then(function(returned_data){
        console.log(returned_data.data);
      })
  }
  return factory;
}]);
