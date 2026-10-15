class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_value(self) -> float:        
        return self.price * self.quantity
    
    def __str__(self) -> str:
        return f"- {self.name:<15} | Precio: ${self.price:>6.2f} | Cantidad: {self.quantity:>3} | Subtotal: ${self.get_value():>8.2f}"


class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)        

    def show_products(self):     
        for product in self.products:
            print(product)        

    def calculate_total_value(self) -> float:
        total = sum(product.get_value() for product in self.products)
        return total


def main():
    
    mi_inventario = Inventory()

    
    p1 = Product("Laptop", 1200.50, 5)
    p2 = Product("Mouse", 25.00, 15)
    p3 = Product("Teclado", 85.99, 8)
    
    mi_inventario.add_product(p1)
    mi_inventario.add_product(p2)
    mi_inventario.add_product(p3)
    
    mi_inventario.show_products() 
    
    valor_total = mi_inventario.calculate_total_value()
    print(f"Valor total del inventario: ${valor_total:,.2f}\n")


if __name__ == "__main__":
    main()