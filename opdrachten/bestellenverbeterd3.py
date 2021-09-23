i = 1
bakje = False
print("Welkom bij Papi Gelato.")
def bonnetje():
    print("---------['Papi Gelato']---------")
    prijs = round(bolletjes * 1.09, 2)
    print(f"bolletjes        {bolletjes}  x 1,09 =    {prijs}  ")
    if bakje:
        print(f"bakje            1  x 0,75 =    €0,75")
        print("                                ------+")
        print(f"Totaal:                         {prijs + 0.75}")
    else:
        print(f"hoorntje         1  x 1,25 =    €1,25")
        print("                                ------+")
        print(f"Totaal:                         {round(prijs + 1.25, 2)}")

def opnieuwBestellen():
    keuze3 = input(f"wilt u nogmeer bestellen?\n".lower())
    if keuze3 == "ja":
        overnieuw()
    elif keuze3 == "nee":
        print("bedankt voor uw bestelling, tot ziens!")
        exit()
    else:
        print("sorry ik heb u niet kunnen begrijpen!")
        opnieuwBestellen()

def overnieuw():
    global bolletjes
    bolletjes = int(input("hoeveel bolletjes wilt u?\n"))
    for i in range(bolletjes):
        i += 1
        keuzebolletje = input(f"welke smaak wilt u bolletje nummer {i} hebben? a) Aardbei, b) Chocolade c) Munt of d) Vanillie.\n")
        smaken = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
        if not smaken.__contains__(keuzebolletje):
            print("dat is geen smaak")
            overnieuw()

    if 0 < bolletjes < 9:
        if bolletjes < 4:
            def overnieuwVragen():
                keuze2 = input(f"wilt u deze {bolletjes} bolletjes in een bakje of een hoorntje?\n".lower())
                if keuze2 == "bakje":
                    print(f"Oke dan krijgt u van mij een bakje met {bolletjes} bolletjes!")
                    global bakje
                    bakje = True
                    bonnetje()
                    bakje = False
                    opnieuwBestellen()
                elif keuze2 == 'hoorntje':
                    print(f"Oke dan krijgt u van mij een hoorntje met {bolletjes} bolletjes!")
                    bonnetje()
                    opnieuwBestellen()
                else:
                    print("sorry ik heb u niet goed kunnen verstaan")
                    overnieuwVragen()

            overnieuwVragen()
        else:
            print(f"Oke dan krijgt u van mij een bakje met {bolletjes} bolletjes!")
            bonnetje()
            bakje = True
            opnieuwBestellen()
    elif bolletjes >= 0:
        print("Sorry, zoveel bolletjes kunt u niet bestellen!")
        overnieuw()
    else:
        print("sorry dat snap ik niet.")
        overnieuw()


overnieuw()
