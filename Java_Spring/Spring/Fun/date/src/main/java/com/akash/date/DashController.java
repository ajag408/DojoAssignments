package com.akash.date;
import java.time.LocalDateTime; // Import the LocalDateTime class
import java.time.format.DateTimeFormatter; 
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
public class DashController {
    @RequestMapping("/")
    public String index() {
        return "choices.jsp";
    }	
    @RequestMapping("/date")
    public String date(Model model) { 
    	 LocalDateTime myDateObj = LocalDateTime.now(); 
    	 DateTimeFormatter dayFormatter = DateTimeFormatter.ofPattern("EEEE");
    	 DateTimeFormatter day2Formatter = DateTimeFormatter.ofPattern("dd");
    	 DateTimeFormatter day3Formatter = DateTimeFormatter.ofPattern("MMMM, yyyy");
    	 String dayOne = myDateObj.format(dayFormatter);
    	 String dayTwo = myDateObj.format(day2Formatter);
    	 String dayThree = myDateObj.format(day3Formatter);
    	 model.addAttribute("stringOne", dayOne);
    	 model.addAttribute("stringTwo", dayTwo);
    	 model.addAttribute("stringThree", dayThree);
         return "date.jsp";
    }
    @RequestMapping("/time")
    public String time(Model model) { 
   	 	LocalDateTime myDateObj = LocalDateTime.now();
   	 	DateTimeFormatter timeFormatter = DateTimeFormatter.ofPattern("h:m a");
   	 	String time = myDateObj.format(timeFormatter);
//   	 	System.out.println(time);
   	 	model.addAttribute("time", time);
        return "time.jsp";
    }
}
