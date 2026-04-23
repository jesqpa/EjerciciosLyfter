price = int(input("Indica el precio: "))
discount = 0

if(price<100) : 
    discount = price * 2 / 100
else :
    discount = price * 10 / 100

print(f"El precio final es: {price-discount}")
