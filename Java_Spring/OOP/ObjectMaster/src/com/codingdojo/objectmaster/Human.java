package com.codingdojo.objectmaster;

public class Human {
	protected int stealth = 3;
	protected int strength = 3;
	protected int intelligence = 3;
	protected int health = 100;
	
	public void attack(Human hanu) {
		hanu.health = hanu.health - this.strength;
	}
}
