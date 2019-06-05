package com.codingdojo.bankaccount;
import java.util.Random;
public class BankAccount {
	private String acctNum;
	private double checkBal;
	private double savBal;
	
	private static int numAcct;
	private static int totMool;
	
	private String generateNumAcct() {
		Random r = new Random();
		int randAcctNum = r.nextInt()+1000000000;
		return Integer.toString(randAcctNum);
	}
	
	BankAccount(){
		acctNum = generateNumAcct();
		numAcct++;	
	}
	
	public void checkCheck() {
		System.out.println("Your checking balance is: " + checkBal);
	}
	
	public void checkSav() {
		System.out.println("Your saving balance is: " + savBal);
	}
	
	public void deposit(String userChoice, double amount) {
		if(userChoice == "checking") {
			checkBal = checkBal + amount;
			totMool = totMool + (int) amount;
		} else if(userChoice == "savings") {
			savBal = savBal + amount;
			totMool = totMool + (int) amount;
		} else {
			System.out.println("Please enter valid account choice (checking or savings)");
		}
	}
	
	public void withdraw(String userChoice, double amount) {
		if(userChoice == "checking") {
			if(amount<=checkBal) {
				checkBal = checkBal - amount;
				totMool = totMool - (int) amount;
			} else {
				System.out.println("You do not have that much in checking");
			}
		} else if(userChoice == "savings") {
			if(amount<=savBal) {
				savBal = savBal - amount;
				totMool = totMool - (int) amount;
			} else {
				System.out.println("You do not have that much in savings");
			}
		} else {
			System.out.println("Please enter valid account choice (checking or savings)");
		}
	}
	
	public void checkTotal() {
		System.out.println(totMool);
	}
}
