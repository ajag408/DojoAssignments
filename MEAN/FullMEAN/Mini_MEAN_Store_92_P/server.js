var express  = require( 'express' )
    bp       = require('body-parser'),
    path     = require( 'path' ),
    root     = __dirname,
    port     = process.env.PORT || 8000,
    app      = express();


app.use( express.static( path.join( root, 'client' )));
app.use( express.static( path.join( root, 'bower_components' )));
app.use(bp.json())

require('./server/config/mongoose.js');


var routes_product = require('./server/config/productRoutes.js');
var routes_customer = require('./server/config/customerRoutes.js');
var routes_order = require('./server/config/orderRoutes.js')
routes_product(app);
routes_customer(app);
routes_order(app);

app.listen( port, function() {
  console.log( `server running on port ${ port }` );
});
