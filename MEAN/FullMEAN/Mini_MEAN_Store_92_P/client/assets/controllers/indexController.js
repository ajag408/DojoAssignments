
app.controller('indexController', ['$scope','productFactory', 'orderFactory', 'customerFactory', '$location', function($scope, productFactory, orderFactory, customerFactory, $location) {
  var productIndex = function () {
      productFactory.index(function(data) {
          $scope.products = data;
      })
  }
  var orderIndex = function () {
      orderFactory.index(function(data) {
          var currentDate = new Date();
          console.log(currentDate);
          $scope.orders = data;
      })
  }
  var customerIndex = function () {
      customerFactory.index(function(data) {
          $scope.customers = data;
          console.log($scope.customers);
      })
  }
  productIndex();
  orderIndex();
  customerIndex();


}]);
