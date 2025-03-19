# 70.1.
# Pani Binarna zakupiła tyle materiału, ile wynosi pole prostokąta ABCD, w którym mieści się
#
# zasłona. Oblicz, jaka będzie powierzchnia materiału pozostałego po wykrojeniu zasłony. Wy-
# nik podaj z dokładnością do 1/1000.


def funkcja(x):
    return (x*x*x*x)/500 - (x*x)/200 - 3/250

def liczenie_calki(a,b,przyblizenie):
    wynik = 0
    x = (b-a)/przyblizenie
    for i in range(przyblizenie):
        y = funkcja(a+i*x)
        wynik += y*x
    return wynik

def liczenie_calki_trapezy(a,b,przyblizenie):
    wynik = 0
    x = (b-a)/przyblizenie
    for i in range(przyblizenie):
        y = funkcja(a+i*x)
        y2 = funkcja(a+(i+1)*x)
        wynik += ((y+y2)/2)*x
    return wynik

print(liczenie_calki_trapezy(2436/125,-98,1000))