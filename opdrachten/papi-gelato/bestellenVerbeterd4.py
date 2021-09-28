print('Welkom bij Papi Gelato.')
bolletjes = 0
addedCost = 0
totalbolletjes = 0
totalbakjes = 0
totalhoorntje = 0
totaltoppings = 0
# --------------------particulier--------------------------#

def topping():
    global addedCost
    global totaltoppings
    totaltoppings += 1
    toppings = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?\n').lower()
    if toppings == 'a':
        addedCost += 0
    elif toppings == 'b':
        addedCost += 0.50
        # toppings = 'Slagroom'
    elif toppings == 'c':
        addedCost += (bolletjes * 0.30)
    elif toppings == "d":
        if soort == 'bakje':
            addedCost += 0.90
        elif soort == 'hoorntje':
            addedCost += 0.60
    else:
        print("Die topping hebben wij niet!")
        topping()


def bonnetje():
    total = 0
    total += totalbolletjes * 1.10
    print("---------['Papi Gelato']---------")
    print(f'bolletjes   {totalbolletjes} x 1,10   = {round(totalbolletjes * 1.10, 2)} €')
    if soort == 'bakje':
        print(f'bakje       {totalbakjes} x 0.75   = {round(totalbakjes * 0.75, 2)} €')
        total += (totalbakjes * 0.75)
    elif soort == 'hoorntje':
        print(f'hoorntje    {totalhoorntje} x 1.25   = {round(totalhoorntje * 1.25, 2)} €')
        total += (totalbakjes * 1.25)
    if addedCost > 0:
        print(f'Topping     {totaltoppings} x top    = {round(addedCost, 2)} €')
        total += addedCost
    print('                        -------- +')
    print(f'                        {round(total, 2)}€')


def wiltunogwat():
    nogwat = input('wilt u nog wat bestellen?\n')
    if nogwat == 'ja':
        hoeveelbollen()
        welkesmaken()
        hoorntjeofbakje()
    elif nogwat == 'nee':
        bonnetje()
        print('Bedankt voor uw aankoop,')
        print('Een fijne dag nog!')
        exit()
    else:
        print('Sorry ik kan u niet verstaan.')
        wiltunogwat()


def welkesmaken():
    global totalbolletjes
    totalbolletjes += bolletjes
    for i in range(bolletjes):
        try:
            smaak = int(input(f'Welke smaak wilt u voor bol nummer ({i + 1}) 1.Aardbei 2.Chocolade 3.Munt of 4.Vanille?\n'))
            if int(smaak) < 0 or int(smaak) > 4:
                print('Dat is geen smaak, we beginnen even overnieuw.')
                welkesmaken()

        except ValueError:
            print('Ik heb u niet goed verstaan, we beginnen weer even overnieuw.')
            welkesmaken()
            break


def hoeveelbollen():
    global bolletjes
    try:
        bolletjes = int(input('hoeveel bolletjes wil je?\n'))
    except ValueError:
        print('Ik heb u niet goed verstaan.')
        hoeveelbollen()
        return
    if bolletjes < 1 or bolletjes > 9:
        print('We hebben geen bakjes voor die hoeveelheid.')
        hoeveelbollen()


def hoorntjeofbakje():
    global soort
    global totalhoorntje
    global totalbakjes

    if bolletjes < 4:
        soort = input(f'Wilt u deze {bolletjes} bolletjes in een hoorntje of een bakje?\n'.lower())
        if soort == 'bakje' or soort == 'hoorntje':
            if soort == 'bakje':
                totalbakjes += 1
            else:
                totalhoorntje += 1
            topping()
            print(f'hier is uw {soort} met {bolletjes} bollen.')
            wiltunogwat()
        else:
            print("sorry ik heb u niet kunnen verstaan!")
            hoorntjeofbakje()
    else:
        soort = 'bakje'
        totalbakjes += 1
        topping()
        print(f'hier is uw {soort} met {bolletjes} bollen.')
        wiltunogwat()


# ----------------------Zakelijk-------------------------#

def hoeveelliters():
    global liters
    try:
        liters = int(input('hoeveel liters wilt u?\n'))
    except ValueError:
        print('Ik heb u niet goed verstaan.')
        hoeveelliters()
        return
    if liters < 1:
        print('We hebben geen bakjes voor die hoeveelheid.')
        hoeveelliters()


def welkesmakenliters():
    for l in range(liters):
        try:
            smaakliter = int(input(f'Welke smaak wilt u voor liter nummer ({l + 1}) 1.Aardbei 2.Chocolade 3.Munt of 4.Vanille?\n'))
            if int(smaakliter) < 0 or int(smaakliter) > 4:
                print('Dat is geen smaak, we beginnen even overnieuw.')
                welkesmakenliters()
        except ValueError:
            print('Ik heb u niet goed verstaan, we beginnen weer even overnieuw.')
            welkesmakenliters()
            break


def bonnetjezakelijk():
    totaal = round(liters * 9.80, 2)
    print("---------['Papi Gelato']---------")
    print(f'liters   {liters} x 9,80   = {totaal} €')
    print('                        -------- +')
    print(f'                        {totaal}€')
    print(f'btw                     {round(totaal / 100 * 9, 2)}€')

f = True
while f:
    klant = input('Bent u (1) particulier of (2) zakelijk?\n')
    if klant == '1':
        f = False
        hoeveelbollen()
        welkesmaken()
        hoorntjeofbakje()
    elif klant == '2':
        f = False
        print('zakelijk')
        hoeveelliters()
        welkesmakenliters()
        bonnetjezakelijk()
    else:
        print('Dat heb ik niet verstaan sorry!')


