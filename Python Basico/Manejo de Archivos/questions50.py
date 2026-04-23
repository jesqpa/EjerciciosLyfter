def convert_to_upper(path): 
	upperText = ""
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			text = line.strip()	
			upperText += text.upper() + "\n"
	return upperText

def write_to_file(path, text):  
    with open(path, 'w', encoding='utf-8' ) as file: 
        file.write(text)


uppertext = convert_to_upper('holamundo.txt')
write_to_file('new_holamundo_uppertext.txt', uppertext)
print(f" {uppertext} " )
