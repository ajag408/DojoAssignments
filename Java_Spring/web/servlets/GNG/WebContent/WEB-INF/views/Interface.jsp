<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Great Number Game</title>
</head>
<body>
	<h1>Welcome to the Great Number Game!</h1>

    <c:choose>
     <c:when test="${range == null }">
     	<p>Please select a range by entering a low and a high in the url in the format "?low=yourPick&high=yourPick"</p> 
     </c:when>
     <c:otherwise>
  		<p>I am thinking of a number between <c:out value="${low}"/>  and <c:out value="${high}"/> </p>
		<p>Take a guess!</p>
		<c:out value="${message}"/>   
		<c:choose>
        	<c:when test="${playing == 'no'}">
     			<h2><c:out value="${number}"/> was the number!</h2>
				<form action="/GNG/Numbers" method="GET">
    	 		<button>Play again!</button>
				</form>
	 		</c:when>
	 		<c:otherwise>
	 			<p><b><i>You have <c:out value="${tries}"/> guesses left!</i></b></p>
	    		<form action="/GNG/Numbers" method="POST">
    	  		<input type="text" name="number">
    	  		<button>Submit</button>
	    		</form>
	  		</c:otherwise>
	  	</c:choose>
	  </c:otherwise>
	</c:choose>
</body>
</html>