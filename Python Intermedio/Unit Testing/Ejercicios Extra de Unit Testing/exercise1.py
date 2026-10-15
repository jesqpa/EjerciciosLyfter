class NumberOperations:
    def __init__(self, values):
        self.values = values

    def sum_values(self):
        total = 0
        for value in self.values:
            total += value
        return total

    def average_values(self):
        if not self.values:
            raise ValueError("The list cannot be empty")
        return self.sum_values() / len(self.values)

    def multiply_values(self):
        result = 1
        for value in self.values:
            result *= value
        return result
