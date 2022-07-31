
import logging
logging.basicConfig(level=logging.DEBUG)

print("Hej, pora na małe obliczenia")
dzialanie = float(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
pierwsza = float(input("Skoro wiemy co bedziemy robic prosze podaj pierwsza liczbe :"))
druga = float(input("Dobra jeszcze tylko druga liczba :"))



def dodawanie(pierwsza, druga):
    return pierwsza + druga
def odejmowanie(pierwsza, druga):
    return pierwsza - druga
def mnozenie(pierwsza, druga):
    return pierwsza * druga
def dzielenie(pierwsza, druga):
    return pierwsza / druga

dod=dodawanie(pierwsza, druga)
ode=odejmowanie(pierwsza, druga)
mno=mnozenie(pierwsza, druga)
dzie=dzielenie(pierwsza, druga)

def kalkulator(dzialanie):
    if dzialanie == 1:
        logging.debug("Dodaję  " + str(pierwsza) + " i "+ str(druga))
        print(f"Wynik to " + str(dod))
    if dzialanie == 2:
        logging.debug("Odejmuje  " + str(pierwsza) + " i "+ str(druga))
        print(f"Wynik to " + str(ode))
    if dzialanie == 3:
        logging.debug("Mnoze  " + str(pierwsza) + " i "+ str(druga))
        print(f"Wynik to " + str(mno))
    if dzialanie == 4:
        logging.debug("Dziele  " + str(pierwsza) + " i "+ str(druga))
        print(f"Wynik to " + str(dzie))

kalkulator(dzialanie)


"""
if dzialanie == 1:
    print("Dodaję "+ str(pierwsza) + " i "+ str(druga))
    print(f"Wynik to " + str(pierwsza + druga))
if dzialanie == 2:
    print("Odejmuje "+ str(pierwsza) + " i "+ str(druga))
    print(f"Wynik to " + str(pierwsza + druga))
if dzialanie == 3:
    print("Mnoze "+ str(pierwsza) + " i "+ str(druga))
    print(f"Wynik to " + str(pierwsza + druga))
if dzialanie == 4:
    print("Dziele "+ str(pierwsza) + " i "+ str(druga))
    print(f"Wynik to " + str(pierwsza + druga))
"""
