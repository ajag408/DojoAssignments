var mongoose = require('mongoose');

var OrderSchema = new mongoose.Schema({
 product: {type: String, required: true},
 customer: {type: String, required: true},
 qty: {type: Number, required: true},
}, {timestamp: true });

mongoose.model('Order', OrderSchema);
