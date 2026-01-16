#Ricerca del minimo in una sequenza

n = int(input("Quanti valori vuoi inserire? "))
i = 1      #metto 1 perché c'è un input già PRIMA del ciclo, e DENTRO al ciclo ce ne sono poi 5, se mettessi i = 0 verrebbe 1 + 5 quindi 6 inserimenti di numeri
minimo = int(input("Inserisci un numero: "))
while i < n:
    a = int(input("Inserisci un numero: "))
    if a < minimo:
        minimo = a
    i = i + 1
print("Il minimo vale:", minimo)