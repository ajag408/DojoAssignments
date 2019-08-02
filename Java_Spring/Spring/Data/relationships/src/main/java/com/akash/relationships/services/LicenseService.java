package com.akash.relationships.services;

import org.springframework.stereotype.Service;

import com.akash.relationships.models.License;
import com.akash.relationships.repositories.LicenseRepository;

@Service
public class LicenseService {
    private final LicenseRepository licenseRepository;
    
    public LicenseService(LicenseRepository licenseRepository) {
        this.licenseRepository = licenseRepository;
    }
    
    public License createLicense(License b) {
        return licenseRepository.save(b);
    }
}
