class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def egress(self, amount: float):
        self.balance -= amount

    def income(self, amount: float):
        self.balance += amount
    
    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, min_balance: float, initial_balance: float = 0.0):
        super().__init__(initial_balance)
        self.min_balance = min_balance

    def egress(self, amount: float):
        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"Retiro denegado: El balance final ({self.balance - amount}) "
                f"quedaría por debajo del mínimo requerido ({self.min_balance})."
            )
        super().egress(amount)

    def making_egress(self):
        while True:
            try:
                print("\n¿Qué operación desea realizar?")
                print("1. Ingreso (Depositar)")
                print("2. Egreso (Retirar)")
                print("3. Consultar balance")
                print("4. Salir")
                opcion = input("Seleccione una opción (1, 2, 3 o 4): >> ").strip().lower()

                if opcion in ('4', 'salir'):
                    print("Cerrando sesión. ¡Hasta luego!")
                    break
                elif opcion in ('1', 'ingreso', 'depositar'):
                    amount = float(input("Ingrese monto a depositar: >> "))
                    self.income(amount)
                    print(f"*** Ingreso exitoso. Balance actual: {self.get_balance()}")
                elif opcion in ('2', 'egreso', 'retirar'):
                    amount = float(input("Ingrese monto a retirar: >> "))
                    self.egress(amount)
                    print(f"*** Egreso exitoso. Balance actual: {self.get_balance()}")
                elif opcion == '3':
                    print(f"*** Balance actual: {self.get_balance()} - Balance minimo: {self.min_balance}")
                else:
                    print("*** Opción no válida. Por favor, intente de nuevo.")
            
            except ValueError as e:
                print(f"*** Error: {e}")
            
            except Exception as e:
                print(f"*** Error: {e}")


    @staticmethod
    def request_min_balance():
        while True:
            try:        
                min_balance = float(input("Indique el monto de balance minimo: >> "))
                return min_balance
            except ValueError:
                print("*** Error: Monto no válido.")    


def main():
    account = BankAccount()
    print(f"*** Balance de BankAccount: {account.get_balance()}") 
    min_balance = SavingsAccount.request_min_balance()
    savings = SavingsAccount(min_balance, account.get_balance())
    savings.making_egress()


if __name__ == "__main__":
    main()