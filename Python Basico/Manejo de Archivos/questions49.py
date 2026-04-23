def get_words_amount(path): 
	count = 0
	with open(path, 'r', encoding='utf-8' ) as file: 
		for line in file.readlines(): 			
			text = line.strip()	
			count += len(text.split())

	return count



words = get_words_amount('words.txt')
print(f"Este archivo contiene {words} palabras" )
