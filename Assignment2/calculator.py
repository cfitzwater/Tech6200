
def main():
    print("Welcome to the Simple Calculator!")
    
    # Prompt for first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Prompt for operation
    while True:
        op = input("Enter an operation (+, -, *, /): ").strip()
        if op in ['+', '-', '*', '/']:
            break
        else:
            print("Please enter a valid operation: +, -, *, or /.")
    
    # Prompt for second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Perform calculation with error handling for division by zero
    try:
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        print(f"{num1} {op} {num2} = {result}")
    
    except ZeroDivisionError as e:
        print(f"Error: {e} Please try again with a non-zero second number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
    