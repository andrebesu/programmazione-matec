# Conta quanti voti sono alti (>26)
voto1 = int(input("Inserisci il voto: "))
voto2 = int(input("Inserisci il voto: "))
voto3 = int(input("Inserisci il voto: "))
conta = 0
if voto1 > 26:
    conta = conta + 1
if voto2 > 26:
    conta = conta + 1
if voto3 > 26:
    conta = conta + 1
print("Hai ottenuto", conta, "voti alti")

