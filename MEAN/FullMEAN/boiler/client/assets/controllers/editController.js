app.controller('editController', ['$scope','***FACTORYNAME***', '$routeParams', function($scope, ***FACTORYNAME***, $routeParams) {
   ***FACTORYNAME***.show($routeParams.id, function(returnedData){
     $scope.***VAR*** = returnedData;
   });
   $scope.update = function(){
     ***FACTORYNAME***.update($routeParams.id, $scope.***VAR***);
   }
}]);
