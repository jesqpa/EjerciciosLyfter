to_find=int(input("Indique un numero a buscar: "))
counter=0

for index in range(10):
    number=int(input("Indique un numero para la lista: "))
    if(number==to_find):
        counter = counter + 1
    

print(f"El número {to_find} aparece {counter} veces.")