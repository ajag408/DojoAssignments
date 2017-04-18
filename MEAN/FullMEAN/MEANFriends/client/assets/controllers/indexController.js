
app.controller('indexController', ['$scope','friendsFactory', '$location', function($scope, friendsFactory, $location) {
  var index = function () {
      friendsFactory.index(function(data) {
          $scope.friends = data;
      })
  }
  index();
  $scope.edit = function(user_id) {
    $location.url('/edit/' + user_id);
  }
  $scope.show = function(user_id) {
    $location.url('/show/' + user_id);
  }
  $scope.delete = function(user_id) {
    friendsFactory.delete(user_id);
    index();
  }
}]);
