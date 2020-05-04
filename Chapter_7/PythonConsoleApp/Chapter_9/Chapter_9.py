<<<<<<< HEAD

import dog as dg


dg.calling_dog_main()

dog = dg.Dog("Medor",21)
# dog._age = 1

print(dog)

print(dog)




from person import person

p1=person("daa")
p1.name="Steve"

del p1.name
=======
from Car import * 
from electric_car import ElectricCar
from dog import Dog



car = Car('Ford', "Focus",2020)
name = car.get_descriptive_name()


car.update_odometer(100)
print(name)
car.read_odometer()

# 
my_new_car = Car('audi', 'a4', 2015)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


#
my_beetle = Car('volkswagen', 'beetle', 2015)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2015)
print(my_tesla.get_descriptive_name())


# dog

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nMy dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

>>>>>>> 1afcaf9b60f7516456f74688776579f4badaa836
