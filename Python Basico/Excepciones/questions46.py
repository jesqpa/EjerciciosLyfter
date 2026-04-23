my_list = ['10', 'manzana', '5.5', '3', 'n/a'] 


def sumar_valores(list):    
    summation = 0 
    for value in list:
        try:        
            new_value=float(value)
            summation+=new_value
            print(f"{value} sumado correctamente")
        except ValueError:
            print(f"Elemento inválido: {value}")
    print(f"La suma total es: {summation}")



print(f"my_list: {my_list}")
sumar_valores(my_list)