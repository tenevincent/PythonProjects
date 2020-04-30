# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:20:19 2020

@author: Tene
"""
 


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician)
  
  
magicians = ['alice', 'david', 'carolina', "Vincent"]
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

print('vincent' in magicians)

for value in range(1, 5):
    print(value)

squares = []
for value in range(1,11):
  squares.append(value**2)
  print(value)
  
print("The minimum is %s " % min(squares))
print("The maximum is %s " % max(squares))

#slicing a list...
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

#slicing a list...
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

