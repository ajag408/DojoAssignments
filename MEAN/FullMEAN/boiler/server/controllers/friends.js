var mongoose = require('mongoose');
var Friend = mongoose.model('Friend');
module.exports = {
    index: function(req,res){
      Friend.find({}, function(err, friends){
        if(err){
          console.log("index error mongo db find")
        } else {
          res.json({friends: friends});
        }
      })
      // res.json({placeholder:'index'});
    },
    create: function(req,res){
      var friend = new Friend({first_name: req.body.first_name, last_name: req.body.last_name, birthday: req.body.birthday});
      friend.save(function(err) {
        // if there is an error console.log that something went wrong!
        if(err) {
          console.log('something went wrong with add');
        } else { // else console.log that we did well and then redirect to the root route
          console.log('successfully added a friend!');
          res.json({placeholder:'create'});
        }
      })

    },
    update: function(req,res){
      Friend.findOne({_id: req.params.id}, function(err, friend){
        if(err) {
          console.log('something went wrong w/ update');
        } else { // else console.log that we did well and then redirect to the root route
          friend.first_name = req.body.first_name;
          friend.last_name = req.body.last_name;
          friend.birthday = req.body.birthday;
          friend.save(function(err){
            if(err){
              console.log("jeez");
            } else {
              console.log("successful update")
              res.json({placeholder:'update'});
            }
          })
        }
      })
      // res.json({placeholder:'update'});
    },
    delete: function(req,res){
      Friend.remove({_id: req.params.id}, function(err, friend){
        if(err){
          console.log("couldn't delete friend")
        } else {
          res.json({placeholder:'delete'});
        }
      })
      // res.json({placeholder:'delete'});
    },
    show: function(req,res){
      Friend.find({_id: req.params.id}, function(err, friend){
        if(err){
          console.log("couldn't pull up friend")
        } else {
          res.json({friend: friend});
        }
      })
      // res.json({placeholder:'show'});
    }
}
