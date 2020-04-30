# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:40:01 2020

@author: Tene
"""



cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
     print(car.upper())
  else:
     print(car.lower())
     
     
game_active = True
can_edit = False
 
    
age = 19
if age >= 18:
   print("You are old enough to vote!")
   print("Have you registered to vote yet?")
