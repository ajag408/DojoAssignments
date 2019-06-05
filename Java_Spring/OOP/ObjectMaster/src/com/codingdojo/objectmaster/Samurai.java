package com.codingdojo.objectmaster;

public class Samurai extends Human{
	static int numSam = 0;
	Samurai(){
		numSam++;
		health = 200;
	}
	
	public void deathBlow(Human punched) {
		if(punched instanceof Samurai) {
			numSam--;
		}
		punched = null;
		this.health = this.health/2;
	}
	
	public void meditate() {
		int halfCurrentHealth = this.health/2;
		this.health = this.health + halfCurrentHealth;
	}
	
	public int howMany() {
		return numSam;
	}
}
