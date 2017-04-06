// get the http module:
var http = require('http');
// fs module allows us to read and write content for responses!!
var fs = require('fs');
// creating a server using http module:
var server = http.createServer(function (request, response){
    // see what URL the clients are requesting:
    console.log('client request URL: ', request.url);
    // this is how we do routing:
    if(request.url === '/cars') {
        fs.readFile('./views/cars.html', 'utf8', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(contents);
            response.end();
        });
    }
    else if (request.url === "/cats") {
         fs.readFile('./views/cats.html', 'utf8', function (errors, contents){
             response.writeHead(200, {'Content-type': 'text/html'});
             response.write(contents);
             response.end();
         });
    }
    else if (request.url === '/cars/new'){
      fs.readFile('./views/create_car.html', 'utf8', function (errors, contents){
          response.writeHead(200, {'Content-type': 'text/html'});
          response.write(contents);
          response.end();
      });
    }

    else if (request.url === "/stylesheets/cars.css") {
      fs.readFile('./stylesheets/cars.css', function(errors, contents){
        response.writeHead(200, {'Content-type': 'text/css'});
        response.write(contents);
        response.end();
      });
    }

    else if (request.url === "/stylesheets/cats.css") {
      fs.readFile('./stylesheets/cats.css', function(errors, contents){
        response.writeHead(200, {'Content-type': 'text/css'});
        response.write(contents);
        response.end();
      });
    }

    else if(request.url === '/images/bugatti.jpg'){
      // notice we won't include the utf8 encoding
      fs.readFile('./images/bugatti.jpg', function(errors, contents){
          response.writeHead(200, {'Content-type': 'image/jpg'});
          response.write(contents);
          response.end();
        });
    }
    else if(request.url === '/images/mazda.jpg'){
      // notice we won't include the utf8 encoding
      fs.readFile('./images/mazda.jpg', function(errors, contents){
          response.writeHead(200, {'Content-type': 'image/jpg'});
          response.write(contents);
          response.end();
        });
    }
    else if(request.url === '/images/mercedes.jpg'){
      // notice we won't include the utf8 encoding
      fs.readFile('./images/mercedes.jpg', function(errors, contents){
          response.writeHead(200, {'Content-type': 'image/jpg'});
          response.write(contents);
          response.end();
        });
    }
    else if(request.url === '/images/lion.jpg'){
      // notice we won't include the utf8 encoding
      fs.readFile('./images/lion.jpg', function(errors, contents){
          response.writeHead(200, {'Content-type': 'image/jpg'});
          response.write(contents);
          response.end();
        });
    }
    else if(request.url === '/images/ragdoll.jpg'){
      // notice we won't include the utf8 encoding
      fs.readFile('./images/ragdoll.jpg', function(errors, contents){
          response.writeHead(200, {'Content-type': 'image/jpg'});
          response.write(contents);
          response.end();
        });
    }
    else if(request.url === '/images/tiger.jpg'){
      // notice we won't include the utf8 encoding
      fs.readFile('./images/tiger.jpg', function(errors, contents){
          response.writeHead(200, {'Content-type': 'image/jpg'});
          response.write(contents);
          response.end();
        });
    }
    // request didn't match anything:
    else {
        response.end('File not found!!!');
    }
});
// tell your server which port to run on
server.listen(7077);
// print to terminal window
console.log("Running in localhost at port 7077");
