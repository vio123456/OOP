


-- Luodaan artist-taulu
CREATE TABLE IF NOT EXISTS artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    followers INTEGER NOT NULL
);

.import --csv --skip 1 t1_artist.csv artist

--TODO album
-- Luodaan album-taulu
CREATE TABLE IF NOT EXISTS album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    tracks INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);
--1. Create schema 
-- -colums
-- -foreign key
.import --csv --skip 1 t1_album.csv album
