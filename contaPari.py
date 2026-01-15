'''
Programma che chiede all'utente di inserire n numeri interi, con n a sua volta
in input, e conta quanti numeri pari sono stati inseriti
'''


n = int(input("Scegli quanti numeri inserire: "))

contatore_numeriPari = 0
i = 0

while i < n:
    numero = int(input("Inserisci un numero intero: "))
    if numero % 2 == 0:
        contatore_numeriPari += 1
        print("Il numero è pari")
    else:
        print("Il numero è dispari")
    i = i + 1

print("Dei", n, "numeri che hai inserito, ", contatore_numeriPari, "sono pari")

