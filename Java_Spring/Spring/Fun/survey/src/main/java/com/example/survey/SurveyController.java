package com.example.survey;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class SurveyController {
    @RequestMapping("/")
    public String index() {
      return "survey.jsp";
    }
}
