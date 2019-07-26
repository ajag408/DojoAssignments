package com.akash.languages.controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

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
	        if (result.hasErrors()) {
	            return "/languages/index.jsp";
	        } else {
	            languageService.createlanguage(language);
	            return "redirect:/languages";
	        }
	    }
}
