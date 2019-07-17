<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Current visit count</title>
</head>
<body>
<p>You have visited <a href = "/">localhost:8080</a> <c:out value="${count}"/> times</p>
<a href = "/">Test another visit?</a><br>
<form action = "/reset">
	<button type = "submit">Reset counter</button>
</form>
</body>
</html>