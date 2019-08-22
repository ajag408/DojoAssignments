<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
         <%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>  
 <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>New Ninja</title>
</head>
<body>
<h1>New Ninja</h1>
<form:form action="/ninja" method="post" modelAttribute="ninja">
    <p>
        <form:label path="dojo">Person:</form:label>
        
        <form:select path="dojo">
        	<c:forEach var="dojo" items="${dojos}">
    			<form:option value="${dojo}" label = "${dojo.name}"/>
			</c:forEach>
        </form:select>
    </p>
    <p>
        <form:label path="state">State:</form:label>
        <form:errors path="state"/>
        <form:input path="state"/>
    </p>
	<p>
        <form:label path="expirationDate">Expiration Date:</form:label>
        <form:input type = "date" path="expirationDate"/>
    </p>
    <input type="submit" value="Create"/>
</form:form> 
</body>
</html>