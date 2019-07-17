package com.akash.counter;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
public class CounterController {
	@RequestMapping("/")
	public String index(HttpSession session) {
	   if(session.getAttribute("count") == null) {
		   session.setAttribute("count", 1);
	   } else {
		   Integer count = (Integer) session.getAttribute("count");
		   count = count + 1;
		   session.setAttribute("count", count);
	   }
	   return "home.jsp";
	}	
	
	@RequestMapping("/counter")
	public String counter(HttpSession session) {
		   if(session.getAttribute("count") == null) {
			   session.setAttribute("count", 0);
		   } else {
			   Integer count = (Integer) session.getAttribute("count");
		   }
		 return "counter.jsp";
	}
	@RequestMapping("/counter2")
	public String counter2(HttpSession session) {
		   if(session.getAttribute("count") == null) {
			   session.setAttribute("count", 2);
		   } else {
			   Integer count = (Integer) session.getAttribute("count");
			   count = count + 2;
			   session.setAttribute("count", count);
		   }
		 return "counter2.jsp";
	}
	@RequestMapping("/reset")
	public String reset(HttpSession session) {
		if(session.getAttribute("count") != null) {
			session.setAttribute("count", 0);
		}
		return "counter.jsp";
	}
}
