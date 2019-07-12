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
		if(request.getParameter("delete") != null) {
			HttpSession session = request.getSession();
			int id = Integer.parseInt(request.getParameter("id"));
			Team thisTeam = (Team) session.getAttribute("team");
			thisTeam.deletePlayer(id);
			String urlID = Integer.toString(thisTeam.getID());
			session.setAttribute("team", thisTeam);
			response.sendRedirect("/Roster/teams?id=" + urlID);
		} else {
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
		int id = thisTeam.getCurrentPlayerID();
		Player player = new Player(firstName, lastName, age, id);
		thisTeam.addPlayer(player);
		String urlID = Integer.toString(thisTeam.getID());
		session.setAttribute("team", thisTeam);
		response.sendRedirect("/Roster/teams?id=" + urlID);
	}

}
