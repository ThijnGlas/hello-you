import time
import os

#uitleg
vers1 = "ik heb 4 vragen om aan u te stellen"
vraag1= "hoe oud ben ik? "
vraag2= "waar woon ik?"
vraag3= "welke sport doe ik?"
vraag4= "wat is mijn tweede naam."
kies= "kies tussen A, B, C. "
brk= "______________________________________________________________________"
F= "dit antwoord is fout!"
T="dit antwoord is goed!"
N="voer een antwoord in."
O="Wil je nog een keer proberen? Beantwoord met Y/N."
goed= "het goede antwoord is"
voetbalvraag= "welke voetbalclub denk je dat ik voor ben?"

#voorstellen
print ("hello you, ik ben Thijn.")

#naam vragen
naam = input("wat is jouw voornaam? ")


print ("hallo "+ naam)

time.sleep (1)

print(vers1)

time.sleep (1)
print(brk)

#vraag1
print(vraag1)

#keuzes
print("A = 16")
print("B = 18")
print("C = 20")

X= input(kies)

if ( X == "A" ) :
    print(T)
else:
    print(F), print(goed + " A" )

print(brk)

time.sleep (1)

#vraag2
print(vraag2)

#keuzes
print("A = Alkmaar")
print("B = middenbeemster")
print("C = Amsterdam")

Z= input(kies)

if ( Z == "B" ) :
    print(T)
else:
    print(F), print(goed+" B")

print(brk)

time.sleep (1)

#vraag3
print(vraag3)

#voetbalvraag
A = "A = Az"
B = "B = ajax"
C = "C = voetbal kan mij niet minder boeien."

#keuzes
print("A = kickboksen")
print("B = voetbal")
print("C = fitness")

V = input(kies)

if ( V == "C" ) :
    print(T)
elif( V == "B" ) :
    time.sleep(1)
    print(brk)
    print(A)
    print(B)
    print(C)
    J= input("dit antwoord is niet goed. maar je kan wel raden welke voetbalclub ik voor ben")
if (J == "C"):
    print(T)
else:
    print(F), print(goed + " C")

print(brk)

time.sleep(1)

#vraag4
print(vraag4)

#keuzes
print("A = tobias")
print("B = Julius")
print("C = willem")

C= input(kies)

if ( C == "B" ) :
    print(T)
else:
    print(F), print(goed+" B")

print(brk)

time.sleep(1)

retry = input("wil je dit nog een keer proberen? y/n ")

print(brk)

if (retry == "y"):
    os.system('python "ditbenik.py"')
else:
    print("gemaakt door Thijn.")
