words = []

for index in range(5):
    word = input("Ingrese una palabra: ")
    if(len(word)>4):
        words.append(word)

print(words)
