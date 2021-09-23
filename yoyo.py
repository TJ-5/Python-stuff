class automat:
    kartentheather = 400
    preistheater = 3
    Karteauswahl = "Karten: \n Theater \n Abiball "
    error1 = "Falsch geschrieben oder nichts geschrieben"
    
    #Kartenauswahl
    print(Karteauswahl)
    Wähler = input()
    if (Wähler == "Theater"):
        auswahl = Wähler
        print("Programm ausgeführt\n")
    else:
        print(error1)
        print(Karteauswahl)
        Wähler2 = input()
        if (Wähler2 == "Theater"):
            auswahl = Wähler
            print("Programm ausgeführt\n")

    #anzahl an Karten wird bestimmt
    print("Wie viele Karten willst du kaufen?")
    Wähler3 = int(input())
    kartentheater = kartentheather-Wähler3
    #preis wird berechnet
    intpreis = preistheater*Wähler3
    print("Du musst " + str(intpreis), "€ bezahlen\n")
    
    geldeingabe = 0
    while geldeingabe != intpreis:
        geldeingabe = 0
        geldeingabe = int(input())
        rest = intpreis-geldeingabe
        if(geldeingabe !=intpreis):
            print("Du musst noch", str(rest),  "€ bezahlten")
        
    print("Es sind noch " + str(kartentheater) + " Karten verfügbar")

