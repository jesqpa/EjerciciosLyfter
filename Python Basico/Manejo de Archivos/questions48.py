def open_hola_mundo_file(path): 
	text = ""
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			text += line.strip() + " "		
	
	return text

def write_hola_mundo_file(path, text):  
    with open(path, 'w', encoding='utf-8' ) as file: 
        file.write(text)

songs = open_hola_mundo_file('holamundo.txt')
print(f"Texto: {songs}")

write_hola_mundo_file('new_holamundo.txt', songs)
