inp = input("Enter a number:")
i =  int(inp)
for x in (range(1,i + 1)):
    if (x % 3 == 0 and x % 5 == 0):
        print("FizzBuzz")
    elif  ( x % 3 == 0 ):
        print("Fizz")
    elif ((x % 5) == 0):
        print("Buzz")
    else:
        print(x)
