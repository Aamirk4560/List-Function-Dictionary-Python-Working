dictionary = {'one': 1, "two":2, "three":3}
print(dictionary['two'])

alien_0= {"color":"green", "points":5}
print(alien_0['color'])
print(alien_0["points"])

#Accessing Dictionaries
alien_0= {
    "color":"green", 
    "points":5
    }
alien_0['color']
alien_0.get("color")

alien_0['color_1']         #return key error
alien_0.get("color_1")   #return null

#Example
# Dictionary is muttalble and dynamic
alien_0= {"color":"green", "points":5}
alien_0['color']= "red"
print(alien_0)

#EXAMPLE
alien_0['color_1']= "Blue"
print(alien_0)

#Addition new key-value pairs
alien_0.update({"key1":"value1", "key2":"value2"})
print(alien_0)

alien_0 = dict()
print(alien_0)
alien_0.update({"key1":"value1", "key2":"value2"})
print(alien_0)

#Conditional Test
alien_0 = {"color": "green", "points": 5, "speed": "medium"}

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0['speed'] == "medium":
    x_increment = 2
else:
    x_increment = 3

print(x_increment)

# New position is the old position plus the increment
alien_0["points"] = alien_0["points"] + x_increment
print(f'New Position: {alien_0["points"]}')  # Corrected the key "points"

#Removal of the value 
alien_0={"color": "green", "points": 5}
print(alien_0)
print(alien_0["points"])
del alien_0["points"]
print(alien_0)

fav_language={
    "ali": "python",
    "ahmed": "c",
    "zain": "java"
}
language=fav_language["ahmed"].title()
print(f'ahmed interedted in {language}.')

#Loop
for item in fav_language.keys():
    print(item)

for item in fav_language.values():
    print(item)

for item in fav_language.items():
    print(item)

for key,value in fav_language.items():
    print(key, value)

#A List in a Dictionary
pizza = {
    "crust": "thick",
    "toppings": ['mushroom', 'Extra cheese']
}
#Summerize the Order
print(f'You Ordered a {pizza["crust"]}--crust pizza ""with the following toppings')
for topping in pizza["toppings"]:
    print("\t" + topping)

#example
fav_language={
    "ali": "python",
    "ahmed": "c",
    "zain": ["java", "go"],
    "Zia": ["python", "Hadoop"]
}
for name, languages in fav_language.items():
    print(f'\n{name.title()} faverite languages are: ')
    for language in languages:
         print(f"\t{language.title()}")

#Dictionary in Dictionary
users = {
    'first': "albert",
    'second': 'Ali',
    'Location': 'Karachi',
},  # This comma shouldn't be here

mcurie = {
    'first': 'marie',
    'Last': 'curie',
    "Location": 'Lahore'
}  # No comma needed here

for username, user_info in users.items():  # Use .items() to iterate over key-value pairs
    print(f'\nUsername: {username}')

    full_name = f"{user_info['first']} {user_info.get('Last', '')}"  # Corrected Last to last and used .get() method to handle missing key
    location = user_info['Location']
    print(f'\tFull Name: {full_name.title()}')  # Corrected full_name to Full Name
    print(f'\tLocation: {location.title()}')  # Added printing of location


#Example
users = {
    'first': {"first": "albert", "Location": "Karachi"},
    'second': {"first": "Ali", "Location": "Karachi"},
    'mcurie': {"first": "marie", "Last": "curie", "Location": "Lahore"}
}

for username, user_info in users.items():
    print(f'\nUsername: {username}')

    full_name = f"{user_info['first']} {user_info.get('Last', '')}"  
    location = user_info['Location']
    print(f'\tFull Name: {full_name.title()}')
    print(f'\tLocation: {location.title()}')

#Example
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'Extra cheese'],
    'user':{
        'name': 'Aamir Ali',
        'address': 'Karachi'
    }

}    

for key, value in pizza.items():
    if key == 'crust':
        print(f"Pizza crust: {value}")  # Use 'value' instead of pizza['crust']
    if key == 'toppings':
        for topping in value:
            print(f"Pizza Topping: {topping}")  # Use 'topping' instead of pizza["toppings"]
    if key == 'user':
        print(f"User name: {value['name']}")  # Use 'value['name']' instead of value["name"]
        print(f"User Address: {value['address']}")