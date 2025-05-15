numbers = input("Enter numbers (separated by space): ")
numbers = numbers.split()
numbers = [float(n) for n in numbers]

operator = input("Enter operation (+, -, *, /): ")

result = numbers[0]

for n in numbers[1:]:
    if operator == "+":
        result += n
    elif operator == "-":
        result -= n
    elif operator == "*":
        result *= n
    elif operator == "/":
        if n == 0:
            result = "Error"
            result /= n
        else:
            result /= n
    else:
        print("Invalid operator!")
        result = "Error"

print("Result:", result)