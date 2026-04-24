import json

def extract_json(path): 
	json_text = ""
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			text = line.strip()	
			json_text += text	
	return json.loads(json_text)



def write_to_file(path, text):  
    with open(path, 'w', encoding='utf-8' ) as file: 
        file.write(text+'\n')

def append_new_pokemon(data):
	try:
		name = input("Digite el nombre del Pokemon: ")		
		if(name==""):
			raise ValueError("El nombre no puede estar vacío")
	except ValueError as error:
		print(f"Error: {error}")
		return
	
	try:
		type_ = input("Digite el tipo del Pokemon: ")
		if(type_==""):
			raise ValueError("El tipo no puede estar vacío")
	except ValueError as error:
		print(f"Error: {error}")
		return

	try:
		hp = int(input("Digite el HP del Pokemon: "))
	except ValueError:
		print("Error: El HP debe ser un numero valido")
		return
	
	try:
		attack = int(input("Digite el ataque del Pokemon: "))
	except ValueError:
		print("Error: El ataque debe ser un numero valido")
		return
	
	try:
		defense = int(input("Digite la defensa del Pokemon: "))
	except ValueError:
		print("Error: La defensa debe ser un numero valido")
		return
	
	new_pokemon = {
		"name": name,
		"type": type_,
		"hp": hp,
		"attack": attack,
		"defense": defense
	}
	data.append(new_pokemon)
	write_to_file('pokemons.json', json.dumps(data, indent=4))

def main():
	data = extract_json('pokemons.json')
	append_new_pokemon(data)

main()



