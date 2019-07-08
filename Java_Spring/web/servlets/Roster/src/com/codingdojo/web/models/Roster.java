package com.codingdojo.web.models;
import java.util.ArrayList;

public class Roster {
	ArrayList<Team> teamList = new ArrayList<Team>();
	
	public Roster() {
	}
	
	public void addTeam(Team team) {
		teamList.add(team);
	}
	
	public void deleteTeam(int id) {
		teamList.remove(id);
	}
}
