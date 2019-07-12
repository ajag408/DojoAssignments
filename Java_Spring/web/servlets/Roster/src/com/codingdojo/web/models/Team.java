package com.codingdojo.web.models;
import java.util.ArrayList;

public class Team {
	private String name;
	ArrayList<Player> playerList = new ArrayList<Player>();
	private int id;
	private int currentPlayerID;
	
	public Team() {
	}
	
	public Team(String name, int id) {
		this.name = name;
		this.id = id;
	}
	
	
	public Player findPlayer(int id) {
		for(int i = 0; i<playerList.size(); i++) {
			Player player = playerList.get(i);
			if(player.getID() == id) {
				return player;
			}
		}
		return null;
	}
	
	public String getName() {
		return name;
	}
	
	public int getID() {
		return id;
	}
	
	public int getCurrentPlayerID() {
		return this.currentPlayerID;
	}
	
	public void addPlayer(Player player) {
		playerList.add(player);
		this.currentPlayerID = this.currentPlayerID+1;
	}
	
	public void deletePlayer(int id) {
		Player player = this.findPlayer(id);
		if(player!=null) {
			playerList.remove(player);
		}
	}
	
	public int getPlayerCount() {
		return playerList.size();
	}
	
	public ArrayList<Player> getPlayerList(){
		return this.playerList;
	}
}
