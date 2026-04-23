import random
secret = random.randint(1, 10)
print(f"Secret: {secret}")
number = 0
while(number != secret):
    number = int(input("Indica un número del 1 al 10 "))