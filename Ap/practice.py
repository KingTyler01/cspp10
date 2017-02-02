# x = ""
# y = ""
# z = ""
# def picking_op():
#     x = input("Enter a type of expression. [+], [-], [*], [/]: ")
#     return x
    
# def number1():
#     y = int(input("What number do you want to change based on your operation[Ex: 3]: "))
#     return y
# def number2():
#     z = int(input("Pick another number:"))
#     return z
    
# def result(x,y,z):
#     choice = print("You chose to {} the number {} and {}".format(x,y,z))
#     print(choice)
    
    
# def main():
#     picking_op()
#     number1()
#     number2()
#     result(x,y,z)
    

# main()
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
    

    
    
    
    
    



