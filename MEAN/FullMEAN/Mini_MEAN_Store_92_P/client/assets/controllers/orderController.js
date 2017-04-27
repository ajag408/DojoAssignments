app.controller('orderController', ['$scope','productFactory', 'customerFactory', 'orderFactory', function($scope, productFactory, customerFactory, orderFactory) {
  var productIndex = function () {
      productFactory.index(function(data) {
          $scope.products = data;
      })
  }
  var customerIndex = function () {
      customerFactory.index(function(data) {
          $scope.customers = data;
      })
  }
  productIndex();
  customerIndex();

  var index = function () {
      orderFactory.index(function(data) {
          $scope.orders = data;
      })
  }

  index();

  $scope.create = function() {
      $scope.newOrder.qty = Number($scope.newOrder.qty);
      productFactory.getProduct($scope.newOrder, function(data){

        $scope.productQty = data;
        if($scope.productQty>=$scope.newOrder.qty){
          $scope.newOrder.qtyUpdate = $scope.productQty - $scope.newOrder.qty;
          console.log($scope.newOrder.qtyUpdate);
          productFactory.update($scope.newOrder);
          orderFactory.create($scope.newOrder);
          $scope.error = "";
        } else {
          $scope.error = "Not enough of that product in stock";
        }

      });




      index();
  }

}]);
