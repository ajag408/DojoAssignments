package com.akash.lookify.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.akash.lookify.models.Song;

@Repository
public interface SongRepository extends CrudRepository<Song, Long> {

}
