
    
print("Choose an operation:")
print("1 for Addition (+)")
print("2 for Subtraction (-)")
print("3 for Multiplication (*)")
print("4 for Division (/)")

 
        
operation = input("Enter the number of the operation which you want to perform 1/2/3/4: ")

if operation not in ['1', '2', '3', '4']:
 print("Invalid number. Please select a valid no for operation.")
            

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if operation == "1":
    result = num1 + num2
    print(f"The result of addition: {num1} + {num2} = {result}")


elif operation == "2":
    result = num1 - num2
    print(f"The result of subtraction: {num1} - {num2} = {result}")


elif operation == "3":
    result = num1 * num2
    print(f"The result of multiplication: {num1} * {num2} = {result}")


elif operation == "4":
    if num2 == 0:
     print("error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print(f"The result of division: {num1} / {num2} = {result}")

