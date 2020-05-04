

def break_demo():
    geheimnis = 9
    versuch = -1
    zaehler = 0

    while versuch != geheimnis:
        versuch = int(input("Raten Sie: "))

        if versuch == 0:
            print("Das Spiel wird beendet")
            break

        if versuch < geheimnis:
            print("Zu klein")
        if versuch > geheimnis:
            print("Zu groß")

        zaehler = zaehler + 1

    print("Sie haben es geschafft!")

def continue_demo():
    while True:
        zahl = int(input("Geben Sie eine Zahl ein: "))

        if zahl < 0:
            print("Negative Zahlen sind nicht erlaubt")
            continue

        ergebnis = 1
        while zahl > 0:
            ergebnis = ergebnis * zahl
            zahl = zahl - 1
        print("Ergebnis: ", ergebnis)

def else_demo():
    geheimnis = 9
    versuch = -1
    zaehler = 0

    while versuch != geheimnis:
        versuch = int(input("Raten Sie: "))

        if versuch == 0:
            print("Das Spiel wird beendet")
            break

        if versuch < geheimnis:
            print("Zu klein")
        if versuch > geheimnis:
            print("Zu groß")

        zaehler = zaehler + 1
    else:
        print("Sie haben es geschafft!")


break_demo()

