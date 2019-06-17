<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="style.css">
<meta charset="UTF-8">
<title>Checkerboard</title>
</head>
<body>
    <% String width = request.getParameter("width"); %>
    <% String height = request.getParameter("height"); %>
    <% if(width == null){ %>
    	<% width = "0"; %>
    <%} %>
    <% if(height == null){ %>
    	<% height = "0"; %>
    <%} %>
    <h1>Checkerboard: <%= width %>w X <%= height %>h</h1>
    
    <div class = 'board'>
    	<div class = 'col'></div>
    	    	<div class = 'col'></div>
    	    	    	<div class = 'col'></div>
    	    	    	    	<div class = 'col'></div>
    	    	    	    	    	<div class = 'col'></div>
    	    	    	    	    	    	<div class = 'col'></div>
    	    	    	    	    	    	    	<div class = 'col'></div>
    	    	    	    	    	    	    	    	<div class = 'col'></div>
    	    	    	    	    	    	    	    	    	<div class = 'col'></div>
    	    	    	    	    	    	    	    	    	    	<div class = 'col'></div>
    </div>
</body>
</html>