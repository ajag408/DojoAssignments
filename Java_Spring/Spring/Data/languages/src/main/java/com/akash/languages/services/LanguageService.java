package com.akash.languages.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.akash.languages.models.Language;
import com.akash.languages.repositories.LanguageRepository;
import com.akash.languages.models.Language;

@Service
public class LanguageService {
    private final LanguageRepository languageRepository;
    
    public LanguageService(LanguageRepository languageRepository) {
        this.languageRepository = languageRepository;
    }
    
    // returns all the languages
    public List<Language> allLanguages() {
        return (List<Language>) languageRepository.findAll();
    }
    // creates a language
    public Language createlanguage(Language l) {
        return languageRepository.save(l);
    }
    // retrieves a language
    public Language findLanguage(Long id) {
        Optional<Language> optionalLanguage = languageRepository.findById(id);
        if(optionalLanguage.isPresent()) {
            return optionalLanguage.get();
        } else {
            return null;
        }
    }
    
    
    public void deleteLanguage(Long id) {
    	languageRepository.deleteById(id);
    }
	public Language updateLanguage(Long id, String name, String creator, String version) {
    	Language language = this.findLanguage(id);
    	if(language != null) {
    		language.setName(name);
    		language.setCreator(creator);
    		language.setVersion(version);
    		return languageRepository.save(language);
    	} else {
    		return null;
    	}
	}
}
