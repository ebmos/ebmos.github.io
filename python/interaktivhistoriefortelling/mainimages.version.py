import sys,time,os
from PIL import Image

one = Image.open("interaktivhistoriefortelling/bilder/story1.png")
two = Image.open("interaktivhistoriefortelling/bilder/story2.png")
C = Image.open("interaktivhistoriefortelling/bilder/storyC.png")
three = Image.open("interaktivhistoriefortelling/bilder/story3.png")
E = Image.open("interaktivhistoriefortelling/bilder/storyE.png")
F = Image.open("interaktivhistoriefortelling/bilder/storyF.png")

# INTRO

one.show()
    
# VALG A OG B

choices = ["a", "b"]

valg = input("\n \n VALG: a) Gå rett til skolen | b) Gå inn i kirken for å se hva som skjer (svar): ").lower()

# (FORTSETTELSE)
if valg in choices:
    two.show()

# HVIS DU VELGER NOE SOM IKKE ER INNENFOR LISTA (a & b)
elif valg not in choices:
    print("Feil input.")
    quit()

# VALG C OG D

choices2 = ["c", "d"]

valg2 = input("\n \n VALG: c) Per prøver å redde dragen selv | d) Per drar til legen for å hente medisiner: ").lower()

# SLUTT C
if valg2 == "c":
    C.show()

# HVIS DU SKRIVER NOE SOM IKKE ER INNENFOR LISTA (c & d)
elif valg2 not in choices2:
    print("Feil input.")
    quit()

# VALG D FORTSETTELSE
if valg2 == "d":
    three.show()


# VALG E OG F
    ef_choice = ["e", "f"]
    ef_valg = input("\n \n Skal han prøve å redde dragen med den gamle formelen (valg e), eller skal han gi opp og gå tilbake til skolen? (valg f): ").lower()


# VALG E
    if ef_valg == "e":
        E.show()

# VALG F
    elif ef_valg == "f":
        F.show()

# HVIS DU SKRIVER NOE SOM IKKE ER INNENFOR LISTA (valg e & f)
    elif ef_valg not in ef_choice:
        print("Feil input.")
        quit()

        #nice