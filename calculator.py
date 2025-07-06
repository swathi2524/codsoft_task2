def calculator():
    print("Simple Calculator")
    print("Available operations: + (add), - (subtract), * (multiply), / (divide)")

    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))

        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation.")
            return

        print(f"Result: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Error: Invalid input. Please enter numbers.")

# Run the calculator
calculator()
