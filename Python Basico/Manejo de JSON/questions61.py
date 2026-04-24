import json

def extract_json(path): 
	json_text = ""
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			text = line.strip()	
			json_text += text	
	return json.loads(json_text)


def print_pokemons(data, type_filter):
	counter = 0
	list = []
	for pokemon in data:		
		if pokemon['type'][0].lower() == type_filter.lower():
			list.append(pokemon['name']['english'])
			counter += 1			
	if counter == 0:
		print("No se encontraron Pokémon de ese tipo.")	
	else:
		print(f"Los Pokémon de tipo {type_filter} son:")
		for name in list:
			print(name)

def main():
	data = extract_json('pokemons.json')
	type = input("Indique el tipo de Pokémon (water, fire, electric): ")
	print_pokemons(data, type)
	

main()



