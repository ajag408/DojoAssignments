package com.codingdojo.web.controllers;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.codingdojo.web.models.Player;
import com.codingdojo.web.models.Roster;
import com.codingdojo.web.models.Team;

/**
 * Servlet implementation class NewPlayer
 */
@WebServlet("/players")
public class NewPlayer extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public NewPlayer() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		response.getWriter().append("Served at: ").append(request.getContextPath());
		HttpSession session = request.getSession();
		if(request.getParameter("delete") != null) {

			int id = Integer.parseInt(request.getParameter("id"));
			Team thisTeam = (Team) session.getAttribute("team");
			thisTeam.deletePlayer(id);
			String urlID = Integer.toString(thisTeam.getID());
			session.setAttribute("team", thisTeam);
			response.sendRedirect("/Roster/teams?id=" + urlID);
		} else {
			session.setAttribute("error1", null);
			session.setAttribute("error2", null);
			session.setAttribute("error3", null);
			RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/newPlayer.jsp");
			view.forward(request, response);
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		doGet(request, response);
		HttpSession session = request.getSession();
		Team thisTeam = (Team) session.getAttribute("team");
		String firstName = request.getParameter("firstName");
		String lastName = request.getParameter("lastName");
		int age = Integer.parseInt(request.getParameter("age"));
		if(firstName.length()<=2 || lastName.length()<=2 || age<18) {
			if(firstName.length() <= 2) {
				session.setAttribute("error1", "Please enter a first name with more than two chars");
			}
			if(lastName.length()<=2) {
				session.setAttribute("error2", "Please enter a last name with more than two chars");
			}			
			if(age<18) {
				session.setAttribute("error3", "Player has to be 18 or older");
			}
	        RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/newPlayer.jsp");
	        view.forward(request, response);
		} else {

		int id = thisTeam.getCurrentPlayerID();
		Player player = new Player(firstName, lastName, age, id);
		thisTeam.addPlayer(player);
		String urlID = Integer.toString(thisTeam.getID());
		session.setAttribute("team", thisTeam);
		response.sendRedirect("/Roster/teams?id=" + urlID);
		}
	}

}
