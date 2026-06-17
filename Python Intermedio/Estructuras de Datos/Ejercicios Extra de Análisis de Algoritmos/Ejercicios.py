def manual_add(number):     # O(n)
    result = 0     # O(1)
    for i in range(1, number + 1):     # O(n)
        result += i     # O(1)
    return result     # O(1)


def add_formula(number):     # O(1)
    return number * (number + 1) // 2     # O(1)

# ¿Cuál es la complejidad de cada versión?
#   manual_add(number):     # O(n)
#   add_formula(number):    # O(1)
# ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué? 
#   Respuesta: usaría add_formula porque no tiene ciclos




def linear_search(my_list, target):     # O(n)
    for item in my_list:     # O(n)
        if item == target:     # O(1)
            return True     # O(1)
    return False     # O(1)


def binary_search(my_list, target):     # O(n)
    low = 0     # O(1)
    high = len(my_list) - 1     # O(1)
    while low <= high:     # O(n)
        mid = (low + high) / 2     # O(1)
        if my_list[mid] == target:     # O(1)
            return True     # O(1)
        elif my_list[mid] < target:     # O(1)
            low = mid + 1     # O(1)
        else:
            high = mid - 1     # O(1)
    return False     # O(1)


# ¿Cuál es la complejidad de cada algoritmo?
#   linear_search(my_list, target):     # O(n)
#   binary_search(my_list, target):     # O(n)
# ¿En qué condiciones conviene usar cada uno?
#   binary_search es más conveniente entre más grande sea my_list
# ¿Qué pasa si la lista no está ordenada?
#   en una lista no ordenada, binary_search no devolverá el resultado correcto.


def print_all_pairs(my_dict):    # O(n^2)
    for key1 in my_dict:     # O(n)
        for key2 in my_dict:    # O(n^2)
            print(f"{key1}-{key2}")     # O(1)


# ¿Cuál es la complejidad temporal?
# O(n^2)
# ¿Cuanto dura si hay 1 millón de claves?
# (1 millón)^2