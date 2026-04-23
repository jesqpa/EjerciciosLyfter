my_list = ['4', 'hola', '10', '5.2'] 


def convertir_a_entero(list):    
    for value in list:
        try:        
            new_value=int(value)
            print(f"'{value}' convertido a {new_value}")
        except ValueError:
            print(f"No se pudo convertir el elemento: {value}")
        



print(f"my_list: {my_list}")
convertir_a_entero(my_list)