#Programma che, dato il punteggio di una prova, stampa il voto
punteggio = int(input("Inserisci il punteggio: "))
if punteggio < 18:
    print("Insufficiente")
else:
    if punteggio > 30:
        print("30 e lode")
    else:
        print(punteggio)
