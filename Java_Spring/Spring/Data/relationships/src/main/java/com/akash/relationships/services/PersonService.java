package com.akash.relationships.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.akash.relationships.models.Person;
import com.akash.relationships.repositories.PersonRepository;

@Service
public class PersonService {
    private final PersonRepository personRepository;
    
    public PersonService(PersonRepository personRepository) {
        this.personRepository = personRepository;
    }
    
    public List<Person> allPeople() {
        return (List<Person>) personRepository.findAll();
    }
    
    public Person createPerson(Person b) {
        return personRepository.save(b);
    }
    
    public Person findPerson(Long id) {
        Optional<Person> optionalPerson = personRepository.findById(id);
        if(optionalPerson.isPresent()) {
            return optionalPerson.get();
        } else {
            return null;
        }
    }
    
}
