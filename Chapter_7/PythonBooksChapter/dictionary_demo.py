# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:57:47 2020

@author: Tene
"""


alien_0 = {'color': 'green', 'points': 5, 'IsColored': True}
print(alien_0['color'])
print(alien_0['points'])


alien_0['Age'] = 34
print(alien_0)

del alien_0['Age']
del alien_0['IsColored']


keys = alien_0.keys()
for key in keys:
   print("key is: %s" % key)

values = alien_0.values()
for value in values:
   print("value: %s" % value)
   
#empty dictinoary
aliens = {}
aliens['color'] = 'green'
aliens['points'] = 5
print(aliens)

alienAll = {'color': 'green', 'points': 5}
print(alienAll)
del alienAll['points']
print(alienAll)

alien = {'color': 'green', 'speed': 'slow'}
point_value = alien.get('points', "null")
print(point_value)

print(alien['speed'])

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
print(aliens)



