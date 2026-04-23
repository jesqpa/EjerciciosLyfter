"""my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11111,24,11,11,11,11,11]

new_list=[]
for index,number in enumerate(my_list) :
    if(number%2 != 1):        
        new_list.append(number)

print(new_list)