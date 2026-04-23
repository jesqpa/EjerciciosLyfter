words_list = ["cielo", "sol", "maravilloso", "días"] 

def get_words_more_than(words):   
    new_word_list = [] 
    max_size = int(input("Ingrese el numero de letras minimas en la palabra: "))
    for word in words:
        if(len(word)>max_size):
            new_word_list.append(word)
    return new_word_list

print(f"{words_list}")
print(get_words_more_than(words_list)) 