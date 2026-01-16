'''
Programma che chiede all'utente di inserire n numeri interi, con n a sua volta
in input, e conta quanti numeri pari sono stati inseriti
'''


n = int(input("Inserisci quanti interi vuoi utilizzare: "))
i = 0
conta_pari = 0
while i < n:
    a = int(input("Inserisci un intero: "))
    resto = a % 2
    if resto == 0:
        conta_pari += 1
        i = i + 1
print("Sono stati inseriti", conta_pari, "numeri pari")
