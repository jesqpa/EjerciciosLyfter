from datetime import datetime


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = datetime.now()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )
    
    @staticmethod
    def check_adult_age(func):
        """Decorator that validates if the User is of legal age"""
        def wrapper(user):
            if user.age < 18:
                raise ValueError(f"{user.name} debe ser mayor de 18 años. Edad actual: {user.age}")
            return func(user)
        return wrapper
    
    @staticmethod
    @check_adult_age
    def enter_bar(user):
        return f"{user.name} puede entrar al bar (edad: {user.age})"
    
    @staticmethod
    @check_adult_age
    def vote(user):
        return f"{user.name} puede votar (edad: {user.age})"


def main():
    user1 = User("Carlos", datetime(2000, 5, 15))
    user2 = User("Andrea", datetime(2010, 3, 20))
    
    # Legal age user
    print(User.enter_bar(user1))
    print(User.vote(user1))
    
    # Minor user
    try:
        print(User.enter_bar(user2))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()