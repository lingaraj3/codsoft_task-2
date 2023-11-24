print("Enter 0 for addition ")
print("Enter 1 for subtraction ")
print("Enter 2 for multiplication ")
print("Enter 3 for division ")
while True:
    try:
        operation_choice = int(input("Enter 0/1/2/3 for operation"))
    except ValueError:
        print("Please enter valid input")
        continue
    else:
        if operation_choice >= 0 <= 3:
            break
        else:
            print("Choice should be less than 4")

if operation_choice == 0:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    print(f"Addition of two number is {num1 + num2}")
elif operation_choice == 1:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    print(f"Subtraction of two numbers is {num1 - num2}")
elif operation_choice == 2:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    print(f"multiplication  of two numbers is {num1 * num2}")
else:
    num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(f"Division of two numbers is {num1 / num2}")