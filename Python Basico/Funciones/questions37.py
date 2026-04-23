
my_string = "Pizza Con Piña" 

def get_upper_and_lower_case_letters(string):
    uppercase_letters = 0
    lowercase_letters = 0
    for number in range(len(string)):
        letter= string[number] 
        if(letter.isupper()):
            uppercase_letters += 1
        elif(letter.islower()):
            lowercase_letters += 1
    return {"uppercase":uppercase_letters,"lowercase":lowercase_letters}

upper_and_lower_case_letters = get_upper_and_lower_case_letters(my_string)
print(f"'{my_string}' tiene {upper_and_lower_case_letters["uppercase"]} mayúsculas y {upper_and_lower_case_letters["lowercase"]} minúsculas")