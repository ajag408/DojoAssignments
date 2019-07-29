package com.akash.languages.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.akash.languages.models.Language;
import com.akash.languages.services.LanguageService;



@Controller
public class LanguageController {
	 private final LanguageService languageService;
	    
	    public LanguageController(LanguageService languageService) {
	        this.languageService = languageService;
	    }
	    
	    @RequestMapping("/languages")
	    public String index(Model model, @ModelAttribute("language") Language language) {
	        List<Language> languages = languageService.allLanguages();
	        model.addAttribute("languages", languages);
	        return "/languages/index.jsp";
	    }
	    
	    @RequestMapping(value="/languages", method=RequestMethod.POST)
	    public String create(@Valid @ModelAttribute("language") Language language, BindingResult result) {
//	    	System.out.println(language.getVersion());
	        if (result.hasErrors()) {
	            return "/languages/index.jsp";
	        } else {
	            languageService.createlanguage(language);
	            return "redirect:/languages";
	        }
	    }
	    
	    @RequestMapping(value="/languages/delete/{id}")
	    public String destroy(@PathVariable("id") Long id) {
	        languageService.deleteLanguage(id);
	        return "redirect:/languages";
	    }
	    
	    
	    @RequestMapping("/languages/edit/{id}")
	    public String edit(@PathVariable("id") Long id, Model model) {
	        Language language = languageService.findLanguage(id);
	        model.addAttribute("language", language);
	        return "/languages/edit.jsp";
	    }
	    
	    @RequestMapping(value="/languages/{id}", method=RequestMethod.PUT)
	    public String update(@Valid @ModelAttribute("language") Language language, BindingResult result, @PathVariable("id") Long id, @RequestParam("name") String name, @RequestParam("creator") String creator,@RequestParam("version") String version) {
	        if (result.hasErrors()) {
	            return "/languages/edit.jsp";
	        } else {

	            languageService.updateLanguage(id, name, creator, version);
	            return "redirect:/languages";
	        }
	    }
	   
	    @RequestMapping("/languages/{id}")
	    public String show(@PathVariable("id") Long id, Model model) {
	    	Language language = languageService.findLanguage(id);
	    	model.addAttribute("language", language);
	        return "/languages/show.jsp";
	    }
	    
}
