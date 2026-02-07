print("Welcome")

try :
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    Activist = input("Enter Activist (* , / , + , -): ")
    if Activist == "*" :
        result = num1 * num2 
    elif Activist == "/" :
        result = num1 / num2 
    elif Activist == "+" :
        result =  num1 + num2
    elif Activist == "-" :
        result = num1 - num2 
    else : 
        print("Wrong operator")
except ValueError :
    print("Please enter a number!!!")
except ZeroDivisionError :
    print("Division by 0 is prohibited!!!")
else :
    print(f"Your answer : {result}")
finally :
    print("The calculator is finished.")
