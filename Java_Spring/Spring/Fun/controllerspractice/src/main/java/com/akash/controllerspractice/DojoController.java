package com.akash.controllerspractice;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
public class DojoController {
	@RequestMapping("/{locay}")
    public String renderPage(@PathVariable("locay") String locay){
//		System.out.println(locay);
//		locay = (String) locay;
//		System.out.println(locay == "burbank-dojo");
    	if(locay.equals("dojo")) {
    		return "The dojo is awesome!";
    	} else if (locay.equals("burbank-dojo")) {
//    		System.out.println("this should print");
    		return "Burbank Dojo is located in Southern California";
    	} else if (locay.equals("san-jose")) {
    		return "SJ dojo is the headquarters";
    	}else {
    		return null;
    	}
    }
}
