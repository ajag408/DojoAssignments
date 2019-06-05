package com.codingdojo.objectmaster;

public class Ninja extends Human {
	Ninja(){
		stealth = 10;
	}
	
	public void steal(Human poor) {
		int stolenHealth = stealth;
		poor.health = poor.health - stolenHealth;
		this.health = this.health + stolenHealth;
	}
	
	public void runAway() {
		this.health = this.health - 10;
	}
}
