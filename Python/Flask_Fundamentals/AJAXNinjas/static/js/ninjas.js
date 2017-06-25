$(document).ready(function(){
  $('button').click(function(){
    if($(this).text() == 'red'){
      $.get('http://localhost:5000/red', function(res){
        $('#picture').html('<h1>' + res.text + '</h1>')
        $('#picture').append('<img src="/static/'+res.img+'">')
      }, 'json')
    } else if($(this).text() == 'blue'){
      $.get('http://localhost:5000/blue', function(res){
        $('#picture').html('<h1>' + res.text + '</h1>')
        $('#picture').append('<img src="/static/'+res.img+'">')
      }, 'json')
    } else if($(this).text() == 'orange'){
      $.get('http://localhost:5000/orange', function(res){
        $('#picture').html('<h1>' + res.text + '</h1>')
        $('#picture').append('<img src="/static/'+res.img+'">')
      }, 'json')
    } else if($(this).text() == 'purple'){
      $.get('http://localhost:5000/purple', function(res){
        $('#picture').html('<h1>' + res.text + '</h1>')
        $('#picture').append('<img src="/static/'+res.img+'">')
      }, 'json')
    }
  });
});
