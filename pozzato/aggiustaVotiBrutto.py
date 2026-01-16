'''
Programma che raccoglie i voti di un esame del master. I voti vengono forniti in input.
Il programma deve stampare i voti finali: se più della metà degli studenti ha ottenuto
un voto inferiore a 24, tutti i voti vengono alzati di 3 punti
'''

n = int(input("Quanti voti vuoi inserire? "))
i = 0
conta_sotto_24 = 0
while i < n:
    voto = int(input("Inserisci il voto: "))
    if voto < 24:
        conta_sotto_24 += 1
    i = i + 1
if conta_sotto_24 > n/2:
    i = 0
    while i < n:
        voto = int(input("Inserisci il voto: "))
        voto = voto + 3
        print("Voto finale: ", voto)
        i = i + 1
