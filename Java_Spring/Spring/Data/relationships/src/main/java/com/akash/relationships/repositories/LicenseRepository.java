package com.akash.relationships.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.akash.relationships.models.License;

@Repository
public interface LicenseRepository extends CrudRepository<License, Long>{

}
