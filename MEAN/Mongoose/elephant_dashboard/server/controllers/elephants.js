var mongoose = require('mongoose');
var Elephant = mongoose.model('Elephant');
module.exports = {
  show: function(req, res) {
    Elephant.find({}, function(err, elephants){
      if(err){
        console.log("index error mongo db find")
      } else {
        res.render('index', {elephants: elephants});
      }
    })
  },

  view_one: function(req, res) {
    Elephant.find({_id: req.params.id}, function(err, elephant){
        if(err){
          console.log("couldn't pull up elephant")
        } else {
          res.render('view_one', {elephant: elephant});
        }
    })
  },

  make_one_form: function(req, res) {
    console.log("hello")
    res.render('make_one');
  },

  make_one: function(req, res) {
    var elephant = new Elephant({name: req.body.name, age: Number(req.body.age)});
    elephant.save(function(err) {
    // if there is an error console.log that something went wrong!
      if(err) {
        console.log('something went wrong with add');
      } else { // else console.log that we did well and then redirect to the root route
        console.log('successfully added an ele!');
        res.redirect('/');
      }
    })
  },

  edit_view: function(req, res) {
    Elephant.find({_id: req.params.id}, function(err, elephant){
        if(err){
          console.log("couldn't pull up elephant for edit")
        } else {
          res.render('edit', {elephant: elephant});
        }
    })
  },

  update: function(req, res) {
    Elephant.findOne({_id: req.params.id}, function(err, elephant){
        if(err) {
          console.log('something went wrong w/ update');
        } else { // else console.log that we did well and then redirect to the root route
          elephant.name = req.body.name;
          elephant.age = req.body.age;
          elephant.save(function(err){
            if(err){
              console.log("jeez");
            } else {
              res.redirect('/');
            }
          })
        }
    })
  },

  delete: function(req, res) {
    Elephant.remove({_id: req.params.id}, function(err, elephant){
        if(err){
          console.log("couldn't delete elephant")
        } else {
          res.redirect('/');
        }
    })
  }
}
