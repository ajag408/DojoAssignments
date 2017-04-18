app.controller('editController', ['$scope','friendsFactory', '$routeParams', function($scope, friendsFactory, $routeParams) {
   friendsFactory.show($routeParams.id, function(returnedData){
     $scope.friend = returnedData;
     console.log($scope.friend);
   });
   $scope.update = function(){
     console.log("editController");
     console.log($scope.friend.birthday);
     friendsFactory.update($routeParams.id, $scope.friend);
   }
  /*
    OUR $scope.update function goes here <-- $scope because we need to access this method
    with ng-submit or ng-click (from the form in the previous assignment).  Want to see
    all of the friends when we get back including the updated on??
    See Index in the previous controller.
  */
}]);
