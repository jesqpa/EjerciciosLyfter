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
    list = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:")
    print(list)
    list = bubble_sort(list)
    print("Lista ordenada:")
    print(list)

if __name__ == "__main__":
    main()