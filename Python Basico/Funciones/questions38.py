
my_string = "python-variable-funcion-computadora-monitor"

def reordered_words(string):    
    new_list=sorted(string.split("-"))    
    return "-".join(new_list)

print(reordered_words(my_string))