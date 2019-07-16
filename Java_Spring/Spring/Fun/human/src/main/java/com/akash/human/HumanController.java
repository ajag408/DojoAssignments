package com.akash.human;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HumanController {
    @RequestMapping("/")
    public String index(@RequestParam(value="first_name", required = false) String first_name,@RequestParam(value="last_name", required = false) String last_name) {
    	if(first_name == null || last_name == null) {
    		if(first_name == null && last_name == null) {
    			return "Hello Human!";
    		}else if(first_name == null) {
    			return "Hello " + last_name + "!";
    		}else if(last_name == null) {
    			return "Hello " + first_name + "!";
    		}else {
    			return null;
    		}
    	} else {
    		 return "Hello " + first_name + "  " + last_name + "!";
    	}
    }
}
