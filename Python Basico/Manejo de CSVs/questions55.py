import csv

def extract_csv(path): 
	games_list = []
	with open(path, 'r', encoding='utf-8' ) as file: 
		reader = csv.DictReader(file)		
		for row in reader:			
			games_list.append(row)
	return games_list

games = extract_csv('video_games.csv')

def get_by_category(games): 
	categ = input('Indique la clasificación deseada: ').capitalize()
	cant = 0
	for game in games: 
		if game.get('clasificacion') == categ: 
			print(game.get('nombre'))
			cant += 1

	if cant == 0: 
		print('No se encontraron juegos con esa clasificación')

get_by_category(games)
