
app.controller('productController', ['$scope','productFactory', function($scope, productFactory) {
  var index = function () {
      productFactory.index(function(data) {
          $scope.products = data;
      })
  }
  index();

  $scope.create = function() {
      $scope.newProduct.qty = Number($scope.newProduct.qty);
      console.log($scope.newProduct);
      productFactory.create($scope.newProduct);
      index();
  }
}]);
