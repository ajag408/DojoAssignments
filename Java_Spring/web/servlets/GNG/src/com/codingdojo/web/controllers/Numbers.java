package com.codingdojo.web.controllers;

import java.io.IOException;
import java.util.Random;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class Numbers
 */
@WebServlet("/Numbers")
public class Numbers extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Numbers() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		response.getWriter().append("Served at: ").append(request.getContextPath());
		String low = request.getParameter("low");
		String high = request.getParameter("high");
		if(low != null && high != null) {
			HttpSession session = request.getSession();
			String range = "set";
			session.setAttribute("range", range);
			session.setAttribute("low", low);
			session.setAttribute("high", high);
			request.setAttribute("range", range);
			request.setAttribute("low", low);
			request.setAttribute("high", high);
			Random r = new Random();
			int min = Integer.parseInt(low);
			int max = Integer.parseInt(high);
			int number = r.nextInt((max-min)+1)+min;
			System.out.println(number);
			session.setAttribute("number", number);
		}
        RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/Interface.jsp");
        view.forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		doGet(request, response);
		HttpSession session = request.getSession();
		int guess = Integer.parseInt(request.getParameter("number"));
//		System.out.println("the guess is: " + guess);
		int number = (int) session.getAttribute("number");
		String message = null;
		if(guess<number) {
			message = "Too low";
		} else if (guess>number) {
			message = "Too high";
		} else if(guess == number) {
			message = "Correct";
			request.setAttribute("number", number);
		}
//		System.out.println(message);
		request.setAttribute("message", message);
		request.setAttribute("low", session.getAttribute("low"));
		request.setAttribute("high", session.getAttribute("high"));
        RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/Interface.jsp");
        view.forward(request, response);
		
	}

}
