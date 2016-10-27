num = input("Enter a number:")
word= input("Enter a noun:")
space = " "
if num == "1":
    print (num + space + word)
elif num > "1" or num < "1":
    if word[-2:] == "fe":
        word2 = word[:-2]
        ves = "ves"
        print(num + space + word2 + ves)
    elif word[-2:] == "sh" or "ch":
        es="es"
        print(num + space + word + es)
    elif word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] =="uy" or word[-2:] == "ey":
        s = "s"
        print( num + space + word + s)
    