class Calculator(object):
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b

def main():
    # Read inputs and validate as numbers
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input: Please enter numeric values.")
        return

    operation = input("Enter operation (+, -, *, /): ").strip()

    calculator = Calculator()

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation: Please enter one of +, -, *, /.")
        return

    if operation == '+':
        result = calculator.add(a, b)
    elif operation == '-':
        result = calculator.subtract(a, b)
    elif operation == '*':
        result = calculator.multiply(a, b)
    elif operation == '/':
        if b == 0:
            result = "Error: Division by zero."
        else:
            result = calculator.divide(a, b)

    print(result)


if __name__ == '__main__':
    main()

