'''
Programma che raccoglie i voti di un esame del master. I voti vengono forniti in input.
Il programma deve stampare i voti finali: se più della metà degli studenti ha ottenuto
un voto inferiore a 24, tutti i voti vengono alzati di 3 punti
'''

n = int(input("Quanti voti vuoi inserire? "))
lista_voti = []   #ARRAY INZIALMENTE VUOTO
i = 0
conta_minori_24 = 0
while i < n:
    voto = int(input("Inserisci il voto: "))
    lista_voti.append(voto)
    if voto < 24:
        conta_minori_24 += 1
    i = i + 1
if conta_minori_24 > n/2:
    i = 0
    while i < n:
        lista_voti[i] = lista_voti[i] + 3
        i = i + 1
print("Voti finali: ", lista_voti)