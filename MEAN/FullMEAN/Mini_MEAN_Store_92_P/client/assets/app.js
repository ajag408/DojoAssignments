var app = angular.module('app', ['ngRoute']);
app.config(function ($routeProvider) {
  $routeProvider
    .when('/index',{
      templateUrl:'partials/index.html',
      controller:'indexController'
    })
    .when('/products',{
      templateUrl: 'partials/products.html',
      controller: 'productController'
    })
    .when('/orders',{
      templateUrl: 'partials/orders.html',
      controller: 'orderController'
    })
    .when('/customers',{
      templateUrl: 'partials/customers.html',
      controller: 'customerController'
    })
    .otherwise({
      redirectTo: '/index'
    });
});
