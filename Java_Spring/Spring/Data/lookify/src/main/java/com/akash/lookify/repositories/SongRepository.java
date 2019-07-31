package com.akash.lookify.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.akash.lookify.models.Song;

@Repository
public interface SongRepository extends CrudRepository<Song, Long> {
	List<Song> findTop10ByOrderByRatingDesc();
	
	List<Song> findByArtistIgnoreCaseContaining(String artist);
}
