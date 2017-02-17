from pprint import pprint
choice = input("[Add]key-value\n[Remove]key-value\n[Update]key-value\n[Exit]\n:")
d = {}
def add(choice,d):
    if choice == "add" or choice == "Add":
        check = input("What new key would you like to add to the dictionary?: ")
        if check in d:
            print("Invalid. Input a new key into the dictionary: ")
            print(check)
        else:
            d[check] = input("What is the value of this key?: ")
            pprint(d)
            
def remove(choice,d):
    if choice == "remove" or choice =="Remove":
        remove = input("What new key would you like to remove from the dictionary?: ")
        del d[remove]
        pprint(d)

def update(choice,d ):
    if choice == "Update" or choice == "update":
        check = input ("What key do you want to add to the list?: ")
        value = input ("What value do you want the key to have?: ")
   
    if choice not in d:
        d[check] = value
        pprint(d)
        
def Exit(choice,d):
    if choice == "Exit" or "exit":
        print("The End")

        
        
    
        

Exit(choice,d)