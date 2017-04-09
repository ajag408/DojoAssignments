// Load the express module (Where do you think this comes from?)
var express = require("express");

var session = require('express-session');

// invoke var express and store the resulting application in var app
var app = express();

app.use(session({secret: 'codingdojorocks', saveUninitialized: true, resave: true}));

app.use(express.static(__dirname + "/static"));

app.set('views', __dirname + '/views');
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');
// two underscores before dirname
// try printing out __dirname using console.log to see what it is and why we use it
app.get("/", function (request, response){
    // hard-coded user data
    request.session.count = 0;
    response.render('index');
})

var server = app.listen(8000, function() {
  console.log("listening on port 8000");

})

var io = require('socket.io').listen(server);

var count = 0;

io.sockets.on('connection', function (socket) {
  socket.on("epicPressed", function (){
    count++;
    io.emit('1up', {count: count});
  })
  socket.on("resetPressed", function(){
    count = 0;
    io.emit('base', {count:count});
  })


})
