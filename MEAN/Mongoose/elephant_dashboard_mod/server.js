// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();

var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/elephant_dashboard');

var ElephantSchema = new mongoose.Schema({
 name: {type: String, required: true},
 age: {type: Number, required: true}
}, {timestamps: true})
mongoose.model('Elephant', ElephantSchema); // We are setting this Schema in our Models as 'User'
var Elephant = mongoose.model('Elephant')

mongoose.Promise = global.Promise;

var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));

var path = require('path');

app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
// Routes
// Root Request
app.get('/', function(req, res) {
  Elephant.find({}, function(err, elephants){
    if(err){
      console.log("index error mongo db find")
    } else {
      res.render('index', {elephants: elephants});
    }
  })
})

app.get('/elephant/:id', function(req, res) {
  Elephant.find({_id: req.params.id}, function(err, elephant){
      if(err){
        console.log("couldn't pull up elephant")
      } else {
        res.render('view_one', {elephant: elephant});
      }
  })
})

app.get('/elephants/new', function(req, res) {
  console.log("hello")
  res.render('make_one');
})

app.post('/elephants', function(req, res) {
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
})

app.get('/elephant/edit/:id', function(req, res) {
  Elephant.find({_id: req.params.id}, function(err, elephant){
      if(err){
        console.log("couldn't pull up elephant for edit")
      } else {
        res.render('edit', {elephant: elephant});
      }
  })
})

app.post('/elephant/:id', function(req, res) {
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
})

app.get('/elephant/destroy/:id', function(req, res) {
  Elephant.remove({_id: req.params.id}, function(err, elephant){
      if(err){
        console.log("couldn't delete elephant")
      } else {
        res.redirect('/');
      }
  })
})
//
// app.get('/quotes', function(req, res) {
// })
//
// app.post('/like', function(req,res){
// })
// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
