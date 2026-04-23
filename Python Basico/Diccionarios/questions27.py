list_a = ["first_name", "last_name", "role"] 
list_b = ["Alek", "Castillo", "Software Engineer"] 

data = {}

for index,key in enumerate(list_a):
    data[key]=list_b[index]
    
print(data)