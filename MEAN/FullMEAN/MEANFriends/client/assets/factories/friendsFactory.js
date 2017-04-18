
console.log('Friends Factory');
app.factory('friendsFactory', ['$http', function($http) {
  var factory = {};
  factory.index = function(callback) {
      //call this method if you want to update or set the friends variable
      $http.get('/friends').then(function(returned_data){
        console.log(returned_data.data.friends);
        callback(returned_data.data.friends);
      });
  }
  factory.show = function(id, callback) {
    $http.get('/friends/'+id).then(function(returned_data){
      var birthdate = new Date(returned_data.data.friend[0].birthday);
      var createdAt = new Date(returned_data.data.friend[0].createdAt)
      returned_data.data.friend[0].birthday = birthdate
      returned_data.data.friend[0].createdAt= createdAt
      callback(returned_data.data.friend[0]);
    });
  }
  factory.create = function(newfriend, callback) {
      $http.post('/friends', newfriend).then(function(returned_data){
        console.log(returned_data.data);
        if (typeof(callback) == 'function'){
          callback(returned_data.data);
        }
      });
  }
  factory.update = function(id, friend) {
    console.log("factory.update");
    console.log(friend);
    $http.post('/friends/' + id, friend).then(function(returned_data) {
        console.log(returned_data.data);
    })
  }
  factory.delete = function(id) {
      $http.delete('/friends/'+id).then(function(returned_data){
        console.log(returned_data.data);
      })
  }
  return factory;
}]);
