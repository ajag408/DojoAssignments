package com.codingdojo.objectmaster;

public class Wizard extends Human {
	Wizard(){
		health = 50;
		intelligence = 8;
	}
	
	public void heal(Human unwise) {
		unwise.health = unwise.health + this.intelligence;
	}
	
	public void fireball(Human scorched) {
		scorched.health = scorched.health - (3*this.intelligence);
	}
}
