
def get_vowel_count(text):    
    counter = 0
    for letter in text:
        if(letter in "aeiou"):
            counter += 1
    return counter


my_text = input("Ingrese un texto: ")
print(f"{my_text} contiene {get_vowel_count(my_text)} vocales")
