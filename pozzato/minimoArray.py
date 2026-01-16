#Ricerca del minimo in una sequenza con array

n = int(input("Quanti valori vuoi inserire? "))
i = 0
lista = []
while i < n:
    a = int(input("Inserisci un numero: "))
    lista.append(a)
    i = i + 1
minimo = int(input("Inserisci un numero: "))
i = 0
while i < n:
    if lista[i] < minimo:
        minimo = lista[i]
        i = i + 1


    a = int(input("Inserisci un numero: "))
    if a < minimo:
        minimo = a
    i = i + 1
print("Il minimo vale:", minimo)