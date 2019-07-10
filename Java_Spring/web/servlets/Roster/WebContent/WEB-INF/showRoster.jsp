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
<title>Roster</title>
</head>
<body>
	<p>Prototype Roster</p>
	<a href = '/Roster/teams'>New Team</a>
	
	<br>
	<br>
	<br>
	
	<table>
  		<tr>
    		<th>Team</th>
    		<th>Players</th> 
    		<th>Action</th>
  		</tr>
  	  <c:forEach var="team" items="${roster.teamList}">
  	    <tr>
  	    	<td>
       			 <c:out value="${team.getName()}"/>
       		</td>
       		<td>
       			 <c:out value="${team.getPlayerCount()}"/>
       		</td>
       		<td>
       			<a>Details</a> <a>Delete</a>
       		</td>
        </tr>
      </c:forEach>
	</table>
</body>
</html>