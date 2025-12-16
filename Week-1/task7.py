num1 = float(input("First number: "))
operation = input("Operation (+, -, *, /): ")
num2 = float(input("Second number: "))

result = (num1 / num2 if num2 != 0 else "Error: Division by zero!") if operation == "/" \
         else num1 + num2 if operation == "+" \
         else num1 - num2 if operation == "-" \
         else num1 * num2 if operation == "*" \
         else "Error: Unknown operation!"

print(f"{num1} {operation} {num2} = {result}")
