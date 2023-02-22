# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

# 1) Ecrire une fonction tarif_carte qui prend en argument une chaîne de caractère correspondant au nom de la carte ("Jeune" ou "Senior")
# et qui renvoie le prix de la carte. Si un autre nom que "Jeune" ou "Senior" est utilisé, la fonction affichera "Carte inconnue" 
# et ne renverra rien (ou renverra None, ce qui revient au même).

# 2) Ecrire une fonction plein_tarif qui prend en argument deux chaînes de caractères correspondant respectivement à la ville de 
# départ de la ville d'arrivée et qui renvoie le prix d'un billet plein tarif sur ce trajet-là. Si le trajet demandé n'est aucun 
# des 6 trajets existants dans cet exercice, la fonction affichera "Trajet inconnu" et renverra None (ou rien).

# 3) Ecrire une fonction tarif_billet qui prend en argument la ville de départ, la ville d'arrivée 
# et 3 arguments optionnels : un booléen modifiable indiquant si le billet est modifiable (True par défaut), 
# un argument carte correspondant au nom de l'éventuelle carte de réduction (None par défaut; pourra valoir "Jeune" ou "Senior" 
# dans les appels), et enfin un argument periode  (None par défaut; pourra valoir "bleue" ou "blanche" dans les appels), et qui 
# renvoie le tarif du billet. Si le trajet ou la carte demandé(e) est inconnu(e), un message d'erreur s'affichera et la fonction 
# renverra None.

def tarif_carte(carte):
    if carte == "Jeune":
        return float(50)
    elif carte == "Senior":
        return float(60)
    else:
        print("Carte inconnue")
        return None

def reduc_carte(carte, periode):
    
    if carte == "Jeune":
        if periode == "bleue":
            return float(0.5)
        elif periode == "blanche":
            return float(0.3)
        
    if carte == "Senior":
        if periode == "bleue":
            return float(0.5)
        elif periode == "blanche":
            return float(0.25)
        
    else:
        print("Carte inconnue")
        return None
    
def plein_tarif(city1, city2):
    city = [city1, city2]
    
    if("Grenoble" in city and "Lyon" in city): 
        return float(20)
        
    elif("Grenoble" in city and "Paris" in city):
        return float(100)
        
    elif("Lyon" in city and "Paris" in city):
        return float(80)
    else:
        print("Trajet inconnu")
        return None
        
def reduc_modifiable(is_modifiable:bool) -> float:
    if is_modifiable:
        return None
    else:
        return float(0.1)
    
def tarif_billet(city1, city2, modifiable=True, carte=None, periode=None):
    
    prixBillet = plein_tarif(city1=city1, city2=city2)
    prixCarte = tarif_carte(carte=carte)
    reducCarte = reduc_carte(carte=carte, periode=periode)
    reducModifiable = reduc_modifiable(is_modifiable=modifiable)
    
    if prixBillet is not None:
        prix = prixBillet
        
        if prixCarte is not None and reducCarte is not None:
            prix -= prix*reducCarte
        else:
            if reducModifiable is not None:
                prix -= prix*reducModifiable
            
        return prix    
        
    else:
        return None    

    print("-----------------")
    print(prixBillet)
    print(prixCarte)       
    print(reducCarte)
    print(reducModifiable)    
            
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    
    print(tarif_billet("Grenoble", "Lyon", modifiable=True, carte=None, periode=None))