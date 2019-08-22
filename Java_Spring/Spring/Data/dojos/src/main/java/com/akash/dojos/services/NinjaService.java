package com.akash.dojos.services;

import org.springframework.stereotype.Service;

import com.akash.dojos.models.Ninja;
import com.akash.dojos.repositories.NinjaRepository;

@Service
public class NinjaService {
    private final NinjaRepository ninjaRepository;
    
    public NinjaService(NinjaRepository ninjaRepository) {
        this.ninjaRepository = ninjaRepository;
    }
    
    public Ninja createNinja(Ninja b) {
        return ninjaRepository.save(b);
    }
}
