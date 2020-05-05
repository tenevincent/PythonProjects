

woerter = {}

def readfile():
    fileObj = open("woerterbuch.txt","r")
    for line in fileObj:
         line = line.strip()
         zuordnung = line.split(" ")
         woerter[zuordnung[0]] = zuordnung[1]
    fileObj.close()



def readFileWithAs():
    with open('woerterbuch.txt',"r") as file_object:
        for line in file_object:
            line = line.strip()
            zuordnung = line.split(" ")
            woerter[zuordnung[0]] = zuordnung[1]


def runReadFile():
    while True:
        wort = input("Geben Sie ein Wort ein: ")
        if wort in woerter:
            print("Das deutsche Wort lautet:", woerter[wort])
        else:
            print("Das Wort ist unbekannt")


filename = 'programming.txt'

def writeToFile():
    with open(filename, 'w') as fileObj:
        fileObj.write("I love programming.")
        fileObj.write("I love creating new games.")
        fileObj.write("I love creating new games.")
        fileObj.write("I love creating new games.")
        fileObj.write("I love creating new games.")


# append to a file
with open(filename, 'a') as fileObject:
    fileObject.write("New item added\n")
    fileObject.write("New item added\n")









