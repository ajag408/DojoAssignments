package com.codingdojo.zookeeper;

public class Gorilla extends Mammal {
	public void throwSomething() {
		System.out.println("The gorilla has thrown something");
		energyLevel = energyLevel - 5;
	}
	
	public void eatBanana() {
		System.out.println("Mucho gusto");
		energyLevel = energyLevel + 10;
	}
	
	public void climb() {
		System.out.println("Foolish endeavor");
		energyLevel = energyLevel - 10;
	}
}
