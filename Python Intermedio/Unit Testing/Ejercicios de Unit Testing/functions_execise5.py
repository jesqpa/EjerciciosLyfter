
my_string = "Pizza con piña" 

def invert_string(string):
    inverted_string = ""
    for letter in range(len(string)-1,-1,-1):
        inverted_string = inverted_string + string[letter]
    return inverted_string

print(f"'{my_string}' invertido es '{invert_string(my_string)}'")