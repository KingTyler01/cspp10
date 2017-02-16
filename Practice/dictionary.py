from pprint import pprint

d = {
    "name":"King",
    "birthyear":"Decemeber",
    "grade":10,
    "A": "Chemistry",
    "B": "Algebra II",
    "F/Grey" : "Weight Room",
    "F/Red": "Health",
    "C" : "English",
    "D": "Global",
    "E": "Global"
}
pprint(d[input("Schedule : ")])