
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    result_add = calc.add(5, 3)
    result_subtract = calc.subtract(8, 2)
    result_multiply = calc.multiply(4, 6)
    result_divide = calc.divide(9, 3)

    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")
    print(f"Multiplication: {result_multiply}")
    print(f"Division: {result_divide}")
    print("Conflict?")