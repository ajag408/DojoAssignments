
app.controller('customerController', ['$scope','customerFactory', function($scope, customerFactory) {
  var index = function () {
      customerFactory.index(function(data) {
          $scope.customers = data;
      })
  }
  index();

  $scope.create = function() {
      customerFactory.create($scope.newCustomer);
      index();
  }
  $scope.delete = function(customer_id) {
    customerFactory.delete(customer_id);
    index();
  }
}]);
