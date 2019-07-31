package com.akash.lookify.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.akash.lookify.models.Song;
import com.akash.lookify.repositories.SongRepository;

@Service
public class SongService {
    private final SongRepository songRepository;
    
    public SongService(SongRepository songRepository) {
        this.songRepository = songRepository;
    }
    
    public List<Song> allSongs() {
        return (List<Song>) songRepository.findAll();
    }
    
    public Song createSong(Song b) {
        return songRepository.save(b);
    }
    
    public Song findSong(Long id) {
        Optional<Song> optionalSong = songRepository.findById(id);
        if(optionalSong.isPresent()) {
            return optionalSong.get();
        } else {
            return null;
        }
    }
    
    public void deleteSong(Long id) {
    	songRepository.deleteById(id);
    }
}
