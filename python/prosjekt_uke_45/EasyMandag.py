import random

'''
Oppgave 1
VELG RIKTIG OUTPUT
alternative 1 = 'none'
alternative 2 = 'invalid syntax'
alternative 3 = 'the cat on the roof'
'''
word = 'the cat on the roof'
print(word)

#Riktig output er alternativ 3

'''
Oppgave 2
VELG RIKTIG OUTPUT
alternative 1 = 'Eureka'
alternative 2 = 'IM- Åssiden vgs'
alterbative 3 = 'none'
'''
a =1
b =1
c =7
d =5

result = a + b + d
if result < c:
    print('Eureka')
else:
    print('IM- Åssiden vgs')


#Riktig output er alternative 2


'''
Oppgave 3 
Hvor mange ganger skal følgende loop kjøres?
VELG RIKTIG SVAR
 alternative 1 = 150
 alternative 2 = 50
 alternative 3 = 30
 alternative 4 = uendelig mange ganger.
'''

r = 150
while r <= 200:
    print(r)
    r+=5
 

#Riktig output er alternativ 2 (tror jeg)


'''
oppgave 4
forklar linje for linje hva er det som skjer i funksjonen oddTall.
 VIKTIG!!!!! Forklar linjene først, før du tester den i editoren din.
'''

def oddeTall():
     num1 = random.randint(1,10) #tilfeldig tall mellom 1 og 10
     num2 = random.randint(2,9) #tilfeldig tall mellom 2 og 9
     if num1%num2 ==0: ### symbol % betyr resten av tallet (deling)
            result = num1/num2
            
     return result
# nice
'''
 I linje 62, blir variabelen oddeTall gjort om til en funksjon.
 Linje 63 betyr at num1 blir til en variabel. random.randint(1,10) betyr at pcen
 skal velge et tilfeldig tall fra 1 - 10.
 I linje 64 skjer det samme, men bare at pcen skal velge et tall fra 2-9.

 I linje 65 står det at hvis variabelen num1 modulus (hva nå enn det er) num2 blir 0:
    variabelen result blir skapt, og den står for num1 delt på num2

    return result betyr at variabelen result (num1/num2) blir returnert i terminalen.
 '''