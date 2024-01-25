def function_one():
    pass

def greet_user(username):
    """Display a sample greeting."""
    print(f"Hello!: {username.title()}")
greet_user(username="Aamir Ali")

#Passing Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a: {animal_type.title()}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(animal_type='cat', pet_name='Mano')

#Positional Arguments
def describe_pet(animal_type, pet_name:
    """Display information about a pet."""
    print(f"\nI have a: {animal_type.title()}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
#describe_pet(animal_type='cat', pet_name='Mano')
describe_pet("mano", 'cat')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a: {animal_type.title()}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_pet(pet_name='Mano', animal_type='cat')

#Default Value
def describe_pet(animal_type, pet_name, age=10):
    """Display information about a pet."""
    print(f"\nI have a: {animal_type.title()}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    print(f"her age is: {age}")
describe_pet(animal_type='cat', pet_name='Mano')

def describe_pet(animal_type, pet_name='Mano', age=10):
    """Display information about a pet."""
    print(f"\nI have a: {animal_type.title()}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    print(f"her age is: {age}")
describe_pet('cat')

def get_formatted_name(first_name, last_name):
    """Return a Full name Neatly formatted."""
    full_name=f"{first_name.title()} {last_name.title()}"
    return full_name
get_formatted_name('aamir', 'ali')


def get_formatted_name(first_name, last_name, age=27):
    """Return a Full name Neatly formatted."""
    full_name=f"{first_name.title()} {last_name.title()}"
    return full_name, age
musician, age=get_formatted_name('aamir', 'ali')
print(musician)
print(age)

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a Full name, neatly formatted."""
    # if middle_name:
    full_name=f"{first_name} {middle_name} {last_name}"
    # # else:
    #   full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('aamir', 'ali')
print(musician)
musician=get_formatted_name('aamir','bali', 'ali')
print(musician)


#Loop
def greet_users(names):
    """Print a simple to each user in this list."""
    for name in names:
        msg=f"Hello, {name.title()}!"
        print(msg)
username=['Ali', 'Aamir', 'Ahmed']
greet_users(username)

#passing an Arbitary number of Arguments
def greet_users(*names): #* print everything in the define function without any discrimination
    """Print the list of names that have been requested."""
    print(names)

greet_users('Ali', [], ())
greet_users('Ali', 'Aamir', 'Ahmed')

def greet_users(*names):
    """Print the list of names that have been requested."""
    for name in names:
        print(name)

greet_users('Ali', [], ())
greet_users('Ali', 'Aamir', 'Ahmed')

#using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):  #** pass an Argument
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

build_profile(
    'Aamir','Ali'    
)

build_profile(
    'Aamir','Ali',  
    location= 'karachi', field='DataScience'  
)

def arb_params(**kwargs):
    """Build a dictionary containing everything we know about a user."""
    print(kwargs)
arb_params(one='one')
arb_params(one='one', two=2)
arb_params(one='one', two=2, username='Aamir Ali')


def arb_params(**kwargs):
    if kwargs.get('username'):
        print('This is my username:', kwargs['username'])
    """Build a dictionary containing everything we know about a user."""
    print(kwargs)
arb_params(one='one', two=2)
arb_params(one='one', two=2, username='Aamir Ali')