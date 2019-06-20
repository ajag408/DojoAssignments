<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Clicker</title>
</head>
<body>
	<form action = "/ButtonClicker/Counter" method="POST">
		<button>Click Me!</button>
	</form>
	
	<p>
        You have clicked this button <c:out value="${counter}"/> times
    </p>
</body>
</html>