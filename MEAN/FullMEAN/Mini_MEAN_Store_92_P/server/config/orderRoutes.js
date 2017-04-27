var orders = require('../controllers/orders.js');
module.exports = function(app){
  app.get('/orders', function(req, res) {
    orders.index(req,res);
  });
  app.post('/orders', function(req, res){
    orders.create(req,res);
  });
}
