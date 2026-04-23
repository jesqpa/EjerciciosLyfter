summation = 0
is30 = False

for cant in range(3):
    value = int(input("Indica un número: "))
    summation = summation + value
    if(value==30):
        is30 = True
    
if(is30 or summation==30):
    print("Correcto")
else :
    print("Incorrecto")