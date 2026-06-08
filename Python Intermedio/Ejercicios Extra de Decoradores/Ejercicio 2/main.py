
user_logged_in = False


class RequiresLogin:
    """Decorator class that verifies if user is logged in"""
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):        
        if not user_logged_in:
            raise ValueError("Usuario no autenticado")
        return self.func(*args, **kwargs)


@RequiresLogin
def view_profile(username):
    return f"Perfil de {username}"


def main():
    global user_logged_in
    
    # Without login
    try:
        print(view_profile("Carlos"))
    except ValueError as e:
        print(f"Error: {e}")
    
    # With login
    user_logged_in = True
    
    print(view_profile("Carlos"))
    


if __name__ == "__main__":
    main()