<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 <%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>  
  <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Lookify!</title>
</head>
<body>
<a href = "/songs/new">Add New</a><br>
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