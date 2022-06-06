""""
Implementacja programu w ramach Mikro-Projektu “CodesMicroHack” z przeddmiotu WMMC.

Marta Brzezińska
Kinga Kawczyńska
"""
tresc1 = "Czy dla dowolnej macierzy generującej kod liniowy zawsze można jednoznacznie \n"\
        "wyznaczyć macierz kontroli parzystości z dokładnością do zmiany kolejności wierszy. "
rozw1 = "nie"

tresc2 = "Rozważmy automat skończony o 64 stanach dla kodu splotowego o parametrach r = 4 i K = 7, \n" \
            "którego wartości przejść (wartości na krawędziach diagramu) znajdują się w liscie automat. \n"  \
            "Listę tę czytamy tak, że na $i$-tym indeksie (indeksujemy od zera) znajduje się zakodowana \n" \
            "(naszym kodem) binarna reprezentacja liczby i. Pierwsza cyfra binarnej reprezentacji i determinuje przejście do następnego stanu, a pozostałe stan wychodzący. Wiemy, że jedna z wartości przejsc \n" \
            "w automacie jest błędna. Znajdź ją i popraw (wartość ta jest flagą)."
automat = [[0, 0, 0, 0], [1, 0, 1, 1], [0, 0, 1, 1], 
           [1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0], 
           [1, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], 
           [0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 0, 0], 
           [0, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], 
           [1, 0, 0, 1], [0, 0, 1, 0], [1, 0, 0, 1], 
           [0, 0, 0, 1], [1, 0, 1, 0], [1, 1, 1, 1], 
           [0, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1],
           [1, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], 
           [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 0], 
           [0, 0, 0, 0], [1, 0, 1, 1], [0, 1, 1, 0], 
           [1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0], 
           [1, 0, 1, 1], [0, 0, 0, 0], [1, 0, 0, 0], 
           [0, 0, 1, 1], [1, 0, 1, 0], [0, 0, 0, 1], 
           [1, 0, 0, 1], [0, 0, 1, 0], [0, 1, 1, 1], 
           [1, 1, 0, 0], [0, 1, 0, 0], [1, 1, 1, 1], 
           [0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], 
           [1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0], 
           [1, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], 
           [0, 0, 1, 1], [1, 0, 1, 1], [0, 0, 0, 0], 
           [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0], 
           [1, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 0], 
           [1, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0], 
           [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 0, 0], 
           [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0], 
           [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1], 
           [1, 0, 1, 1], [0, 0, 0, 0], [1, 0, 1, 1], 
           [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 1], 
           [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], 
           [1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 0, 0], 
           [0, 1, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0], 
           [0, 0, 0, 1], [1, 0, 0, 1], [0, 0, 1, 0], 
           [1, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 0], 
           [0, 1, 1, 1], [0, 0, 1, 0], [1, 0, 0, 1], 
           [0, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 1], 
           [1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], 
           [1, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], 
           [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], 
           [1, 1, 1, 0], [0, 1, 0, 1], [0, 0, 0, 0], 
           [1, 0, 1, 1], [0, 0, 1, 1], [1, 0, 0, 0], 
           [0, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], 
           [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1], 
           [1, 1, 1, 1], [0, 1, 0, 0]]


rozw2 = "[1, 1, 0, 0]"

tresc3 = "Rozważmy kryptosystem McEliece’a, gdzie wykorzystując klucz publiczny G′ szyfrujemy wiadomość za pomocą wzoru: \n" \
         "c = mG′ + e \n" \
         "oraz kryptosystem Niederreiter’a, w którym wykorzystując klucz publiczny H′ szyfrujemy za pomocą wzoru:\n" \
         "s = eH′T \n" \
         "Czy bezpieczeństwa tych kryptosystemów są sobie równoważne? Udowodnij."
rozw3 = "tak"

tresc4 = "Rozważmy kod splotowy o r=2 i K=3. Niech: \n" \
         "g1(x1,x2,x3)=x3+x2, \n" \
         "g2(x1,x2,x3)=x3+x2+x1, \n" \
         "p=(0,0).\n" \
         "\n" \
         "Za jego pomocą zostało zakodowanych 8 6-bitowych słów i otrzymano następujące wyniki:\n" \
         "(1,1,1,1,0,1,1,1,1,1,0,1)\n" \
         "(1,0,1,1,0,1,1,1,0,0,0,1)\n" \
         "(0,0,1,1,0,0,1,0,1,0,0,0)\n" \
         "(1,1,1,1,0,1,0,0,1,1,0,0)\n" \
         "(0,1,0,0,1,1,1,1,1,1,0,0)\n" \
         "(0,0,1,1,1,1,0,1,1,1,0,0)\n" \
         "(1,1,0,0,1,0,1,0,1,1,0,1)\n" \
         "(1,1,0,0,1,0,1,1,1,1,0,1)\n" \
         "W ilu przypadkach został popełniony błąd podczas kodowania?"
rozw4 = "3"

def zadania():
    print("Start!")
    print("Zadanie 1")
    print(tresc1)
    odp1 = input()

    while odp1 != rozw1:
        print("Niepoprawne rozwiązanie, spróbuj jeszcze raz!")
        odp1 = input()

    print("Super! Przechodzimy do kolejneg zadania.")
    print("Zadanie 2")
    print(tresc2)
    print('automat = ', automat)
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
