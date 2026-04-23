def get_user_data():
    try:
        name = input("Cuál es su nombre? ")
        if(name.isdigit()):
            raise ValueError("El nombre no puede ser un número") 
        age = input("Cuál es su edad? ")
        if(age.isdigit() == False):
            raise ValueError("La edad debe ser un número válido") 
        print(f"Hola {name}, su edad es {age} ")
    except ValueError as error:
        print(error)
        get_user_data()


get_user_data()