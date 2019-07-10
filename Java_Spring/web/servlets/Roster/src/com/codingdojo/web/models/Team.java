package com.codingdojo.web.models;
import java.util.ArrayList;

public class Team {
	private String name;
	ArrayList<Player> playerList = new ArrayList<Player>();
	private int id;
	
	public Team() {
	}
	
	public Team(String name, int id) {
		this.name = name;
		this.id = id;
	}
	
	public String getName() {
		return name;
	}
	
	public void addPlayer(Player player) {
		playerList.add(player);
	}
	
	public void deletePlayer(int id) {
		playerList.remove(id);
	}
	
	public int getPlayerCount() {
		return playerList.size();
	}
}
