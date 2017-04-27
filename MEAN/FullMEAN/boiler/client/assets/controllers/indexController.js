
app.controller('indexController', ['$scope','***FACTORYNAME***', '$location', function($scope, ***FACTORYNAME***, $location) {
  var index = function () {
      ***FACTORYNAME***.index(function(data) {
          $scope.***VAR*** = data;
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
    ***FACTORYNAME***.delete(user_id);
    index();
  }
}]);
