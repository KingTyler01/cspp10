E = input("Enter a three digit equation such as 4+5: ")
num1 = int(E[0])
op = E[1]
num2 = int(E[2])
if op == "+":
    num3 = num1 + num2
    print("The result is {}.".format(num3))
elif op == "-":
    num3 = num1 - num2
    print("The result is {}.".format(num3))
elif op == "*":
    num3 = num1 * num2
    print("The result is {}.".format(num3))
elif op == "/":
    num3 = num1 / num2
    print("The result is {}.".format(num3))
elif op == "%":
    num3 = num1 % num2
    print("The result is {}.".format(num3))
    
