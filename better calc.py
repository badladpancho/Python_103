#       this is going to be a better calc
#       this is going to be able to do the basics add,sub,multilpy,divide
#       user will enter number and operation
#       if operation is not valid then error will occur

num1 = float(input("Enter the first number\n"));
op = input("Enter operator:")
num2 = float(input("Enter the second number\n"));
if op == "+":
    print(num1 + num2);
elif op == "-":
    print(num1 - num2);
elif op == "*":
    print(num1 * num2);
elif op == "/":
    print(num1 / num2);
else:
    print("Error operation");