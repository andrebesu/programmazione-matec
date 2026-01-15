#Somma di 5 numeri interi

#Versione con il while
somma = 0
i = 0
while i < 5:
    a = int(input("Inserisci un numero: "))
    somma = somma + a
    i = i + 1
print("La somma vale", somma)

#Versione con il for
somma = 0
i = 0
for i in range(0, 10):
    a = int(input("Inserisci un numero: "))
    somma = somma + a
    #i = i + 1
print("La somma vale", somma)
