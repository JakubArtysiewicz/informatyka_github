liczby1_lista = []
with open("liczby1.txt") as liczby1:
    for liczba in liczby1:
        liczby1_lista.append(liczba)

def dec_na_binarny(liczba):
    wynik = ""
    while liczba > 0:
        wynik = wynik + str(liczba % 2)
        liczba = liczba // 2
    return wynik

def bin_na_oks(liczba):
    wynik = ""
    mniejszywynik = 0
    mnoznik = 0
    for i in liczba[::-1]:
        mniejszywynik += int(i)*(2**mnoznik)
        mnoznik += 1
        if mnoznik == 3:
            wynik += str(mniejszywynik)
            mniejszywynik = 0
            mnoznik = 0
    if mnoznik > 0:
        wynik += str(mniejszywynik)
    return wynik[::-1]

def zad62_1(lista_liczb):
    najm = 0
    najw = 0
    for i in lista_liczb:
        if int(i) > najw:
            najw = int(i)
        if int(i) < najm:
            najm = int(i)

    return najm, int(bin_na_oks(dec_na_binarny(najw)))

def zad62_2(lista_liczb):
    najw_ilosc_liczb = 0
    ilosc_liczb = 0
    lista_liczb_najw = []
    lista_liczb_akt = []
    for i in lista_liczb:
        lista_liczb_akt.append(int(i))
        ilosc_liczb += 1
        for j in range(len(lista_liczb)-lista_liczb.index(i)):
            if j > int(i):
                ilosc_liczb += 1
                if ilosc_liczb > najw_ilosc_liczb:
                    najw_ilosc_liczb = ilosc_liczb
            else:
                if len(lista_liczb_akt) > len(lista_liczb_najw):
                    lista_liczb_najw = lista_liczb_akt
                lista_liczb_akt.clear()
                ilosc_liczb = 0
                break
    return najw_ilosc_liczb, lista_liczb_najw

print(zad62_2(liczby1_lista))

print(zad62_1(liczby1_lista))

