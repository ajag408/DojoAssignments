<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
     <%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>  
  <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Search</title>
</head>
<body>
<a href = "/dashboard">Dashboard</a><br><br>

<p>Songs by artist: <c:out value="${song.title}"/></p><br>

<form:form action="/search" method="post" modelAttribute="song">
    <p>
       <form:input path="artist"/>
    	<input type="submit" value="Search Artists"/>
    </p>
</form:form> <br>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>rating</th>
            <th>action</th>
        </tr>
    </thead>
    <tbody>
        <c:forEach items="${songs}" var="song">
        <tr>
            <td><a href = "/songs/${song.id}"><c:out value="${song.title}"/></a></td>
            <td><c:out value="${song.rating}"/></td>
            <td><a href = "/songs/delete/${song.id}">delete</a></td>
        </tr>
        </c:forEach>
    </tbody>
</table>


</body>
</html>