import sys

print("Hej, pora na małe obliczenia")
dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
pierwsza = input("Skoro wiemy co bedziemy robic prosze podaj pierwsza liczbe :")
druga = input("Dobra jeszcze tylko druga liczba :")
print(pierwsza)
print(druga)
print(dzialanie)


def dodawanie(pierwsza, druga):
    return pierwsza + druga
def odejmowanie(pierwsza, druga):
    return pierwsza - druga
def mnozenie(pierwsza, druga):
    return pierwsza * druga
def dzielenie(pierwsza, druga):
    return pierwsza / druga


def kalkulator(dzialanie):
    if dzialanie == 1:
        print(dodawanie)
    if dzialanie == 2:
        print(odejmowanie)
    if dzialanie == 3:
        print(mnozenie)
    if dzialanie == 4:
        print(dzielenie)

kalkulator(dzialanie)