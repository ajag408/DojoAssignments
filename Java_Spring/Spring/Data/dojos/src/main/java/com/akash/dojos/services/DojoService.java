package com.akash.dojos.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.akash.dojos.models.Dojo;
import com.akash.dojos.repositories.DojoRepository;

@Service
public class DojoService {
    private final DojoRepository dojoRepository;
    
    public DojoService(DojoRepository dojoRepository) {
        this.dojoRepository = dojoRepository;
    }
    
    public List<Dojo> allDojos() {
        return (List<Dojo>) dojoRepository.findAll();
    }
    
    public Dojo createDojo(Dojo b) {
        return dojoRepository.save(b);
    }
    
    public Dojo findDojo(Long id) {
        Optional<Dojo> optionalDojo = dojoRepository.findById(id);
        if(optionalDojo.isPresent()) {
            return optionalDojo.get();
        } else {
            return null;
        }
    }
}
