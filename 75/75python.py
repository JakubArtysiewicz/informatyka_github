with open('tekst.txt') as plik:
    tekst = plik.readline()
lista = tekst.split()

with open('probka.txt') as plik2:
    lista2 = []
    for i2 in plik2:
        lista2.append([i2.split()])

print(lista2)

def zad75_1():
    for wyraz in lista:
        if wyraz[0] == 'd' and wyraz[-1] == 'd':
           print(wyraz)

def szyfr(litera,klucz1,klucz2):
    szyfrowana_litera = ((ord(litera)-97) * klucz1) + klucz2
    if szyfrowana_litera > 25:
        return chr((szyfrowana_litera%26)+97)
    else:
        return chr(szyfrowana_litera+97)
def szyfr_cale_zdanie(slowo,klucz1,klucz2):
    wynik = ""
    for i in slowo:
        wynik += szyfr(i,klucz1,klucz2)
    return wynik

def zad75_2():
    for i in lista:
        wyraz = ""
        if len(i)>=10:
            for j in i:
                wyraz += szyfr(j,5,5)
            print(wyraz)

def zad75_3(i):
        for h in range(len(i[0][0])):
            for k1 in range(1,10000):
                for k2 in range(1,10000):
                    if szyfr_cale_zdanie(i[0][0],k1,k2) == i[0][1]:
                        return (k1,k2)

def zad75_3_deszyfr(i):
        for h in range(len(i[0][0])):
            for k1 in range(1,10000):
                for k2 in range(1,1000):
                    if szyfr_cale_zdanie(i[0][1],k1,k2) == i[0][0]:
                        return (k1,k2)

def zad75_podsumowanie():
    szyfr_deszyfr = []
    for i in lista2:
        szyfr_deszyfr.append(zad75_3(i))
        szyfr_deszyfr.append(zad75_3_deszyfr(i))
    return szyfr_deszyfr

print(zad75_podsumowanie())


