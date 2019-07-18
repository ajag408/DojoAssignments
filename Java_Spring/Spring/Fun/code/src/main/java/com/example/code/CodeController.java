package com.example.code;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
public class CodeController {
    @RequestMapping("/")
    public String index(HttpSession session) {
    	session.setAttribute("code", "bushido");
        return "home.jsp";
    }
    
    @RequestMapping(value="/code", method=RequestMethod.POST)
    public String checkCode(HttpSession session, @RequestParam(value="guess") String guess, RedirectAttributes redirectAttributes) {
    	if(guess.equals(session.getAttribute("code"))) {
    		return "code.jsp";
    	} else {
    		redirectAttributes.addFlashAttribute("error", "Train harder!");
    		return "redirect:/";
    	}
    }
}
