package com.akash.languages.models;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.persistence.Table;
import javax.validation.constraints.Size;
@Entity
@Table(name="languages")
public class Language {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Size(min = 2, max = 20, message = "between 2 and 20 chars")
    private String name;
    @Size(min = 2, max = 20, message = "between 2 and 20 chars")
    private String creator;
    @Size(min=1, message = "Version cannot be null")
    private String version;
    // This will not allow the createdAt column to be updated after creation
    @Column(updatable=false)
    private Date createdAt;
    private Date updatedAt;
    
    
    
	public Language() {
	}
	
	
	public Language(String name,
			String creator,
			String version) {

		this.name = name;
		this.creator = creator;
		this.version = version;
	}

	

	public Long getId() {
		return id;
	}


	public void setId(Long id) {
		this.id = id;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public String getCreator() {
		return creator;
	}


	public void setCreator(String creator) {
		this.creator = creator;
	}


	public String getVersion() {
		return version;
	}


	public void setVersion(String version) {
		this.version = version;
	}


	@PrePersist
    protected void onCreate(){
        this.createdAt = new Date();
    }
    @PreUpdate
    protected void onUpdate(){
        this.updatedAt = new Date();
    }
}
