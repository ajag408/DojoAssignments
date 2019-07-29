<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>  
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>${language.name}</title>
</head>
<body>
<a href = "/languages">Dashboard</a><br>

<p>${language.name}</p><br>
<p>${language.creator}</p><br>
<p>${language.version}</p><br>

<a href = "/languages/edit/${language.id}">Edit</a><br>
<a href = "/languages/delete/${language.id}">Delete</a>
</body>
</html>