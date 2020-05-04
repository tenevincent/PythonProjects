
def calling_dog_main():
    my_dog = Dog('willie', 6)
    your_dog = Dog('lucy', 3)

    print("My dog's name is " + my_dog.name.title() + ".")
    print("My dog is " + str(my_dog.age) + " years old.")
    my_dog.sit()

    print("\nMy dog's name is " + your_dog.name.title() + ".")
    print("My dog is " + str(your_dog.age) + " years old.")
    your_dog.sit()

    # test auf identity
    dog1 = Dog("Hund",5)
    dog2 = Dog("Hund",5)
    # 
    print(f"Are objects equals: {dog1 == dog2}")
    identity01 = id(dog1)
    identity02 = id(dog2)
    print(f"Are objects identical: {identity01 == identity02}")


class Dog(object):
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
 
    def __str__(self):
        """Initialize name and age attributes."""
        return f"{self.name} {self.age}"

    def __eq__(self, value):
        return self.name.__eq__(value.name) and self.age.__eq__(value.age)




