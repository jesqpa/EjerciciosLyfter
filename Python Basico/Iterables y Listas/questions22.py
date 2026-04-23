my_list = [3, 6, 0, -2, 4] 
no_positives = 0
print(my_list)
for number in my_list:
    if(number<=0):
        no_positives = no_positives + 1

if(no_positives>0):
    print("Hay al menos un número negativo o cero")
else:
    print("Solo hay números positivos.")
