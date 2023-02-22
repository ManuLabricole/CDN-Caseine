# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

voyelleList = ["a", "e", "i", "o", "u", "y"]

def commence_par(lettre:str, mot:str) -> bool:
    listMot = list(mot)
    
    if len(listMot) > 0:
        if listMot[0] == lettre:
            return True
        else:
            return False
    
    else:
        raise ValueError("Empty string")

def contient_voyelle(mot:str) -> bool:
    voyelleList = ["a", "e", "i", "o", "u", "y"]
    listMot = list(mot)
    
    for el in voyelleList:
        print(el)
        if el in listMot:
            print(el + "is in " + mot)
            return True
        else:
            return False
        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    
    # Exemple de transformation d'un mot en liste
    mot="bonjour"
    test=list(mot)
    print(test)

    print(commence_par("a", "voiture"))  
    print(commence_par("a", "abri"))
    contient_voyelle("tortue")


