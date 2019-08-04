package com.akash.relationships.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.akash.relationships.models.License;
import com.akash.relationships.models.Person;
import com.akash.relationships.services.LicenseService;
import com.akash.relationships.services.PersonService;

@Controller
public class dLicenseController {
    private final PersonService personService;
    private final LicenseService licenseService;
    private int licenseNumber = 1;
    
    public dLicenseController(PersonService personService, LicenseService licenseService) {
        this.personService = personService;
        this.licenseService = licenseService;
    }
    
    @RequestMapping("/persons/new")
    public String addPerson(Model model) {
    	model.addAttribute("person", new Person());
    	return "/dLicense/newPerson.jsp";
    }
    
    @RequestMapping(value="/person", method=RequestMethod.POST)
    public String createPerson(@Valid @ModelAttribute("person") Person person, BindingResult result) {
        if (!result.hasErrors()) {
        	personService.createPerson(person);
        }
        return "redirect:/persons/new";
    }
    
    @RequestMapping("/licenses/new")
    public String addLicense(Model model) {
    	List<Person> persons = personService.allPeople();
    	model.addAttribute("license", new License());
    	model.addAttribute("persons", persons);
    	return "/dLicense/newLicense.jsp";
    }
    
    @RequestMapping(value="/license", method=RequestMethod.POST)
    public String createPerson(@Valid @ModelAttribute("license") License license, BindingResult result) {
        if (!result.hasErrors()) {
        	license.setNumber(licenseNumber);
        	licenseService.createLicense(license);
        	licenseNumber = licenseNumber+1;
        }
        return "redirect:/licenses/new";
    }
    
    @RequestMapping("/persons/{id}")
    public String show(@PathVariable("id") Long id, Model model) {
    	Person person = personService.findPerson(id);
    	model.addAttribute("person", person);
        return "/dLicense/show.jsp";
    }
}
