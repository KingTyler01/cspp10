import random
ending_number = input("Enter the number for the end of the range:")
print ("The number is between 1 and {}.".format(ending_number))
answer = random.randint(1, int(ending_number))
number_of_guess = 0
guess = 0
while guess != answer:
    number_of_guess = number_of_guess + 1
    guess = int(input("Guess a number: "))
    if guess > answer:
        print("Too high, Try again")
    elif guess < answer:
        print("Too low, Try again")
print("You are correct!! It took you {} tries.".format(number_of_guess))