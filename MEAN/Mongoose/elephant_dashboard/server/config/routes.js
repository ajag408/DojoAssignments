var elephants = require('../controllers/elephants.js');
module.exports = function(app){
  app.get('/', function(req, res) {
    elephants.show(req,res)
  })

  app.get('/elephant/:id', function(req, res) {
    elephants.view_one(req,res)
  })

  app.get('/elephants/new', function(req, res) {
    elephants.make_one_form(req,res)
  })

  app.post('/elephants', function(req, res) {
    elephants.make_one(req,res)
  })

  app.get('/elephant/edit/:id', function(req, res) {
    elephants.edit_view(req,res);
  })

  app.post('/elephant/:id', function(req, res) {
    elephants.update(req,res)
  })

  app.get('/elephant/destroy/:id', function(req, res) {
    elephants.delete(req,res)
  })
}
