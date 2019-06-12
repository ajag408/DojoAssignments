package com.codingdojo.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class Home
 */
@WebServlet("/Home")
public class Home extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Home() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // get the value for the query parameter
        String firstName = request.getParameter("firstName");
        if(firstName == null) {
        	firstName = "Unknown";
        }
        String lastName = request.getParameter("lastName");
        if(lastName == null) {
        	lastName = "Unknown";
        }
        String language = request.getParameter("favoriteLanguage");
        if(language == null) {
        	language = "Unknown";
        }
        String home = request.getParameter("hometown");
        if(home == null) {
        	home = "Unknown";
        }
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.write("<h1>Welcome " + firstName + " " + lastName + "</h1>");
        out.write("<h3>Your favorite language is: " + language + "</h3>");
        out.write("<h3>Your hometown is: " + home + "</h3>");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
