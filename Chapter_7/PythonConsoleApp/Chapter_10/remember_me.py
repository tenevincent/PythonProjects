import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    vorname = input("What is your vorname? ")
    age = input("What is your age? ")

    filename = 'username.json'
    with open(filename, 'w') as file:
        person = {'name': username, 'vorname': vorname, 'age': 43}     
        json.dump(person, file)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username['name'] + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
