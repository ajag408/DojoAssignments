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
  			<option value="sj">San Jose</option>
  			<option value="ba">Burbank</option>
  			<option value="se">Seattle</option>
  			<option value="vk">Vaikuntha</option>
							</select></label><br>
    	<label>Favorite Language: <select name="language">
  			<option value="py">Python</option>
  			<option value="c+">C++</option>
  			<option value="sk">Sanskrit</option>
  			<option value="jv">Java</option>
							</select></label>
		<label>Comment (optional):<br>
		 <textarea rows="4" cols="50"></textarea></label>
    	<button>Submit</button>
	</form>
</body>
</html>