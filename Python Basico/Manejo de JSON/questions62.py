import json

def extract_json(path): 
	json_text = ""
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			text = line.strip()	
			json_text += text	
	return json.loads(json_text)


def print_pokemons_stats(data):
	for pokemon in data:
		print(f"Name: {pokemon['name']['english']}")				
		print(f"Base Stats:")		
		for stat, value in pokemon['base'].items():
			print(f"  {stat}: {value}")


def main():
	data = extract_json('pokemons.json')
	print_pokemons_stats(data)
	

main()



