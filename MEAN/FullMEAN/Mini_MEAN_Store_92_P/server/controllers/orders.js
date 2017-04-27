var mongoose = require('mongoose');
var Order = mongoose.model('Order');
module.exports = {
    index: function(req,res){
      Order.find({}, function(err, orders){
        if(err){
          console.log("index error mongo db find")
        } else {
          res.json({orders: orders});
        }
      })
      // res.json({placeholder:'index'});
    },
    create: function(req,res){
      var order = new Order({product: req.body.product, customer: req.body.customer, qty: req.body.qty});
      order.save(function(err) {
        // if there is an error console.log that something went wrong!
        if(err) {
          console.log('something went wrong with add order');
        } else { // else console.log that we did well and then redirect to the root route
          console.log('successfully added a order!');
          res.json({placeholder:'created order'});
        }
      })

    }

}
