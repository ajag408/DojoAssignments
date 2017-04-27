var app = angular.module('app', ['ngRoute']);
app.config(function ($routeProvider) {
  $routeProvider
    .when('/index',{
      templateUrl:'partials/index.html',
      controller:'indexController'
    })
    .when('/new',{
      templateUrl: 'partials/new.html',
      controller: 'newController'
    })
    .when('/edit/:id',{
      templateUrl: 'partials/edit.html',
      controller: 'editController'
    })
    .when('/show/:id',{
      templateUrl: 'partials/show.html',
      controller: 'editController'
    })
    .otherwise({
      redirectTo: '/index'
    });
});
