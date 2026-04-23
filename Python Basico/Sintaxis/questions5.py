name = input("¿Cuál es su nombre? ")
lastname = input("¿Cuál es su apellido? ")
age = int(input("¿Cuántos años tienes? "))


if(age<1):
    print(f"{name} {lastname} es un bebé.")
elif(age<=8):
    print(f"{name} {lastname} es un niño.")
elif(age<=12):
    print(f"{name} {lastname} es un preadolescente.")
elif(age<=19):
    print(f"{name} {lastname} es un adolescente.")
elif(age<=35):
    print(f"{name} {lastname} es un adulto joven.")
elif(age<=65):
    print(f"{name} {lastname} es un adulto.")
else :
    print(f"{name} {lastname} es un adulto mayor.")
