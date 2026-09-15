### version 1.2 (Thirawat Klawkla)
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! cant divide 0"
    return x / y


def calculator():
    while True:
        print("\n=== (Calculator) ===")
        print("1. add(+)")
        print("2. subtract(-)")
        print("3. multiply(*)")
        print("4. divide(/)")
        print("5. leave")

        choice = input(" (1-5): ")

        if choice == "5":
            print(".leave")
            break

        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("number wanna put 1: "))
                num2 = float(input("number wanna put 2: "))
            except ValueError:
                print("error: only put number!")
                continue

            if choice == "1":
                print(f"Addition : {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"Divisoin: {num1} / {num2} = {result}")
        else:
            print("Error only put calculator list only 1-5")


# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    calculator()