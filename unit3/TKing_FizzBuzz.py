inp = input("Enter a number:")
int =  int(inp)#int stands for making the input an integer3
for x in (range(1,int + 1)):
    if (x % 3 == 0 and x % 5 == 0):
        print("FizzBuzz")
    elif  ( x % 3 == 0 ):
        print("Fizz")
    elif ((x % 5) == 0):
        print("Buzz")
    else:
        print(x)
