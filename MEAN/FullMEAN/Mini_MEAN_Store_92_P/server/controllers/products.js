var mongoose = require('mongoose');
var Product = mongoose.model('Product');
module.exports = {
    index: function(req,res){
      Product.find({}, function(err, products){
        if(err){
          console.log("index error mongo db find")
        } else {
          res.json({products: products});
        }
      })
      // res.json({placeholder:'index'});
    },
    create: function(req,res){
      var product = new Product({name: req.body.name, image: req.body.image, description: req.body.description, qty: req.body.qty});
      product.save(function(err) {
        // if there is an error console.log that something went wrong!
        if(err) {
          console.log('something went wrong with add product');
        } else { // else console.log that we did well and then redirect to the root route
          console.log('successfully added a product!');
          res.json({placeholder:'created product'});
        }
      })

    },

    getProduct: function(req,res){
      Product.find({name: req.body.product}, function(err, product){
        if(err){
          console.log("error pulling up order product")
        } else{
          console.log("success pulling up product");
          res.json({product: product});
        }
      })
    },

    update: function(req,res){
      Product.findOne({name: req.body.product}, function(err, product){
        if(err) {
          console.log('something went wrong w/ update');
        } else { // else console.log that we did well and then redirect to the root route
          product.qty = req.body.qtyUpdate;
          product.save(function(err){
            if(err){
              console.log("jeez");
            } else {
              console.log("successful update")
              res.json({placeholder:'update'});
            }
          })
        }
      })
    }
}
