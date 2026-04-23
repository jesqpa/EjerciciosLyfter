import csv

video_game_headers = (
	'nombre',
	'genero',
	'desarrollador',
	'clasificacion',
)

def input_videogames():
  video_game_list = []
  count = int(input('Cuantos videojuegos quieres agregar? '))
  for cant in range(count):
   name = input('Nombre del videojuego: ')
   gender = input('Genero del videojuego: ')
   developer = input('Desarrollador del videojuego: ')
   classification = input('Clasificacion del videojuego: ')
   video_game_list.append({
	  'nombre': name,
	  'genero': gender,
	  'desarrollador': developer,
	  'clasificacion': classification,
	})
  return video_game_list

def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers, delimiter='\t')
    writer.writeheader()
    writer.writerows(data)

video_game_list = input_videogames()

write_csv_file('video_games_tabs.csv', video_game_list, video_game_headers)