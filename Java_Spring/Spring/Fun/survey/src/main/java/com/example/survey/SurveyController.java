package com.example.survey;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class SurveyController {
    @RequestMapping("/")
    public String index() {
      return "survey.jsp";
    }
    
    @RequestMapping(value = "/result", method=RequestMethod.POST)
    public String process(Model model, @RequestParam(value="name") String name, @RequestParam(value="language") String language, @RequestParam(value="location") String location, @RequestParam(value="comments") String comments) {
      model.addAttribute("name", name);
      model.addAttribute("language", language);
      model.addAttribute("location", location);
      model.addAttribute("comments", comments);
      if(language.equals("Java")) {
    	  return "java.jsp";
      } else {
    	  return "results.jsp";
      }
    }
}
