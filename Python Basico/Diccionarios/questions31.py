products = [ 
    {"name": "Monitor", "category": "Electrónica", "price": 200}, 
    {"name": "Teclado", "category": "Electrónica", "price": 50}, 
    {"name": "Silla", "category": "Muebles", "price": 120}, 
    {"name": "Mesa", "category": "Muebles", "price": 180}, 
    {"name": "Mouse", "category": "Electrónica", "price": 25}, 
] 

categories = {}
for product in products:      
    category = product.get("category")
    price = product.get("price")

    if category not in categories:
        categories[category] = 0

    categories[category] = categories[category] + price

print(categories)

