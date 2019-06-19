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
    <%
    String color = "red";
    int w = Integer.parseInt(width);
    int h = Integer.parseInt(height);
    %> 
    <%for(int x = 0; x<w; x++){ %>
    	<% if(x%2 == 1){%>
    		<% color = "blue"; %>
    	<% }else{ %>
    		<% color = "red";} %>
    	<div class = 'col'>
    	<%for(int y = 0; y<h; y++){%>
    		<% if(color == "red"){ %>
    			<div class = 'red-block'></div>
    			<%color = "blue"; %>
    		<%}else{ %>
    			<div class = 'blue-block'></div>
    			<%color = "red"; } }%>
    	</div>	
    <%}%>
    </div>
</body>
</html>