
app.controller('newController', ['$scope','friendsFactory', '$location', function($scope, friendsFactory, $location) {
  $scope.create = function() {
      console.log($scope.newFriend);
      friendsFactory.create($scope.newFriend, function(data) {
          // If we needed to display an updated list of friends on this page, we would have to do this;
          $scope.friends = data;
      });
  }
}]);
