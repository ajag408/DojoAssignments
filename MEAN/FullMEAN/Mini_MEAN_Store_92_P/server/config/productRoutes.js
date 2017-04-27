var products = require('../controllers/products.js');
module.exports = function(app){
  app.get('/products', function(req, res) {
    products.index(req,res);
  });
  app.post('/products', function(req, res){
    products.create(req,res);
  });
  app.post('/product', function(req,res){
    console.log(req.body.product);
    products.getProduct(req,res);
  });
  app.post('/update', function(req,res){
    products.update(req,res);
  })
}
