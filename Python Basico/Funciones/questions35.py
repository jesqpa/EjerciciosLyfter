numbers_list = [4, 6, 2, 29, 25]

def sum_numbers_list(list):
    summation = 0
    for number in list:
        summation = summation + number
    return summation

summation = sum_numbers_list(numbers_list)

print(f"Sumatoria de {numbers_list} = {summation}")
