package com.akash.dojos.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.akash.dojos.models.Dojo;
import com.akash.dojos.models.Ninja;
import com.akash.dojos.services.DojoService;
import com.akash.dojos.services.NinjaService;

@Controller
public class DojoController {
    private final DojoService dojoService;
    private final NinjaService ninjaService;
    
    public DojoController(DojoService dojoService, NinjaService ninjaService) {
        this.dojoService = dojoService;
        this.ninjaService = ninjaService;
    }
    
    @RequestMapping("/dojos/new")
    public String addDojo(Model model) {
    	model.addAttribute("dojo", new Dojo());
    	return "/DN/newDojo.jsp";
    }
    
    @RequestMapping(value="/dojo", method=RequestMethod.POST)
    public String createPerson(@Valid @ModelAttribute("dojo") Dojo dojo, BindingResult result) {
        if (!result.hasErrors()) {
        	dojoService.createDojo(dojo);
        }
        return "redirect:/dojos/new";
    }
    
    @RequestMapping("/ninjas/new")
    public String addLicense(Model model) {
    	List<Dojo> dojos = dojoService.allDojos();
    	model.addAttribute("ninja", new Ninja());
    	model.addAttribute("dojos", dojos);
    	return "/DN/newNinja.jsp";
    }
}
