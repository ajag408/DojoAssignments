package com.codingdojo.calculator;
import java.util.ArrayList;

public class Calculator implements java.io.Serializable{
	private ArrayList<Object> userNum = new ArrayList<Object>();
	private double result;
	
	public Calculator() {	
	}
	
	public void performOperation(String input) {
		if(input == "+" || input == "-" || input == "*" || input == "/") {
			userNum.add(input);
		}else if(input == "="){
			for(int i = 0; i<userNum.size(); i++) {
				if(userNum.get(i) == "*") {
					double tempVal = (double) userNum.get(i-1) * (double) userNum.get(i+1);
					userNum.set(i-1, tempVal);
					userNum.subList(i, i+2).clear();
				} else if(userNum.get(i) == "/") {
					double tempVal = (double) userNum.get(i-1) / (double) userNum.get(i+1);
					userNum.set(i-1, tempVal);
					userNum.subList(i, i+2).clear();
				}
			}
			for(int i = 0; i<userNum.size(); i++) {
				if(userNum.get(i) == "+") {
					double tempVal = (double) userNum.get(i-1) + (double) userNum.get(i+1);
					userNum.set(i-1, tempVal);
					userNum.subList(i, i+2).clear();
				} else if(userNum.get(i) == "-") {
					double tempVal = (double) userNum.get(i-1) - (double) userNum.get(i+1);
					userNum.set(i-1, tempVal);
					userNum.subList(i, i+2).clear();
				}
			}
			result = (double) userNum.get(0);
			
		}else {
			userNum.add(Double.parseDouble(input));
		}
		
	}
	
	public void getResults() {
		System.out.println(result);
	}
}
