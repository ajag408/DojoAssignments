<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Ninja Gold Game</title>
</head>
<body>
<h3>Your Gold: <c:out value="${gold}"/></h3>
<form action = "/"><button>Reset</button></form>

<h3>Farm (earns 10-20 gold)</h3>
<form method = "POST" action = "/find">
	<button name = "place" value = "farm">Find Gold!</button>
</form>
<h3>Cave (earns 5-10 gold)</h3>
<form method = "POST" action = "/find">
	<button name = "place" value = "cave">Find Gold!</button>
</form>
<h3>House (earns 2-5 gold)</h3>
<form method = "POST" action = "/find">
	<button name = "place" value = "house">Find Gold!</button>
</form>
<h3>Casino! (earns/takes 0-50 gold)</h3>
<form method = "POST" action = "/find">
	<button name = "place" value = "casino">Find Gold!</button>
</form>
<h3>Spa (takes 5-20 gold)</h3>
<form method = "POST" action = "/find">
	<button name = "place" value = "spa">Treat yourself!</button>
</form>

<h3>Activities</h3>

	<textarea rows="10" cols="50">
		<c:forEach var="action" items="${actions}">
    		<c:out value="${action}"/>
		</c:forEach>
	</textarea>
</body>
</html>