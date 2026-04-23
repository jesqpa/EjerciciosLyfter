
my_list = [4, 3, 6, 1, 7] 

print(my_list)

first = my_list[0]
last = my_list[len(my_list)-1]

my_list[0]=last
my_list[len(my_list)-1]=first

print(my_list)