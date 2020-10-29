#keuze verhaal van Mohab

#imports
import time
import os

#intro
print("Hallo mijn naam is Thijn Glas en ik ga het verhaal vertellen van Mohab. er komt steeds een stukje tekst bij als u op ENTER klikt. Als je het originele verhaal wilt zonder keuzes kunt u Enter inklikken zonder iets in hoeven te vullen.")

time.sleep (1)

#voorafgaand het verhaal
tekst1= "Het verhaal van Mohab Alkatmeh begint in Hama, de stad in Syrië waar hij opgroeide."
tekst2= "Het is vroeg in de ochtend als je van huis naar school loopt. Het lijkt een dag zoals alle andere. Op één ding na: om 8 uur begint je laatste examen. als je die haalt ben je geslaagd."
tekst3= "Op weg naar school wordt je staande gehouden door twee mannen die aan komen rijden op een motor. Er wordt gevraagd of je jouw identiteitsbewijs wil laten zien. Na wat gebabbel in hun walkietalkie bepalen ze dat je mee moet naar een militaire outpost."
tekst4= "je legt uit dat jouw examen om 8 uur begint, en dat je het hele jaar opnieuw moet doen als je die niet haalt. De situatie slaat om. in een keer voel je een pistool tegen jouw hoofd, krijgt boeien om je polsen en wordt geblinddoekt. "
tekst5= "De mannen nemen je mee naar een plek, door je blinddoek heb jij geen idee waar. In een gebouw wordt je meegesleurd naar een kelder."
tekst6= "‘Who is your god!’, ‘Who is your god!’, ‘Assad!, Assad!’, klinkt het vanuit de kelder. De middelbare scholier ziet niets maar kan aan het geschreeuw horen dat mensen om je heen in deze ruimte gemarteld worden."
tekst7= "je wordt op een stoel gezet, de gijzelnemers bellen jouw vader en moeder. De mannen willen geld van Mohab zijn ouders, een bedrag dat zijn ouders niet kunnen betalen. Het dringt tot hem door. Hij is gekidnapt door handlangers van “Assad”."
tekst8= "Tien dagen lang houden zij je vast. Totdat ze op een dag met de auto ergens naartoe brengen. je herkent het gebied, het is richting de begraafplaats waar je opa en oma liggen begraven. ‘Hier gaan ze me nu afmaken’"
tekst9= "Maar dat gebeurt niet. De kidnappers gooien je uit de rijdende auto. je valt op de grond, de mannen rijden door en keren niet meer terug."
#keuze1

#het vluchten
vtekst1= "Vanaf die dag ben je geen middelbare scholier meer maar een oorlogsvluchteling."
vtekst2= "“Het geld dat mijn ouders kregen dankzij de verkoop van het huis, gaven zij aan je mee om de reis te kunnen bekostigen. Zo kon je bijvoorbeeld de taxichauffeur betalen die je naar Libanon ‘smokkelde’”."
vtekst3= "Eenmaal in Libanon moet de overstap naar Turkije worden gemaakt."
vtekst4= "Een man biedt aan om jou en dertig anderen in een rubberen bootje te brengen in ruil voor geld. Eenmaal op de boot bleken dat 46 mensen te zijn"
#keuze2
vtekst5= "wonder boven wonder halen de 46 mensen de overkant. Vanuit Turkije ga je Europa in."

#toevallig in de NL belandt
ntekst1= "In eerste instantie wil je naar het Duitse Frankfurt. Maar dat plan gaat op het laatste moment niet door."
ntekst2= "“Tijdens je tocht in Europa word je noodgedwongen opgevangen in een ziekenhuis in Oostenrijk. je bent zwak en moet continu overgeven. Waarschijnlijk omdat je iets met varken had gegeten, dat is je lichaam niet gewend.”"
ntekst3= "Het ziekenhuis wil je niet laten gaan, ondanks dat je de trein om 8 uur ’s morgens (weer dat tijdstip!) moet halen naar Frankfurt. “Ik moest die trein hebben want ik had van mijn laatste geld een ticket voor deze rit gekocht”."
#keuze3
ntekst4= "Uiteindelijk ga je op eigen houtje het ziekenhuis uit. “Al mijn spullen waren alleen niet meer op de plek waar ze eerst lagen. Hoe dan ook, ik snel sprintte naar het station… bleek ik toch te laat zijn.”"
ntekst5= "Zonder spullen, zonder geld, in een land waar je de taal niet spreekt."
ntekst6= "Terwijl de tranen over je wangen lopen komt er een man die Arabisch spreekt naar je toe. Hij vertelt je de volgende trein om 9 uur te nemen naar Amsterdam. In Nederland is volgens de man meer plek voor vluchtelingen dan in Duitsland, dat al twee miljoen mensen heeft opgenomen."
ntekst7= "“De man zei dat ik moest doen alsof ik sliep wanneer de conducteur om een ticket zou vragen. En als de controleur mij toch wakker maakte, moest ik zeggen dat mijn vriend – die even naar de wc is – de kaartjes heeft.”"
#keuze 4
ntekst8= "je gebruikt uiteindelijk beide tips. De slaaptruc in Duitsland en later ook in gebrekkig Engels de vriend-naar-de-wc-truc  in Nederland. Zo komt je aan in Nederland het land waar je nu woont."

itekst1= "Voor vluchtelingen is Nederland complex. Ook is er het taalverschil.de lange tijden van inburgeren drijven veel vluchtelingen tot wanhoop. Meer dan een jaar heeft Mohab moeten wachten in opvangcentra."
itekst2= "“Ik wist in die opvangcentra niet waar ik aan toe was. Of ik mocht blijven en of mijn ouders hierheen konden komen. Ik besloot mezelf nuttig te maken en daarom – met behulp van een online tool – RefInfo te bouwen tijdens mijn verblijf in de opvangcentra. Dit is een app voor Android-toestellen.”"
itekst3= "het was een moeilijke tijd maar ik heb het gered. nu ben ik een burger van Nederland."

brk= "______________________________________________________________________________________________________________"
# verhaal begint
input()
print (tekst1)

input()
print (tekst2)

input()
print (tekst3)

input()
print (tekst4)

input()
print (tekst5)

input()
print (tekst6)

input()
print (tekst7)

input()
print (tekst8)

input()
print (tekst9)

#keuze1
print (brk)
keuzeAA = input ("je hebt nu een keuze. A = je probeert te vluchten zodat ze je niet meer kunnen lastig vallen of B = Je hoopt dat je nooit meer door ze word lastig gevallen.")

if (keuzeAA == "A"):
    print("je ouders verkopen hun huis zodat ze je genoeg geld meegeven zodat je kunt vluchten.")
elif (keuzeAA == "B"):
    print("Het gaat de eerste 2 weken goed, je leeft je leven alsof er niks aan de hand is. tot dat je weer na de 4de week was ontvoerd. Het was geen goede keuze om te blijven. je leeft de rest van je leven in een gevangenis. Je had dus beter kunnen vluchten.")
    quit()

print(brk)

input()
print (vtekst1)

input()
print (vtekst2)

input()
print (vtekst3)

input()
print (vtekst4)

#keuze2
print(brk)

keuzeBA= input ("je hebt nu een keuze. ga je mee met de boot (A) of ga je voor meer geld een andere boot nemen waar minder mensen opzitten(B)")
if (keuzeBA == "A"):
    print("je neemt de boot")
elif(keuzeBA == "B"):
    print("je bent opgelicht door degene die je zou over varen. je hebt niet genoeg geld om een ander iemand te vragen. je hebt geen keuze meer om te vluchten. je bent nu dakloos en heb geen geld meer.")
    quit()

print(brk)
input()
print (vtekst5)

input()
print (ntekst1)

input()
print (ntekst2)

input()
print (ntekst3)

#keuze3
print (brk)

keuzeCA= input ("je hebt nu een keuze. blijf je in het ziekenhuis (A) of ga je stiekem het ziekenhuis verlaten zodat je naar de trein kan (B)?")
if (keuzeCA == "A"):
    print("je blijft in het ziekhuis. daar word je geholpen maar als je op het punt staat om te vertrekken komt de duoane om je op te halen. je word daar onderzocht en wordt naar een vluchtelingen centrum gebracht in Duitsland.")
    quit()
elif (keuzeCA == "B"):
    print("je besluit te vertrekken.")

print (brk)

input()
print (ntekst4)

input()
print (ntekst5)

input()
print (ntekst6)

input()
print (ntekst7)

print(brk)
keuzeDA= input ("je hebt nu een keuze. besluit je om de tips van die man te gebruiken en naar Nederland te gaan (A) of ga je naar een politie bureau voor hulp.")
if (keuzeDA == "A"):
    print("je pakt de trein.")
elif(keuzeDA == "B"):
    print("je gaat naar het bureau, je word geholpen maar niet zoals je wou. je word doorgestuurd naar de douane, daar word je wel geholpen. je verhuist tijdelijk naar Duitsland. je bent 2 jaar later officieel een burger in Duitsland")
    quit()

print(brk)

input()
print (ntekst8)

input()
print (itekst1)

input()
print (itekst2)

input()
print (itekst3)

input()
print("dit is het einde van het verhaal, gemaakt door Thijn Glas")
