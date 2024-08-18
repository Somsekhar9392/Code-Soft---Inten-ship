while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting...")
        break
    
    choice = int(choice)

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero")
            continue

    print("Result:", result)
    print()
    
print("Thank you for using the calculator!")
