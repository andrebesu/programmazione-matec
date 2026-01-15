#Dato un intero in input, voglio sapere se è pari o dispari
x = int(input("Inserisci un numero: "))
resto = x % 2
if resto == 0:
    print("Il numero", x, "è pari")
else:
    print("Il numero", x, "è dispari")