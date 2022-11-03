def addition(tall1, tall2):
    return tall1 + tall2

def subtraction(tall1, tall2):
    return tall1 - tall2

def multiplication(tall1, tall2):
    return tall1 * tall2

def division(tall1, tall2):
    return tall1 / tall2



while True:
    print("Velg operasjon:")
    print("1. Addisjon")
    print("2. Subtraksjon")
    print("3. Multiplikasjon")
    print("4. Divisjon")

    tall = input("Skriv inn et tall (1/2/3/4): ")

    if tall in ('1', '2', '3', '4', '5'):
        num1 = float(input("Skriv inn ditt første tall: "))
        num2 = float(input("Skriv inn ditt andre tall: "))

        if tall == '1':
            print(num1, "+", num2, "=", addition(num1, num2))

        elif tall == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif tall == '3':
            print(num1, "*", num2, "num", multiplication(num1, num2))

        elif tall == '4':
            print(num1, "/", num2, "num", division(num1, num2))

        
        ny_kalk = input("Skal vi gjøre en annen kalkulasjon? (y/n): ")
        if ny_kalk == "n":
            break


    else:
        print("Feil input")