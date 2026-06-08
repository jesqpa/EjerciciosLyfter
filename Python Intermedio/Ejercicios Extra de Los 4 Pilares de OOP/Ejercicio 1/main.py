class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = value

    def promote(self, percentage):
        """Aumenta el salario por un porcentaje definido"""
        if percentage < 0:
            raise ValueError("El porcentaje no puede ser negativo")
        increase = self._salary * (percentage / 100)
        self._salary += increase


def main():
    try:
        salary = float(input("Ingrese el salario inicial del empleado: "))

    except ValueError:
        print("Por favor, ingrese un número válido para el salario.")
        return
    
    try:
        name = input("Ingrese el nombre del empleado: ")
    except ValueError:
        print("Por favor, ingrese un nombre válido para el empleado.")
        return
    
    employee = Employee(name, salary)
    print(f"Nombre: {employee.name}")
    print(f"Salario inicial: ${employee.salary:.2f}")
    
    
    try:
        percentage = float(input("Ingrese el porcentaje de aumento para la promoción: "))
    except ValueError:
        print("Por favor, ingrese un número válido para el porcentaje.")
        return
    
    employee.promote(percentage)
    print(f"Salario después de promoción (10%): ${employee.salary:.2f}")
        
    


if __name__ == "__main__":
    main()