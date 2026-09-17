n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

cal = input("Enter option: ")

match cal:
    case "add":
        print("Addition:", n1 + n2)
    case "sub":
        print("Subtraction:", n1 - n2)
    case "mul":
        print("Multiplication:", n1 * n2)
    case "div":
        print("Division:", n1 / n2)
    case _:
        print("Invalid option")