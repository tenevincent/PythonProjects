

def input_to_integers():
    age = input("How old are you? ")
    ageplus = int(age) +1
    print(f"Increased age: {ageplus}")

    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1


def while_demo():
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
        print(pets)
