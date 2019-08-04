<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
             <%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>  
 <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Profile Page</title>
</head>
<body>
<h1>${person.firstName} ${person.lastName}</h1><br>

<p>License Number: ${person.license.number}</p>
<p>State: ${person.license.state}</p>
<p>Expiration Date: ${person.license.expirationDate}</p>
</body>
</html>