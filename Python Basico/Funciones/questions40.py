text = "Ejercicios extra de Funciones"

def get_character_count(texto):
    character = input("Ingrese el carácter que desea buscar: ")
    counter=0
    for char in texto:
        if(char==character):
            counter += 1
    return counter

print(f"Texto para buscar: '{text}'")
print(f"Se a encontrado {get_character_count(text)} veces el carácter")


