def bubble_sort(values):
    if not isinstance(values, list):
        raise TypeError("bubble_sort expects a list")

    element_count = len(values)
    sorted_values = values[:]

    for i in range(element_count):
        for j in range(0, element_count - i - 1):
            if sorted_values[j] > sorted_values[j + 1]:
                temp = sorted_values[j]
                sorted_values[j] = sorted_values[j + 1]
                sorted_values[j + 1] = temp

    return sorted_values


def main():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:")
    print(numbers)
    sorted_numbers = bubble_sort(numbers)
    print("Sorted list:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()