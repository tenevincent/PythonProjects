
import json

numbers = [2, 3, 5, 7, 11, 13]
person ={'name':'Vincent', 'vorname':'Tene', 'age':45}

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(person, file_object)


