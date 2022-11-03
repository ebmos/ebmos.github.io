# jeg ga opp

from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Hva er hovedpassordet? ")
key = load_key() + master_pwd.encode
fer = Fernet(key)




def view():
    with open('passord.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "\n" "Password:", 
                fer.decrypt(passw.encode()))



def add():
    name = input("Brukernavn: ")
    pwd = input("Passord: ")

    with open('passord.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input(
        "Vil du legge til et nytt passord, eller se eksisterende? (legg til / se) (trykk q for å avslutte.)").lower()
    if mode == "q":
        break

    if mode == "se":
        view()
    elif mode == "legg til":
        add()
    else:
        print("Feil input. Prøv på nytt")
        continue