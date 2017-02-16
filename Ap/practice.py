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
# E = input("Enter a three digit equation such as 4+5: ")
# num1 = int(E[0])
# op = E[1]
# num2 = int(E[2])
# if op == "+":
#     num3 = num1 + num2
#     print("The result is {}.".format(num3))
# elif op == "-":
#     num3 = num1 - num2
#     print("The result is {}.".format(num3))
# elif op == "*":
#     num3 = num1 * num2
#     print("The result is {}.".format(num3))
# elif op == "/":
#     num3 = num1 / num2
#     print("The result is {}.".format(num3))
# elif op == "%":
#     num3 = num1 % num2
#     print("The result is {}.".format(num3))

# number_1 = int(input("Enter your first number: "))
# number_2 = int(input("Enter your second number: "))
# operation = input("""
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# """)
# if operation == "+":
#     print("{} + {} = ".format(number_1, number_2))
#     print(number_1 + number_2)

# elif operation == "-":
#     print("{} - {} = ".format(number_1, number_2))
#     print(number_1 - number_2)

# elif operation == "*":
#     print("{} * {} = ".format(number_1, number_2))
#     print(number_1 * number_2)

# elif operation == "/":
#     print("{} / {} = ".format(number_1, number_2))
#     print(number_1 / number_2)

# else:
#     print("You have not typed a valid operator, please run the program again.")
    
def calculator():
    operation = input("""
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
% for the remainder 
** for exponents
:""")
    
    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))
    
    if operation == "+":
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == "-":
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == "*":
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == "/":
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == "%":
        print("{} % {} = ".format(number_1, number_2))
        print(number_1 % number_2)
    elif operation == "**":
        print("{} ^ {} = ".format(number_1, number_2))
        print(number_1 ** number_2)

    else:
        print("You have not typed a valid operator, please run the program again.")
    
    
def play_again():
    again = input("""Do you want calculate something else[Y/N]
Please use Y for Yes and N for No:""")
    if again == "Y":
        calculator()
    elif again == "N":
        print("----------------------")
        print("Hope to see you again")
    
def main():
    calculator()
    play_again()
    calculator()
    play_again()
    calculator()
    play_again()
    calculator()
    play_again()
    
    
main()
    
    
    
    
    



