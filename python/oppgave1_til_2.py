import numpy as np
i = 1
max = 20
hemmeligTall = np.random.randint(1,69)
print("Finn ut hvilket tall jeg tenker på med færrest mulig gjett, fra 1 - 69!")
gjettetTall = int(input("Hvilket tall gjetter du? "))
while gjettetTall != hemmeligTall:
  if gjettetTall < hemmeligTall:      
    print("tallet du gjettet er for lavt, prøv igjen")
  else:
    print("tallet du gjettet er for høyt, prøv igjen")    
  gjettetTall = int(input("Hvilket tall gjetter du? "))
  i = i + 1
  if i == 20:
    print ("Du har nådd maks antall forsøk, start på nytt") 
    break
print("du brukte", i, "forsøk på å gjette det riktige tallet")
