print("----------------------------------------------------")
print("Welkom bij het soliciatie procress")
print("voor Circusdirecteur voor Circus HotelDeBotel.")
print("Er komen wat simpele vragen beantwoord ze eerlijk.")
print("----------------------------------------------------")
naam = input("Wat is uw naam: ")
geslacht = input("Wat is uw geslacht (M/F) ")
lengte = int(input("Hoe lang bent u in hele centimeters: "))
gewicht = int(input("Hoe zwaar bent u in hele kilo's: "))

evaringDieren = int(input("Hoeveel jaar praktijk ervaring heeft u met dieren-dressuur "))
evaringJongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren "))
evaringAcrobatiek = int(input("Hoeveel jaar praktijk ervaring heeft u met acrobatiek "))

diploma = input("Heeft u een diploma MBO-4 ondernemen(Y/N) ")
rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs(Y/N) ")
hoed = input("Heeft u een hoge hoed in bezit(Y/N) ")

snor = 0
haarLengte = 0

if geslacht == "M":
    snor = int(input("Hoe breed is uw snor in hele centimeters? "))
elif geslacht == "F":
    rood = input("Heeft uw rood krulhaar?(Y/N) ")
    if rood:
        haarLengte = int(input("Hoe lang is uw haar in hele centimeters? "))

certificaat = input("Heeft u het certificaat 'Overleven met gevaarlijk personeel'?(Y/N) ")
certificaat2 = input("Heeft u het certificaat 'Omgaan met clowns'?(Y/N) ")
certificaat3 = input("Heeft u het certificaat 'Een circus zijn en worden'?(Y/N) ")

berenPak = input("Heeft u een beren pak?(Y/N) ")
pakLente = 0
if berenPak == "Y":
    pakLente = int(input("Hoelang is uw beren pak in de lengte in hele centimeters? "))

print("")

if (evaringDieren > 4 or evaringJongleren > 5 or evaringAcrobatiek > 3) and diploma == "Y" and rijbewijs == "Y" and hoed == "Y" \
and ((geslacht == "M" and snor > 10) or (geslacht == "F" and haarLengte > 20)) and lengte > 150 and gewicht > 90 and certificaat == "Y":
    print("Gefeliciteerd uw mag zich direct komen melded bij de circus want uw bent aangenomen")
else:
    print("Helaas uw bent niet aangenomen, bedankt voor de deelname")
