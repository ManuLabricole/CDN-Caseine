# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

def check_debut_inf_fin(numDebut : int, numFin : int) -> bool:
    
    if (numDebut < numFin) :
        return True
    else:
        return False
    
    

numDebut = int(input("Numero de début:"))
numFin = int(input("Numero de fin:"))
numZ = int(input("Numero de z:"))


zString = "z"*numZ

if (numDebut < numFin) :
    
    for i in range(numDebut, numFin):
        if (i%2) == 0:
            print(str(i) + " " + zString + "zigzag")
        else:
            print(zString + "zigzag" + " " + str(i))
            

