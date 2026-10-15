# Mixin de autenticación
class AuthMixin:
    def login(self, username, password):
        if username == self.username and password == self.password:
            self.log("Login exitoso")
            return True
        else:
            self.log("Login fallido")
            return False


# Mixin de logging
class LoggerMixin:
    def log(self, mensaje):
        print(f"[LOG - {self.username}]: {mensaje}")


# Mixin de base de datos
class DatabaseMixin:
    def save(self):
        print(f"Guardando usuario '{self.username}' en la base de datos...")


# Clase principal con herencia múltiple
class User(AuthMixin, LoggerMixin, DatabaseMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        self.save()  # viene de DatabaseMixin
        self.log("Usuario registrado")  # viene de LoggerMixin


def main():
    
    user = User("jonathan", "1234")

    # Registrar usuario
    user.register()

    # Intentar login
    user.login("jonathan", "1234")
    user.login("jonathan", "wrong")
    

if __name__ == "__main__":
    main()