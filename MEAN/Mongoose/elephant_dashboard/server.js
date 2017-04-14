// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();


 // We are setting this Schema in our Models as 'User'
var Elephant = mongoose.model('Elephant')

mongoose.Promise = global.Promise;

var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));

var path = require('path');

app.set('views', path.join(__dirname, './client/views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');

require('./server/config/mongoose.js');
// Routes
// Root Request
var routes_setter = require('./server/config/routes.js');

routes_setter(app);

// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
