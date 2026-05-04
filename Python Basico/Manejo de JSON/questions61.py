import json

def extract_json(path): 
	with open(path, 'r', encoding='utf-8' ) as file: 		
		return json.load(file)


def print_pokemons(data, type_filter):
	counter = 0
	pokemon_list = []
	for pokemon in data:
		pokemon_type = pokemon['type']		
		for t in pokemon_type:
			if t.lower() == type_filter.lower():
				pokemon_list.append(pokemon['name']['english'])
				counter += 1	
	if counter == 0:
		print("No se encontraron Pokémon de ese tipo.")	
	else:
		print(f"Los Pokémon de tipo {type_filter} son:")
		for name in pokemon_list:
			print(name)

def main():
	data = extract_json('pokemons.json')
	pokemon_type_filter = input("Indique el tipo de Pokémon (water, fire, electric): ")
	print_pokemons(data, pokemon_type_filter)
	

main()



