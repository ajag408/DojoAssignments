// Load the express module (Where do you think this comes from?)
var express = require("express");

// invoke var express and store the resulting application in var app
var app = express();

// require body-parser
var bodyParser = require('body-parser');
// use it!
app.use(bodyParser.urlencoded({extended: true}));

app.set('views', __dirname + '/views');
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');
// two underscores before dirname
// try printing out __dirname using console.log to see what it is and why we use it
app.get("/", function (request, response){
    // hard-coded user data
    response.render('index');
})

app.post('/result', function (req, res){
  console.log("POST DATA \n\n", req.body);

  //code to add user to db goes here!
  res.render('result', {name: req.body.name, location: req.body.location, language: req.body.language, comment: req.body.comment});
})

app.listen(8000, function() {
  console.log("listening on port 8000");

})
