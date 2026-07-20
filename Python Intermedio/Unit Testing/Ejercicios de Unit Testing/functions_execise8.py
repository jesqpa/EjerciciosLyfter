
number_list = [1, 4, 6, 7, 13, 9, 67]

def is_prime_number(number):    
    dividers = 0
    if(number>=2):
        for num in range(number):
            divider=num+1            
            if(number%divider==0):  
                dividers += 1          
        if(dividers==2):
            return True
    else:
        return False    


def extract_prime_numbers(list):
    prime_list = []
    for number in list:        
        if(is_prime_number(number)):
            prime_list.append(number)
    return prime_list

print(number_list)
print(f"Solo estos son números primos: {extract_prime_numbers(number_list)}")