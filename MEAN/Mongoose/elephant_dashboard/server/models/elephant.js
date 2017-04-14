var mongoose = require('mongoose');

var ElephantSchema = new mongoose.Schema({
 name: {type: String, required: true},
 age: {type: Number, required: true}
}, {timestamps: true})
mongoose.model('Elephant', ElephantSchema);
