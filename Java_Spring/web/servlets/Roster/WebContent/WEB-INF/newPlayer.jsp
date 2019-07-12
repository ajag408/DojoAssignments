<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title><c:out value="${team.getName()}"/>: New Player</title>
</head>
<body>
	<p>Add a player to team <c:out value="${team.getName()}"/></p>
	<i><c:out value="${error1}"/></i>
	<i><c:out value="${error2}"/></i>
	<i><c:out value="${error3}"/></i>
	<form action="/Roster/players" method="POST">
    	First Name: <input type="text" name="firstName">
    	Last Name: <input type="text" name="lastName">
    	Age: <input type="text" name="age">
    	<button>Add</button>
	 </form>
</body>
</html>