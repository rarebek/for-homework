class Song:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre

    def get_title(self):
        return self.title

    def get_duration(self):
        return self.duration

    def get_genre(self):
        return self.genre


class Artist:
    def __init__(self, name, nationality, genre):
        self.name = name
        self.nationality = nationality
        self.genre = genre

    def get_name(self):
        return self.name

    def get_nationality(self):
        return self.nationality

    def get_genre(self):
        return self.genre


class Album:
    def __init__(self, title, release_year, artist, songs):
        self.title = title
        self.release_year = release_year
        self.artist = artist
        self.songs = songs

    def get_title(self):
        return self.title

    def get_release_year(self):
        return self.release_year

    def get_artist(self):
        return self.artist

    def get_songs(self):
        return self.songs


class Playlist:
    def __init__(self, title, songs):
        self.title = title
        self.songs = songs

    def get_title(self):
        return self.title

    def get_songs(self):
        return self.songs


song1 = Song("Song 1", 180, "Pop")
song2 = Song("Song 2", 210, "Rock")
song3 = Song("Song 3", 240, "Hip Hop")

artist = Artist("Artist 1", "Country", "Pop")

album = Album("Album 1", 2022, artist, [song1, song2, song3])

top_hits_playlist = Playlist("Top Hits", [song1, song2])
favorites_playlist = Playlist("Favorites", [song1, song3])

playlists = [top_hits_playlist, favorites_playlist]

for playlist in playlists:
    print(f"{playlist.get_title()}:")
    for song in playlist.get_songs():
        print(song.get_title())
    print()