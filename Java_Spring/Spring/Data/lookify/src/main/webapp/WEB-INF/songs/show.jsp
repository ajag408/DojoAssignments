<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
     <%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>  
 <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Details</title>
</head>
<body>
<a href = "/dashboard">Dashboard</a><br>

<p><b>Title:</b> ${song.title}</p><br>
<p><b>Artist:</b>          ${song.artist}</p><br>
<p><b>Rating (1-10):</b>   ${song.rating}</p><br>

<a href = "/songs/delete/${song.id}">delete</a>
</body>
</html>