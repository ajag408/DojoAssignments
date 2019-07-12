<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
<meta charset="UTF-8">
<title>Team</title>
</head>
<body>
	<p>
        <c:out value="${team.getName()}"/>
	</p>
	<a href = "/Roster/players?id=${team.getID()}">New <c:out value="${team.getName()}"/></a>
	<br>
	<table>
  		<tr>
    		<th>First Name</th>
    		<th>Last Name</th> 
    		<th>Age</th>
    		<th>Actions</th>
  		</tr>
  	  <c:forEach var="player" items="${team.playerList}">
  	    <tr>
  	    	<td>
       			 <c:out value="${player.getFirstName()}"/>
       		</td>
       		<td>
       			 <c:out value="${player.getLastName()}"/>
       		</td>
       		<td>
       			 <c:out value="${player.getAge()}"/>
       		</td>
       		<td>
       			<a href = "/Roster/players?id=${player.getID()}&delete=true">Delete</a>
       		</td>
        </tr>
      </c:forEach>
	</table>
</body>
</html>