package com.codingdojo.dll;

public class DLL {
    public Node head;
    public Node tail;
    
    public DLL() {
        this.head = null;
        this.tail = null;
    }
    
    // the push method will add a new node to the end of the list
    public void push(Node newNode) {
        // if there is no head in the list, aka, an empty list, we set the newNode to be the head and tail of the list
        if(this.head == null) {
            this.head = newNode;
            this.tail = newNode;
            return;
        }
        
        // first find the lastNode in the list
        // then, set the lastNode's next to be the newNode;
        // then, we have to set the previous of the lastNode to the lastNode that we found previously.
        // finally, set the list's tail to be the node that we have added
        Node lastNode = this.tail;
        lastNode.next = newNode;
        newNode.previous = lastNode;
        this.tail = newNode;
    }
    
    public void printValuesForward() {
        // find the first node, aka head.
        Node current = this.head;
        
        // while the current node exists...
        while(current != null) {
            // print it's value
            System.out.println(current.value);
            // and move on to it's next node.
            current = current.next;
        }
    }
    
    public void printValuesBackward() {
    	Node current = this.tail;
    	while(current!=null) {
    		System.out.println(current.value);
    		current = current.previous;
    	}
    }
    
    public Node pop() {
    	Node store = this.tail;
    	if(this.tail.previous == null) {
    		this.head = null;
    		this.tail = null;
    		return store;
    	} else {
    		this.tail = this.tail.previous;
    		this.tail.next.previous = null;
    		this.tail.next = null;
    	}
    	return store;
    }
    
    public boolean contains(int value) {
    	Node current = this.head;
    	while(current!=null) {
    		if(current.value == value) {
    			return true;
    		}
    		current = current.next;
    	}
    	return false;
    }
    
    public int size() {
    	Node current = this.head;
    	int count = 0;
    	while(current!=null) {
    		count++;
    		current = current.next;
    	}
    	return count;
    }
    
    public void insertAt(Node newNode, int index) {
    	Node current = this.head;
    	int count = 0;
    	if(index>this.size()) {
    		System.out.println("List not that large");
    	} else if (index == this.size()){
    		this.push(newNode);
    	} else if (index == 0) {
    		newNode.next = this.head;
    		this.head.previous = newNode;
    		this.head = newNode;
    	} else {
    		while(count<index-1) {
    			current = current.next;
    			count++;
    		}
    		newNode.next = current.next;
    		current.next = newNode;
    		newNode.previous = newNode.next.previous;
    		newNode.next.previous = newNode;
    	}
    	
    }
    
    public void removeAt(int index) {
    	int count = 0;
    	if(index>this.size()) {
    		System.out.println("Not valid index");
    	} else if (index == this.size()) {
    		this.tail = this.tail.previous;
    		this.tail.next.previous = null;
    		this.tail.next = null;
    	} else if (index == 0) {
    		this.head = this.head.next;
    		this.head.previous.next = null;
    		this.head.previous = null;
    	} else {
    		Node current = this.head;
    		while(count<index) {
    			current = current.next;
    			count++;
    		}
    		current.previous.next = current.next;
    		current.next.previous = current.previous;
    		current.previous = null;
    		current.next = null;
    	}
    }
    
    public boolean isPalindrome() {
    	Node front = this.head;
    	Node back = this.tail;
    	for(int i = 0; i<Math.floor(this.size()/2); i++){
    		if(front.value != back.value) {
    			return false;
    		}
    		front = front.next;
    		back = back.previous;
    	}
    	return true;
    }
    
    
    
}
