def calculator():
    print("\nCalculator:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Choose operation: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid choice!")


def grade_computation():
    print("\nGrade Computation:")
    g1 = float(input("Enter grade 1: "))
    g2 = float(input("Enter grade 2: "))
    g3 = float(input("Enter grade 3: "))
    avg = (g1 + g2 + g3) / 3
    print("Average:", avg)
    if avg >= 60:
        print("Pass")
    else:
        print("Fail")


def temperature_converter():
    print("\nTemperature Converter:")
    print("a) Celsius to Fahrenheit")
    print("b) Fahrenheit to Celsius")
    print("c) Kelvin to Fahrenheit")
    print("d) Fahrenheit to Kelvin")
    print("e) Kelvin to Celsius")
    print("f) Celsius to Kelvin")
    choice = input("Choose conversion: ")

    if choice == 'a':
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5) + 32)
    elif choice == 'b':
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", (f - 32) * 5/9)
    elif choice == 'c':
        k = float(input("Enter Kelvin: "))
        print("Fahrenheit:", (k - 273.15) * 9/5 + 32)
    elif choice == 'd':
        f = float(input("Enter Fahrenheit: "))
        print("Kelvin:", (f - 32) * 5/9 + 273.15)
    elif choice == 'e':
        k = float(input("Enter Kelvin: "))
        print("Celsius:", k - 273.15)
    elif choice == 'f':
        c = float(input("Enter Celsius: "))
        print("Kelvin:", c + 273.15)
    else:
        print("Invalid choice!")


def number_operations():
    print("\nNumber Operations:")
    print("a) Check Even or Odd")
    print("b) Find Factorial")
    print("c) Check if Prime")
    choice = input("Choose operation: ")
    n = int(input("Enter a number: "))

    if choice == 'a':
        if n % 2 == 0:
            print(n, "is Even")
        else:
            print(n, "is Odd")
    elif choice == 'b':
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial:", fact)
    elif choice == 'c':
        if n < 2:
            print(n, "is not Prime")
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    print(n, "is not Prime")
                    break
            else:
                print(n, "is Prime")
    else:
        print("Invalid choice!")


def prompt_next_action():
    while True:
        choice = input("\nDo you want to go back to the main menu or exit the program? (menu/exit): ").lower()
        if choice == "menu":
            return True
        elif choice == "exit":
            print("Exiting program. Goodbye!")
            exit()
        else:
            print("Invalid choice! Please type 'menu' or 'exit'.")


def main():
    while True:
        print("\nMain Menu:")
        print("1. Calculator")
        print("2. Grade Computation")
        print("3. Temperature Converter")
        print("4. Number Operations")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            calculator()
            prompt_next_action()
        elif choice == '2':
            grade_computation()
            prompt_next_action()
        elif choice == '3':
            temperature_converter()
            prompt_next_action()
        elif choice == '4':
            number_operations()
            prompt_next_action()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()