package com.codingdojo.tries;

public class TrieTest {

	public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insertWord("car");
        trie.insertWord("card");
        trie.insertWord("chip");
        trie.insertWord("trie");
        trie.insertWord("try");
        
//        System.out.println(trie.isPrefixValid("tr"));
//        System.out.println(trie.isPrefixValid("ca"));
//        System.out.println(trie.isPrefixValid("ty"));
        
        System.out.println(trie.isWordValid("car"));
        System.out.println(trie.isWordValid("tr"));
        System.out.println(trie.isWordValid("boy"));
        System.out.println(trie.isWordValid("cat"));
	}

}
