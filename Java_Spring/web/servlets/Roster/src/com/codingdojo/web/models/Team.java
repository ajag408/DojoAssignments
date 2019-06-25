package com.codingdojo.web.models;
import java.util.ArrayList;

public class Team {
	private String name;
	ArrayList<Player> playerList = new ArrayList<Player>();
	
	public Team() {
	}
	
	public Team(String name) {
		this.name = name;
	}
	
	public void addPlayer(Player player) {
		playerList.add(player);
	}
	
	
}
