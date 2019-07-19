package com.example.ngold;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class GoldController {
    @RequestMapping("/")
    public String index(HttpSession session) {
    	ArrayList<String> actions = new ArrayList<String>();
    	session.setAttribute("gold", 0);
    	session.setAttribute("actions", actions);
        return "redirect:/gold";
    }
    
    @RequestMapping("/gold")
    public String render() {
        return "gold.jsp";
    }
    
    @RequestMapping(value="/find", method=RequestMethod.POST)
    public String process(HttpSession session, @RequestParam(value="place") String place) {
    	int value = (int) session.getAttribute("gold");
    	ArrayList<String> actions = (ArrayList<String>) session.getAttribute("actions");
    	String result = "";
    	if(place.equals("farm")) {
            int max = 20; 
            int min = 10; 
            int range = max - min + 1; 
            int rand = (int)(Math.random() * range) + min; 
            value = value + rand;
            result = "You entered a farm and earned " + rand + " gold. ";
    	} else if(place.equals("cave")){
            int max = 10; 
            int min = 5; 
            int range = max - min + 1; 
            int rand = (int)(Math.random() * range) + min; 
            value = value + rand;
            result = "You entered a cave and earned " + rand + " gold. ";
    	}else if(place.equals("house")){
            int max = 5; 
            int min = 2; 
            int range = max - min + 1; 
            int rand = (int)(Math.random() * range) + min; 
            value = value + rand;
            result = "You entered a house and earned " + rand + " gold. ";
    	}else if(place.equals("casino")){
            int max = 50; 
            int min = -50; 
            int range = max - min + 1; 
            int rand = (int)(Math.random() * range) + min; 
            value = value + rand;
            if(value >= 0) {
            	result = "You entered a casino and earned " + rand + " gold. ";
            } else {
            	result = "You entered a casino and lost " + rand + " gold. Ouch. ";
            }
    	} else if(place.equals("spa")){
                int max = -5; 
                int min = -20; 
                int range = max - min + 1; 
                int rand = (int)(Math.random() * range) + min; 
                value = value + rand;
                result = "You entered a spa and lost " + rand + " gold. ";
         }
    	session.setAttribute("gold", value);
   	 	LocalDateTime myDateObj = LocalDateTime.now();
   	 	DateTimeFormatter timeFormatter = DateTimeFormatter.ofPattern("MMMM d uuuu h:m a");
   	 	String time = myDateObj.format(timeFormatter);
   	 	result = result + "(" + time + ")";
   	 	actions.add(result);
   	 	session.setAttribute("actions", actions);
   	 	if(value <= -20) {
   	 		return "prison.jsp";
   	 	} else {
   	   	return "redirect:/gold";
   	 	}
    }
}
