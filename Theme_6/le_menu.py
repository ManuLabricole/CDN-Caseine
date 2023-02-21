# Un restaurant possède trois menus : le Basique à 9 euros, le Gourmand à 15 euros et le Complet à 19 euros. 
# Pour chacun des menus, le client peut choisir de rajouter une boisson à 4 euros. 
# De plus, le client peut choisir un supplément fromage et/ou un supplément café, chaque supplément coûtant 1,50 euros.

#     Écrire une fonction prix_menu qui prend comme argument le nom du menu (chaîne de caractères), puis deux arguments optionnels : 
# un booléen avecBoisson dont la valeur par défaut est False, et un entier nb_supplement qui doit valoir 0 par défaut. 
# La fonction doit renvoyer le prix du menu correspondant.
#     Écrire une fonction table_Dupont qui ne prend aucun argument et qui renvoie le prix total de l’addition pour la table des Dupont :
#         Jacqueline a choisi seulement un menu Basique,
#         Michel a pris un menu Gourmand avec boisson,
#         Johanna a choisi un menu Basique avec suppléments fromage et café,
#         et Antoine a choisi un menu Basique avec boisson et supplément café.

#  (Exercice proposé par Aurélie Lagoutte)



def prix_menu(menuName:str, avecBoisson:bool=False, nb_supplement:int=0) -> float:

    menuDict = {
    "Basique":float(9),
    "Gourmand":float(15),
    "Complet":float(19),
    "Boisson":float(4),
    "Supplement":float(1.5)
    }
    
    prix = menuDict[menuName]
    prix += menuDict["Supplement"]*nb_supplement
    
    if avecBoisson:
        prix += menuDict["Boisson"]
    else:
        pass
    
    return prix

def table_Dupont() -> float:
    prix = prix_menu("Basique") + prix_menu("Gourmand", avecBoisson=True) + prix_menu("Basique", nb_supplement=2) + prix_menu("Basique", avecBoisson=True, nb_supplement=1)
    
    return prix

if __name__=="__main__":
    print("Debut du prog. principal")
    print(prix_menu("Basique", True))    
    print(prix_menu("Gourmand", avecBoisson=True))    