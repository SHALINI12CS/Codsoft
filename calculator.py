def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        # Prompt the user for an operation choice
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            try:
                # Prompt the user for two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            
            # Perform calculation based on the choice
            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'
            
            # Display the result
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")
        
        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            break

    print("Thank you for using the calculator!")

# Run the main function
if __name__ == "__main__":
    main()
