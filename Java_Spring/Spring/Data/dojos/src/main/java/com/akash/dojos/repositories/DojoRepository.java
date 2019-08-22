package com.akash.dojos.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.akash.dojos.models.Dojo;

@Repository
public interface DojoRepository extends CrudRepository<Dojo, Long> {

}
