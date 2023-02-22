# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.





def separe(ligne):
    ligne=ligne.strip() # permet d'enlever un éventuel \n et/ou des espaces a la fin de la ligne
    liste_donnees=ligne.split(" ") # separe la ligne a chaque fois qu'un espace est rencontré
    return liste_donnees
    
def affiche_console(nom_fichier):
    print("====================================")
    print("Contenu du fichier", nom_fichier)
    print("====================================")
    with open(nom_fichier) as f:
        print(f.read())
        print("====================================")
        
def import_lignes(nomFichier:str):
    f = open(nomFichier)
    listFile = f.readlines()
    f.close()
    
    return listFile

def cree_patient(ligne:str) -> dict:
    
    newLigne = separe(ligne)
    
    patientDict = {
        "nom" : str(newLigne[0]),
        "poids" : float(newLigne[1]),
        "taille" : float(newLigne[2])
    }
    
    return patientDict

def liste_patients_from_nom_fichier(nomFichier:str) -> list:
    rawList = import_lignes(nomFichier=nomFichier)
    listPatient = []
    
    for el in rawList:
        listPatient.append(cree_patient(el))
    
    return listPatient
    
def imc(patient:dict) -> float:
    
    imc = patient["poids"]/patient["taille"]/patient["taille"]
    imc = round(imc, 2)
    
    return imc

def imc_moyen(listPatient:list) -> float:
    imcList = []
    for el in listPatient:
        imcList.append(imc(el))
    
    imc_moy = round(sum(imcList)/len(imcList), 2)
    
    return imc_moy

def liste_noms_patients_en_corpulence_normale(listPatient:list) -> list:
    listPatientNorm = []
    for patient in listPatient:
        if imc(patient) >= 18.5 and imc(patient) <= 25:
            listPatientNorm.append(patient["nom"])    
    
    return listPatientNorm
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    
    print("Test de la fonction affiche_console")
    #affiche_console("resultats-donnees1.txt")
    ListPatient = import_lignes("donnees1.txt")
    cree_patient(ListPatient[0])
   