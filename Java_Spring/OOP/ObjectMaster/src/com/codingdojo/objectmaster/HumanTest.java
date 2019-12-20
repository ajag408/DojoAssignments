package com.codingdojo.objectmaster;

public class HumanTest {

	public static void main(String[] args) {
		Ninja jefferey = new Ninja();
		Human linda = new Human();
		System.out.println(jefferey.health);
		linda.attack(jefferey);
		jefferey.steal(linda);
		System.out.println(jefferey.health);

	}

}
