from pprint import pprint
# d = {
#     "name":"King",
#     "birthyear":"Decemeber",
#     "grade":10,
#     "A period": "Chemistry",
#     "B period": "Algebra II",
#     "F/Grey" : "Weight Room",
#     "F/Red": "Health",
#     "C period" : "English",
#     "D period": "Global",
#     "E period": "Global"
# }
# for key in d:
#     print(d[key])
# pprint(d[input("Schedule period: ")])

def letsdoit():
    d = {}
    choose = input("[Add]key-value\n[Remove]key-value\n[Update]key-value\n[Exit]\n:")
    if choose == "add" or choose == "Add":
        d[input("What new key would you like to add to the dictionary?: ")] = input("What is the value of this key?: ")
        pprint(d)
        # add = str(input("What key would you like to add?: "))
        # add == add
        # result_add = str(input("What is the value of this key: "))
        # d[add] = result_add
        # pprint(d)
        
        
   
    # pprint(d)
    # pprint(d[input("Schedule : ")])
    
letsdoit()