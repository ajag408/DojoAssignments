
app.controller('newController', ['$scope','***FACTORYNAME***', '$location', function($scope, ***FACTORYNAME***, $location) {
  $scope.create = function() {
      ***FACTORYNAME***.create($scope.newFriend, function(data) {
          // If we needed to display an updated list of friends on this page, we would have to do this;
          $scope.friends = data;
      });
  }
}]);
