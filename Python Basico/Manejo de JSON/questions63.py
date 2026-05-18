import json

def extract_json(path): 
	with open(path, 'r', encoding='utf-8' ) as file: 		
		return json.load(file)


def extract_levels(data):	
	levels = {}
	for pokemon in data:
		level = pokemon['level']
		pokemon_type = pokemon['type']
		for t in pokemon_type:
			if t not in levels:
				levels[t] = []
			levels[t].append(level)
	return levels

def print_average_levels(levels):
	for pokemon_type, level_list in levels.items():
		average = sum(level_list) / len(level_list)
		print(f"Tipo: {pokemon_type} >> Promedio de nivel: {average:.1f}")

def main():
	data = extract_json('pokemons.json')
	levels = extract_levels(data)
	print_average_levels(levels)

main()



