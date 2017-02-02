numbers = []
choice = 1
while choice != 0:
    choice = int(input ("Enter a number: "))
    numbers.insert(0,choice)
    if choice == 0:
        break
    if choice < 0:
        if (choice * -1) in numbers:
            numbers.remove(choice * -1)
            numbers.remove(choice)
        else:
            break
    print(numbers)