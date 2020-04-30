# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:16:10 2020

@author: Tene
"""
 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

bicycles.append("A new item is added!")
bicycles.append("Vincent")
bicycles.append("Tene!")
bicycles.append("A new item is added!")

bicycles.pop()
bicycles.sort()

contains = 'Tene!' in bicycles
print(contains)


print(bicycles)


print(bicycles[0])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

del motorcycles[0]

motorcycles.insert(0, 'ducati')
print(motorcycles)

# list sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#list sort reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)





