def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! ไม่สามารถหารด้วยศูนย์ได้"
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
                num1 = float(input("กรอกตัวเลขที่ 1: "))
                num2 = float(input("กรอกตัวเลขที่ 2: "))
            except ValueError:
                print("ข้อผิดพลาด: กรุณากรอกตัวเลขเท่านั้น!")
                continue

            if choice == "1":
                print(f"ผลลัพธ์: {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"ผลลัพธ์: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"ผลลัพธ์: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"ผลลัพธ์: {num1} / {num2} = {result}")
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกเมนู 1-5 เท่านั้น")


# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    calculator()