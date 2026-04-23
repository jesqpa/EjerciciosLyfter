my_list = [9, 4, 7, 1, 5] 
minimum = 10

print(my_list)

for number in my_list:
    if(number<minimum):
        minimum=number

print(f"El menor valor es {minimum}")
