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

