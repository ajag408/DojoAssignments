var friends = require('../controllers/friends.js');
module.exports = function(app){
  app.get('/friends', function(req, res) {
    friends.index(req,res);
  });
  app.get('/friends/:id', function(req, res){
    friends.show(req,res);
  });
  app.post('/friends', function(req, res){
    friends.create(req,res);
  });
  app.post('/friends/:id', function(req,res){
    console.log("in the routes");
    console.log(req.body);
    friends.update(req,res);
  });
  app.delete('/friends/:id', function(req,res){
    friends.delete(req,res);
  });
}
