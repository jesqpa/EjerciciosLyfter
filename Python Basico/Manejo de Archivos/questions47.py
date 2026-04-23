def open_songs_file(path): 
	names = []
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			names.append(line.strip())			
	return names

def write_songs_file(path, songs):  
    with open(path, 'w', encoding='utf-8' ) as file: 
        for song in songs: 			
            file.write(song + '\n')


songs = open_songs_file('canciones.txt')
print(f"Lista canciones: {songs}")
songs.sort()
print(f"Lista ordenadas: {songs}")
write_songs_file('canciones_ordenadas.txt', songs)