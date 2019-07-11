package com.codingdojo.web.controllers;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.codingdojo.web.models.Roster;
import com.codingdojo.web.models.Team;

/**
 * Servlet implementation class NewTeam
 */
@WebServlet("/teams")
public class NewTeam extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public NewTeam() {
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
		if(request.getParameter("id") != null) {
			int id = Integer.parseInt(request.getParameter("id"));
			if(request.getParameter("delete") != null) {
				Roster roster = (Roster) session.getAttribute("roster");
				roster.deleteTeam(id);
				session.setAttribute("roster", roster);
				response.sendRedirect("/Roster/Home");
			} else {
				System.out.println("team view");
			}
		} else {
	        RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/newTeam.jsp");
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
		String teamName = request.getParameter("teamName");
		int id = (int) session.getAttribute("teamID");
		Team team = new Team(teamName, id);
		Roster roster = (Roster) session.getAttribute("roster");
		roster.addTeam(team);
		id = id + 1;
		session.setAttribute("roster", roster);
		session.setAttribute("teamID", id);
		response.sendRedirect("/Roster/Home");
	}

}
