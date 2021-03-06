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
		HttpSession session = request.getSession();
		if(low != null && high != null) {
			String range = "set";
			session.setAttribute("range", range);
			session.setAttribute("low", low);
			session.setAttribute("high", high);
			session.setAttribute("tries", 5);
			session.setAttribute("playing", "yes");
			Random r = new Random();
			int min = Integer.parseInt(low);
			int max = Integer.parseInt(high);
			int number = r.nextInt((max-min)+1)+min;
			System.out.println(number);
			session.setAttribute("number", number);
		} else {
			session.setAttribute("range", null);
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
		int tries = (int) session.getAttribute("tries");
		String message = null;
		if(guess == number) {
			message = "Correct";
			session.setAttribute("playing", "no");
		} else if(tries<=1) {
			message = "You have lost";
			session.setAttribute("playing", "no");
//			request.setAttribute("number", number);
		} else if(guess<number) {
			tries = tries-1;
//			sessoin.setAttribute("tries", tries)
			message = "Too low";
		} else if (guess>number) {
			tries = tries-1;
			message = "Too high";
		}

		request.setAttribute("message", message);
		session.setAttribute("tries", tries);
        RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/Interface.jsp");
        view.forward(request, response);
		
	}

}
