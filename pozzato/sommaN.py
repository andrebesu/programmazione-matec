#Somma di N numeri interi
n = int(input("Dimmi quanti numeri vuoi sommare: "))
somma = 0
i = 0
while i < n:
    a = int(input("Inserisci un numero: "))
    somma = somma + a
    i = i + 1
print("La somma vale", somma)
