// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();

var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/messageBoard');

// define Schema variable
var Schema = mongoose.Schema;
// define Post Schema
var MessageSchema = new mongoose.Schema({
 name: {type: String, required: true, minlength: 4},
 mtext: {type: String, required: true },
 comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
}, {timestamps: true });
// define Comment Schema
var CommentSchema = new mongoose.Schema({
 _message: {type: Schema.Types.ObjectId, ref: 'Message'},
 name: {type: String, required: true, minlength: 4},
 ctext: {type: String, required: true }
}, {timestamp: true });
// set our models by passing them their respective Schemas
mongoose.model('Message', MessageSchema);
mongoose.model('Comment', CommentSchema);
// store our models in variables
var Message = mongoose.model('Message');
var Comment = mongoose.model('Comment');

mongoose.Promise = global.Promise;

var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));

var path = require('path');

app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
  Message.find({})
    .populate('comments')
    .exec(function(err, messages){
      if(err){
        console.log("index page load error")
      } else {
        res.render('index', {messages: messages});
      }
    })
})

app.post('/message', function(req, res) {
  var message = new Message({name: req.body.name, mtext: req.body.message});
  message.save(function(err) {
    // if there is an error console.log that something went wrong!
    if(err) {
      console.log('something went wrong w/ adding message');
      Message.find({})
        .populate('comments')
        .exec(function(err, messages){
          if(err){
            console.log("index page load error")
          } else {

            res.render('index', {messages: messages, errors: message.errors});
          }
        })

    } else { // else console.log that we did well and then redirect to the root route
      console.log('successfully added a message!');
      res.redirect('/');
    }
  })
})

app.post('/comment/:id', function(req,res){
  Message.findOne({_id: req.params.id}, function(err, message){
      // data from form on the front end
      var comment = new Comment({name: req.body.name, ctext: req.body.comment});
      //  set the reference like this:
      comment._message = message._id;
      // now save both to the DB
      comment.save(function(err){
        if(err){
          Message.find({})
            .populate('comments')
            .exec(function(err, messages){
              if(err){
                console.log("index page load error")
              } else {

                res.render('index', {messages: messages, errors: comment.errors});
              }
            })
        } else {
              message.comments.push(comment);
              message.save(function(err){
                   if(err) {
                        console.log('Error');
                   } else {
                        res.redirect('/');
                   }
               });
        }
       });
  });
})

app.listen(8000, function() {
    console.log("listening on port 8000");
})
