""""
Implementacja programu w ramach Mikro-Projektu “CodesMicroHack” z przeddmiotu WMMC.

Marta Brzezińska
Kinga Kawczyńska
"""
tresc1 = ""
rozw1 = ""

tresc2 = ""
rozw2 = ""

tresc3 = "Czy kryptosystemy McEliece’a i Niederreiter’a są sobie równoważne? Udowodnij."
rozw3 = "tak"

tresc4 = ""
rozw4 = ""

def zadania():
    print("Start!")
    print("Zadanie 1")
    print(tresc1)
    odp1 = input()

    while odp1 != rozw1:
        print("Niepoprawne rozwiązanie, spróbuj jeszcze raz!")
        odp1 = input()

    print("Super! Przechodzimy do kolejnego zadania.")
    print("Zadanie 2")
    print(tresc2)
    odp2 = input()

    while odp2 != rozw2:
        print("Niepoprawne rozwiązanie, spróbuj jeszcze raz!")
        odp2 = input()

    print("Super! Przechodzimy do kolejnego zadania.")
    print("Zadanie 3")
    print(tresc3)
    odp3 = input()

    while odp3 != rozw3:
        print("Niepoprawne rozwiązanie, spróbuj jeszcze raz!")
        odp3 = input()

    print("Super! Przechodzimy do kolejnego zadania.")
    print("Zadanie 4")
    print(tresc4)
    odp4 = input()

    while odp4 != rozw4:
        print("Niepoprawne rozwiązanie, spróbuj jeszcze raz!")
        odp4 = input()
    print("Gratulacje! To już koniec.")

if __name__ == '__main__':
    zadania()
