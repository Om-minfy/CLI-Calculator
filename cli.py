print("Calculator")
num1 = float(input("Enter Number 1: "))
operator = input("Operator(+, -, *, /): ")
num2 = float(input("Enter Number 2: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        result = "Error"
    else:
        result = num1 / num2

else:
    result = "Invalid"

print("Result :", result)