class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

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
        if value <= 0:
            raise ValueError("El salario no puede ser cero o negativo")
        self._salary = value

    def promote(self):
        """Solicita y valida un porcentaje de aumento, luego aplica el aumento al salario"""
        while True:
            try:
                percentage = float(input("Ingrese el porcentaje de aumento para la promoción (0.0-1.0): "))
                if percentage < 0 or percentage > 1:
                    raise ValueError("El porcentaje debe ser un valor entre 0 y 1")
                increase = self._salary * percentage
                self._salary += increase
                break
            except ValueError as e:
                print(f"Error: {e}")


def main():
    while True:
        try:
            salary = float(input("Ingrese el salario inicial del empleado: "))
            name = input("Ingrese el nombre del empleado: ")
            employee = Employee(name, salary)
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    print(f"Nombre: {employee.name}")
    print(f"Salario inicial: ${employee.salary:.2f}")
    
    employee.promote()
    print(f"Salario después de promoción: ${employee.salary:.2f}")
        
    


if __name__ == "__main__":
    main()