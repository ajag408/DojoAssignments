package com.codingdojo.web.models;
import java.util.ArrayList;

public class Roster {
	private ArrayList<Team> teamList = new ArrayList<Team>();
	
	public Roster() {
	}
	
	public Team findTeam(int id) {
		for(int i = 0; i<teamList.size(); i++) {
			Team team = teamList.get(i);
			if(team.getID() == id) {
				return team;
			}
		}
		return null;
	}
	
	
	public void addTeam(Team team) {
		teamList.add(team);
	}
	
	public void deleteTeam(int id) {
		Team team = this.findTeam(id);
		if(team!=null) {
			teamList.remove(team);
		}
	}
	
	public ArrayList<Team> getTeamList(){
		return this.teamList;
	}
}
