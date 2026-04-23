import csv

def extract_csv(path): 
	games_list = []
	with open(path, 'r', encoding='utf-8' ) as file: 
		reader = csv.DictReader(file)		
		for row in reader:			
			games_list.append(row)
	return games_list

games = extract_csv('video_games.csv')

def extract_genres(games): 
	genres = {}
	for game in games: 
		genre = game.get('genero')
		if genre: 
			genres[genre] = genres.get(genre, 0) + 1
	return genres

def print_genres(genres): 
	for genre, count in genres.items(): 
		print(f"{genre}: {count}")

print_genres(extract_genres(games))