import math

print("===== Python Calculator =====")

while True:
    print("\nChoose an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Modulus")
    print("6: Power")
    print("7: Square Root")
    print("8: Floor Division")
    print("9: Exit")

    try:
        choice = int(input("Enter your choice (1-9): "))
    except ValueError:
        print("Invalid input! Please enter a number (1-9).")
        continue

    if choice == 9:
        print("Thank you for using the calculator!")
        break

    # For square root, only 1 number is needed
    if choice == 7:
        try:
            num = float(input("Enter a number: "))
            print("Square root of", num, "is", math.sqrt(num))
        except ValueError:
            print("Error! Invalid number.")
        continue

    # For all other operations, two numbers needed
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered!")
        continue

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", a / b)
    elif choice == 5:
        print("Result:", a % b)
    elif choice == 6:
        print("Result:", a ** b)
    elif choice == 8:
        if b == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", a // b)
    else:
        print("Invalid choice! Please select 1–9.")