

woerter = {}
fobj = open("woerterbuch.txt", "r")
for line in fobj:
    zuordnung = line.split(" ")
    woerter[zuordnung[0]] = zuordnung[1]
fobj.close()



file = open("woerterbuch.txt", "r")
for line in file:
    zuordnung = line.split(" ")
    print(zuordnung[0].strip(), zuordnung[1].strip())
file.close()


v1 = 1337
print(v1)

liste = [4,6,2,1,8,5,9]
liste.append("data")
print(liste)