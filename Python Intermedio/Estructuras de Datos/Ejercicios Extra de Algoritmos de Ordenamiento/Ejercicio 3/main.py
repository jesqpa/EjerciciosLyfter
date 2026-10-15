def validated_bubble_sort(list):
    element_count = len(list)

    print(f"Lista original: {list}")

    # Validación 1: Verificar que la lista no esté vacía
    if element_count == 0:
      print("Validación: La lista está vacía - No se puede ordenar")
      return None

    # Validación 2: Verificar que solo sean números (int o float)
    for i in range(element_count):
      if not isinstance(list[i], (int, float)):
        print(f"Validación: El elemento en la posición {i} ('{list[i]}') no es un número (solo se permiten int o float)")
        return None

    # Validación exitosa → ejecutar bubble_sort
    print("Validacion exitosa. Ejecutando bubble_sort...")
    sorted_list = bubble_sort(list)

    print(f"Lista ordenada: {sorted_list}")

    print("¡Ordenamiento completado con éxito!")
    return list


def bubble_sort(list):
    element_count = len(list)
    for i in range(element_count):
        for j in range(0, element_count-i-1):        
            if list[j] > list[j+1]:
                # Intercambiar los elementos: se puede realizar de 2 formas, la más común es usando una variable temporal
                #list[j], list[j+1] = list[j+1], list[j]
                temp = list[j]          # 1. Guardar el valor de la posición j
                list[j] = list[j+1]     # 2. Poner el valor de j+1 en la posición j
                list[j+1] = temp        # 3. Poner el valor guardado en j+1               
    
    return list

def main():

    list1 = [64, 34, 25, 12,"hola", 22, 11, 90]
    list2 = [64, 34, 25, 12, 22, 11, 90]

    validated_bubble_sort(list1)
    validated_bubble_sort(list2)


    

if __name__ == "__main__":
    main()