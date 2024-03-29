package com.codingdojo.web.models;

public class Player {
	private String first_name;
	private String last_name;
	private int age;
	private int id;
	
	public Player() {
	}
	
	public Player(String first_name, String last_name, int age, int id) {
		this.first_name = first_name;
		this.last_name = last_name;
		this.age = age;
		this.id = id;
	}
	
	public String getFirstName() {
		return first_name;
	}
	
	public String getLastName() {
		return last_name;
	}
	
	public int getAge() {
		return age;
	}
	
	public int getID() {
		return this.id;
	}
	
}
