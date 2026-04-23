my_list = []
maximum = 0

for index in range(10):
    number=int(input("Indique un numero: "))
    my_list.append(number)
    if(number>maximum):
        maximum=number

print(f"{my_list}. El más alto fue: {maximum}")