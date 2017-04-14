// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();

var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/quotingDojo');

var QuoteSchema = new mongoose.Schema({
 name: {type: String, required: true},
 quote: {type: String, required: true},
 likes: {type: Number, required: true}
}, {timestamps: true})
mongoose.model('Quote', QuoteSchema); // We are setting this Schema in our Models as 'User'
var Quote = mongoose.model('Quote')

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
  res.render('index');
})
// Add User Request
app.post('/quotes', function(req, res) {
  var quote = new Quote({name: req.body.name, quote: req.body.quote, likes: 0});
  quote.save(function(err) {
    // if there is an error console.log that something went wrong!
    if(err) {
      console.log('something went wrong');
      res.render('index', {error: quote.errors})
    } else { // else console.log that we did well and then redirect to the root route
      console.log('successfully added a quote!');
      res.redirect('/quotes');
    }
  })
})

app.get('/quotes', function(req, res) {
  Quote.aggregate([{$sort: {likes: -1}}], function(err, quotes) {
    if(err) {
      console.log("cant find me lucky charms");
    } else {

      res.render('quotes', {quotes: quotes});
    }
  })
})

app.post('/like', function(req,res){
  Quote.findOne({_id: req.body.quote_id}, function(err, quote){
      if(err) {
        console.log('something went wrong w/ update');
      } else { // else console.log that we did well and then redirect to the root route
        quote.likes = quote.likes + 1;
        quote.save(function(err){
          if(err){
            console.log("jeez");
          } else {
            res.redirect('/quotes');
          }
        })
      }
  })
})
// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
