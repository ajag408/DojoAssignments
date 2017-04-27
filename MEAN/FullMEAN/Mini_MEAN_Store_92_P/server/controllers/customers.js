var mongoose = require('mongoose');
var Customer = mongoose.model('Customer');
module.exports = {
    index: function(req,res){
      Customer.find({}, function(err, customers){
        if(err){
          console.log("index error mongo db find")
        } else {
          res.json({customers: customers});
        }
      })
      // res.json({placeholder:'index'});
    },
    create: function(req,res){
      var customer = new Customer({name: req.body.name});
      customer.save(function(err) {
        // if there is an error console.log that something went wrong!
        if(err) {
          console.log('something went wrong with add');
        } else { // else console.log that we did well and then redirect to the root route
          console.log('successfully added a friend!');
          res.json({placeholder:'create'});
        }
      })

    },
    delete: function(req,res){
      Customer.remove({_id: req.params.id}, function(err, customer){
        if(err){
          console.log("couldn't delete friend")
        } else {
          res.json({placeholder:'delete'});
        }
      })
      // res.json({placeholder:'delete'});
    }
}
