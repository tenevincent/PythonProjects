

thistuple = ("apple", "banana", "cherry")
print(thistuple)

elem = thistuple[0]
print(elem)

# print the tuple elements
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

for x in thistuple:
  print(x)

  """ Dies ist ein Blockkommentar,
  er kann sich über mehrere Zeilen erstrecken. """


x = 1
if x == 1:
  print("x hat den Wert 1")
elif x == 2:
  print("x hat den Wert 2")
else:
  print("Nothing to say")

if x < 1 or x > 5:
  print("x ist kleiner als 1 ...")
  print("... oder größer als 5")

class Employee(object):
    pass

data = Employee()
if data:
   print("Data must be printed")
else:
   print("Nothing to be printed...")


for i in range(0, 20, 2):
   print(i)


