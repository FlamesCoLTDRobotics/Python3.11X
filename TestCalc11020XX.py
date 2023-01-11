## write a calculator pemdas
print("Welcome to the Calculator")
print("Please enter the first number")
num1 = input()
print("Please enter the second number")
num2 = input()
print("Please enter the operator")
op = input()
if op == "+":
    print(int(num1) + int(num2))
elif op == "-":
    print(int(num1) - int(num2))
elif op == "*":
    print(int(num1) * int(num2))
elif op == "/":
    print(int(num1) / int(num2))
else:
    print("Invalid Operator")
        