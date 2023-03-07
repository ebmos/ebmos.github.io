import sys,time,os


# TREIG TEKST ANIMASJON GREIE TING TANG
def slowtext(text, delay_time=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != ".":
            time.sleep(delay_time)
        else:
            time.sleep(1)


# ÅPNER OG PRINTER TEKSTFILEN DER DEN FØRSTE DELEN (INTROEN) AV HISTORIEN ER
def openfile():
    with open("interaktivhistoriefortelling/tekster/historie.txt", "r", encoding="UTF-8") as file:
        data = ""
        for line in file:
            data += line
    return data

message = openfile()
slowtext(message)

# VALG A OG B

choices = ["a", "b"]

valg = input("\n \n VALG: a) Gå rett til skolen | b) Gå inn i kirken for å se hva som skjer (svar): ").lower()

# (FORTSETTELSE)
if valg in choices:
    def openfile():
        with open("interaktivhistoriefortelling/tekster/answer1.txt", "r", encoding="UTF-8") as file:
            data = ""
            for line in file:
                data += line
        return data

    answer1 = openfile()
    slowtext(answer1)

# HVIS DU VELGER NOE SOM IKKE ER INNENFOR LISTA (a & b)
elif valg not in choices:
    print("Feil input.")
    quit()


# VALG C OG D

choices2 = ["c", "d"]

valg2 = input("\n \n VALG: c) Per prøver å redde dragen selv | d) Per drar til legen for å hente medisiner: ").lower()

slowtext(valg2)

# SLUTT C
if valg2 == "c":
    if valg in choices:
        def openfile():
            with open("interaktivhistoriefortelling/tekster/answerC.txt", "r", encoding="UTF-8") as file:
                data = ""
                for line in file:
                    data += line
            return data

    answerC = openfile()
    slowtext(answerC) #nice


# HVIS DU SKRIVER NOE SOM IKKE ER INNENFOR LISTA (c & d)
elif valg2 not in choices2:
    print("Feil input.")
    quit()

# VALG D FORTSETTELSE
if valg2 == "d":
    def openfile():
            with open("interaktivhistoriefortelling/tekster/answerD.txt", "r", encoding="UTF-8") as file:
                data = ""
                for line in file:
                    data += line
            return data

    answerD = openfile()
    slowtext(answerD)


# VALG E OG F
    ef_choice = ["e", "f"]
    ef_valg = input("\n \n Skal han prøve å redde dragen med den gamle formelen (valg e), eller skal han gi opp og gå tilbake til skolen? (valg f): ").lower()

    slowtext(ef_valg)


# VALG E
if ef_valg == "e":
    def openfile():
        with open("interaktivhistoriefortelling/tekster/valge.txt", "r", encoding="UTF-8") as file:
            data = ""
            for line in file:
                data += line
        return data

    valge = openfile()
    slowtext(valge)


# VALG F
elif ef_valg == "f":
    def openfile():
        with open("interaktivhistoriefortelling/tekster/valgf.txt", "r", encoding="UTF-8") as file:
            data = ""
            for line in file:
                data += line
        return data

    valgf = openfile()
    slowtext(valgf)


# HVIS DU SKRIVER NOE SOM IKKE ER INNENFOR LISTA (valg e & f)
elif ef_valg not in ef_choice:
    print("Feil input.")
    quit()