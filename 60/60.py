# Zadanie 60.
# Wiązka zadań Dzielniki
# W pliku liczby.txt danych jest 200 różnych liczb całkowitych z przedziału [2, 1 000
# 000], każda w osobnym wierszu pliku. Napisz program (lub kilka programów), który poda
# odpowiedzi do poniższych zadań. Odpowiedzi zapisz do pliku wyniki.txt.
# 60.1.
# Policz, ile jest w pliku wejściowym liczb mniejszych niż 1000, oraz podaj dwie takie liczby,
# które pojawiają się w pliku jako ostatnie (możesz założyć, że będą co najmniej dwie).
# 60.2.
#
# Wśród liczb występujących w pliku wejściowym znajdź te, które mają dokładnie 18 dzielni-
# ków naturalnych (wliczając w nie 1 i samą liczbę). Dla każdej znalezionej liczby wypisz,
#
# oprócz jej wartości, listę wszystkich jej dzielników, posortowaną rosnąco.

# 60.3.
# Znajdź największą liczbę w pliku, która jest względnie pierwsza ze wszystkimi pozostałymi,
# czyli taką, która z żadną z pozostałych liczb nie ma wspólnego dzielnika innego niż 1.

with open("liczby.txt") as f:
    wynik = f.read()
    wynik_lista = wynik.split("\n")
    wynik_lista.pop(-1)

def zad60_1():
    wynik = []
    for i in wynik_lista:
        if int(i)<1000:
            wynik.append(int(i))
    return wynik

def zad60_1_odpowiedzi():
    lista = zad60_1()
    print(len(lista))
    print(lista[-2],lista[-1])

def zad60_2():
    liczby_dzielniki_tych_liczb_18 = []
    for i in wynik_lista:
        lista_dzielnikow_liczby = []
        licznik_dzielnikow_liczby = 0
        for j in range(1,int(i)+1):
            # if int(i)%(j**(1/2)) == 0:
            if int(i)%j == 0:
                lista_dzielnikow_liczby.append(j)
                licznik_dzielnikow_liczby += 1
        if licznik_dzielnikow_liczby == 18:
            liczby_dzielniki_tych_liczb_18.append([i,lista_dzielnikow_liczby])
    return liczby_dzielniki_tych_liczb_18

def wszystkie_dzielniki(liczba):
    dzielniki = []
    for i in range(2,int(int(liczba)**(1/2))+1):
        if liczba%i == 0:
            dzielniki.append(i)
    return dzielniki

def zad60_3():
    wynik = []
    for i in wynik_lista:
        zabezpieczenie = True
        licznik = 0
        wynik_i = wszystkie_dzielniki(int(i))
        for j in wynik_lista:
            wynik_j = wszystkie_dzielniki(int(j))
            if wynik_lista.index(j) != wynik_lista.index(i):
                zabezpieczenie = False
                for k in wynik_j:
                    if k in wynik_i:
                        licznik += 1
                        break
        if licznik == 0 and zabezpieczenie == False:
            wynik.append(i)
    return wynik

def zad60_3_odpowiedz():
    najw = 0
    wynik = zad60_3()
    for i in wynik:
        if int(i)>najw:
            najw = int(i)
    return najw
print(zad60_3_odpowiedz())


