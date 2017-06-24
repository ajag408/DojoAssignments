$(document).ready(function(){
  $('#red').click(function(){
    $.get('http://localhost:5000/red', function(res){
      console.log(res.img);
    }, 'json')
  });
  $('#blue').click(function(){

  });
  $('#orange').click(function(){

  });
  $('#purple').click(function(){

  });
});
