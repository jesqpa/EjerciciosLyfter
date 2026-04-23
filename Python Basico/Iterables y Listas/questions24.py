my_list = [10, 20, 30, 40, 50] 
summation = 0
print(my_list)
for number in my_list:
    summation = summation + number

average = summation / len(my_list)

new_list = []

for number in my_list:
    if(number>average):
        new_list.append(number)

print(f"Promedio: {average}")
print(f"Nueva lista: {new_list}")
