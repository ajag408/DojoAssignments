<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Dojo Survey Index</title>
</head>
<body>
	<form method = "POST" action = "/result">
		<label>Your Name: <input type="text" name="name"></label><br>
    	<label>Dojo Location: <select name="location">
  			<option value="San Jose">San Jose</option>
  			<option value="Burbank">Burbank</option>
  			<option value="Seattle">Seattle</option>
  			<option value="Vaikuntha">Vaikuntha</option>
							</select></label><br>
    	<label>Favorite Language: <select name="language">
  			<option value="Python">Python</option>
  			<option value="C++">C++</option>
  			<option value="Sanskrit">Sanskrit</option>
  			<option value="Java">Java</option>
							</select></label>
		<label>Comment (optional):<br>
		 <textarea name = "comments" rows="4" cols="50"></textarea></label>
    	<button>Submit</button>
	</form>
</body>
</html>