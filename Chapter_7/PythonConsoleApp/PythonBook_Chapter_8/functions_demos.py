
def calling_functions():

    musician = build_person('jimi', 'hendrix')
    print(musician)

    musicians = build_list_of_objects('jimi', 'hendrix',10)
    print(musicians)

    #
    usernames = ['hannah', 'ty', 'margot']
    greet_users(usernames)


def calling_functions_list():
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    print_models(unprinted_designs[:] , completed_models)
    show_completed_models(completed_models)
    print(">> Print uncompleted list...")
    show_completed_models(unprinted_designs)



def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


 

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

def build_list_of_objects(first_name, last_name, size):
    """Return a dictionary of information about a person."""
    results = []
    for index in range(1,size):
        person = {'first': f"{first_name} {index}", 'last': f"{last_name} {index}"}
        results.append(person)
    return results



def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


def print_models(unprinted_designs, completed_models):
    """ Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    if not completed_models:
       return 

    print("\n>> The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    print("\n-------------------------------------")