print("-" * 40)
print("Calcola il Perimeto")
print("-" * 40)

print("Fa la tua scelta \n")
print(""" A  Quadrato \n B  Cerchio  \n C Rettangolo \n """)
print("Cosa hai scelto ? \n")
scelta = str(input("A, B, C \n "))
if scelta == 'A':
    print("Ai scelto Quadrato !\n")
    lato = float(input("Inserisci il lato \n"))
    perimetro = lato * 4
    print(f"Il perimetro del tuo quadrato e : {perimetro}")

elif scelta == 'B':
    print("Hai selezionato Cerchio! \n ")
    r = float(input("Inserisci il raggio \n"))
    cir = 2 * r 
    print(f"La circonferenza del cerchio e :\n {cir} ")

elif scelta == 'C' :
    print("Hai scelto Rettangolo! \n")
    base = float(input("Inserisci la base\n"))
    altezza = float(input("Inserisci l'altezza \n"))
    per = (base * 2) + (altezza * 2)
    print(f"Il perimetro del rettangolo e : {per}")
    
else:
    print("Scelta non valida")
