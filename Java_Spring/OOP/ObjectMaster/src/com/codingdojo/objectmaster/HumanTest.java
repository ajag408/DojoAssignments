package com.codingdojo.objectmaster;

public class HumanTest {

	public static void main(String[] args) {
		Human jefferey = new Human();
		Human linda = new Human();
		System.out.println(jefferey.health);
		linda.attack(jefferey);
		System.out.println(jefferey.health);

	}

}
