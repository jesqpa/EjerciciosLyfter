def bubble_sort_right_to_left(list):
    element_count = len(list)
    for i in range(element_count):
        for j in range(element_count-1, i, -1):
            # print(f"Comparando {list[j]} y {list[j-1]}: {list}")
            if list[j] < list[j-1]:
                # Intercambiar usando la sintaxis de asignación múltiple (más eficiente en Python)                
                list[j], list[j-1] = list[j-1], list[j]
                # print(f"Intercambiando {list[j]} y {list[j-1]}: {list}")
    return list
    
    

def main():
 list = [64, 34, 25, 12, 22, 11, 90,265,14,68,35,48,9,5,1,0,64,19,82,46,73,2,55,27,31,17,29,3,2,4,6,7,8,10]
 print("Lista original:")
 print(list)
 list = bubble_sort_right_to_left(list)
 print("Lista ordenada:")
 print(list)

if __name__ == "__main__":
    main()