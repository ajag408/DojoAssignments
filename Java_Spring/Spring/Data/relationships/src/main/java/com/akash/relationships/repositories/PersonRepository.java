package com.akash.relationships.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.akash.relationships.models.Person;

@Repository
public interface PersonRepository extends CrudRepository<Person, Long> {

}
