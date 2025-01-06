#Dictionaries

# - Store key value pairs

#defining a dict
customer = {
    "name": "John Smith",
    "age": 39,
    "is_verified": False
}

print(customer["name"]) #printing

customer["birthdate"] = "Jan 3 200"


## CHALLENGE - Turn numbers into words
numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

phone = input("Phone: ")
output =""
for ch in phone: 
    output += numbers.get(ch, "!") + " "
    
print(output)

