// Load the express module (Where do you think this comes from?)
var express = require("express");

// invoke var express and store the resulting application in var app
var app = express();

app.use(express.static(__dirname + "/static"));


app.set('views', __dirname + '/views');
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');
// two underscores before dirname
// try printing out __dirname using console.log to see what it is and why we use it
app.get("/", function (request, response){
    // hard-coded user data
    response.render('index');
})

var server = app.listen(8000, function() {
  console.log("listening on port 8000");

})

var io = require('socket.io').listen(server);
function message(name, content){
  this.name = name;
  this.content = content;
}
var message_array = [];
io.sockets.on('connection', function (socket) {

  socket.on('new_user', function (data){
      socket.emit('user_view', {name: data.name, messages: message_array});
  })
  socket.on('comment', function(data){
    message_array.push(new message(data.user, data.content));
    io.emit('comment_post', {name: data.user, content: data.content});
  })
})
