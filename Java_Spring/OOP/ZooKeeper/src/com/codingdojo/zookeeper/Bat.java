package com.codingdojo.zookeeper;

public class Bat extends Mammal {
	Bat(){
		energyLevel = 300;
	}
	
	public void fly() {
		System.out.println("urp flying");
		energyLevel = energyLevel -50;
	}
	
	public void eatHumans() {
		energyLevel = energyLevel + 25;
	}
	
	public void attackTown() {
		System.out.println("Burnnnnnnnnnn");
		energyLevel = energyLevel - 100;
	}
	
}
