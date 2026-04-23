def capture_text(): 
    input_text = input("Ingrese un texto: ")
    write_to_file('captures.txt', input_text)

def write_to_file(path, text):  
    with open(path, 'a', encoding='utf-8' ) as file: 
        file.write(text+'\n')

capture_text()