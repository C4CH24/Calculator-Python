def calculator():
    print("🧮 Simple Python Calculator 🧮")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)\n")
    
    try:
        # Get user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        # Perform calculation
        if operation == '+':
            result = num1 + num2
            print(f"\n{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"\n{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("\nError: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"\n{num1} / {num2} = {result}")
        else:
            print("\nInvalid operation! Please use +, -, *, or /")
    
    except ValueError:
        print("\nError: Please enter valid numbers!")
    
    # Ask to continue
    while True:
        choice = input("\nCalculate again? (Y/N): ").upper()
        if choice == 'Y':
            print("\n" + "="*30 + "\n")
            calculator()
            break
        elif choice == 'N':
            print("\nThanks for using the calculator! Goodbye! 👋")
            break
        else:
            print("Please enter Y or N!")

# Start the calculator
calculator()