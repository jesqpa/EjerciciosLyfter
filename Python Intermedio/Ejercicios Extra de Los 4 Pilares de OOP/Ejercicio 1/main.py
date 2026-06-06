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
    # Crear un empleado
    employee = Employee("Juan", 3000)
    
    print(f"Nombre: {employee.name}")
    print(f"Salario inicial: ${employee.salary:.2f}")
    
    # Promover con un aumento del 10%
    employee.promote(10)
    print(f"Salario después de promoción (10%): ${employee.salary:.2f}")
    
    # Cambiar nombre
    employee.name = "Juan Pérez"
    print(f"Nuevo nombre: {employee.name}")
    
    # Cambiar salario directamente
    employee.salary = 4000
    print(f"Salario actualizado: ${employee.salary:.2f}")
    
    # Intentar establecer un salario negativo (esto causará un error)
    try:
        employee.salary = -1000
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()