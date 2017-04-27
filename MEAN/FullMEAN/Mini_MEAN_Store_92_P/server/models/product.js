var mongoose = require('mongoose');

var ProductSchema = new mongoose.Schema({
 name: {type: String, required: true},
 image: {data: Buffer, contentType: String},
 description: {type: String},
 qty: {type: Number, required: true},
}, {timestamps: true });

mongoose.model('Product', ProductSchema);
