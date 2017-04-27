
app.factory('productFactory', ['$http', function($http) {
  var factory = {};
  factory.index = function(callback) {
      //call this method if you want to update or set the friends variable
      $http.get('/products').then(function(returned_data){
        callback(returned_data.data.products);
      });
  }
  factory.create = function(newproduct) {
      $http.post('/products', newproduct).then(function(returned_data){
        console.log("product factory create method");
      });
  }
  factory.getProduct = function(product, callback){
    $http.post('/product', product).then(function(returned_data){
      callback(returned_data.data.product[0].qty);
    })
  }
  factory.update = function(product){
    $http.post('/update', product).then(function(returned_data){
      console.log();
    })
  }
  return factory;
}]);
