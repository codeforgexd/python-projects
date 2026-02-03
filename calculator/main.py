print("Welcome to my calculator")

num1 = float(input("Enter number 1"))
num2 = float(input("Enter number 2"))

print("Choose one of these signs (* , / , + , -)")
sings = input("your choice:")

if sings == "*":
    result = num1 * num2
elif sings == "/":
    if num2 != 0 :
        result = num1 / num2
    else :
        result = "Error ! division by zero"
elif sings == "+":
    result = num1 + num2
elif sings == "-":
    result = num1 - num2
else :
    result = "invalid operation"

print(f"Result : {result}")
