import json

def extract_json(path): 
	json_text = ""
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			text = line.strip()	
			json_text += text	
	return json.loads(json_text)


def extract_levels(data):	
	levels = {}
	for pokemon in data:
		level = pokemon['level']
		type = pokemon['type'][0]
		if type not in levels:
			levels[type] = []
		levels[type].append(level)
	return levels

def print_average_levels(levels):
	for type, level_list in levels.items():
		average = sum(level_list) / len(level_list)
		print(f"Tipo: {type} >> Promedio de nivel: {average:.1f}")

def main():
	data = extract_json('pokemons.json')
	levels = extract_levels(data)
	print_average_levels(levels)

main()



