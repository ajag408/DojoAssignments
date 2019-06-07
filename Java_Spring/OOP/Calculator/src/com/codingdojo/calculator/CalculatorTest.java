package com.codingdojo.calculator;

public class CalculatorTest {

	public static void main(String[] args) {
		Calculator hung = new Calculator();

		hung.performOperation("10.5");
		
		hung.performOperation("+");
		
		hung.performOperation("5.2");
		
		hung.performOperation("*");
		
		hung.performOperation("10");

		hung.performOperation("=");
		hung.getResults();

	}

}
