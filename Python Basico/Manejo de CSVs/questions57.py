import csv

def extract_csv(path): 
	games_list = []
	with open(path, 'r', encoding='utf-8' ) as file: 
		reader = csv.DictReader(file)		
		for row in reader:			
			games_list.append(row)
	return games_list

games = extract_csv('video_games.csv')



def get_by_developer(games_list): 
	developer = input('Indique el nombre del desarrollador: ')
	result = []
	for game in games_list: 		
		if game.get('desarrollador').lower() == developer.lower(): 
			result.append(game)	
	return result

def print_list_by_developer(games_list):
	result = get_by_developer(games_list)
	if len(result) == 0: 
		print('No hay juegos para el desarrollador especificado.')
	else: 		
		print(f'Juegos desarrollados por {result[0].get("desarrollador")}:')
		for game in result: 
			print(f'{game.get("nombre")} (Clasificación: {game.get("clasificacion")}, Género: {game.get("genero")})')

print_list_by_developer(games)

