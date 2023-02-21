# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.



def is_pair(num:int) -> bool:
    
    if num < 0 :
        raise ValueError("Should be integer positive")
    
    if num%2 == 0:
        return True
    else:
        return False

def make_pair_list(numList:list) -> list:
    
    numListCopy = numList.copy()
    pairList = []
    
    for el in numListCopy:
        if is_pair(int(el)):
            pairList.append(el)
    
    return pairList

def somme_pairs(numList:list) -> int:

    numListCopy = numList.copy()
    pairList = make_pair_list(numListCopy)
    
    return sum(pairList)
    

def nb_elem_pairs(numList:list) -> int:
    
    numListCopy = numList.copy()
    pairList = make_pair_list(numListCopy)
    
    return len(pairList)

def max_pair(numList:list) -> list:
    
    numListCopy = numList.copy()
    pairList = make_pair_list(numListCopy)
    
    return max(pairList)

def min_pair(numList:list) -> list:
    
    numListCopy = numList.copy()
    pairList = make_pair_list(numListCopy)
    
    return min(pairList)
    
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    print(is_pair(8))
    print(make_pair_list([4, 5, 10, 12, 7, 13, 20]))
    print(somme_pairs([4, 7, 12, 0, 21, 5]))


## Ci-dessous: copie des exemples
## Pour avoir l'enonce en entier, ouvrez deux fenetres cote-a-cote.
##somme_pairs([4, 7, 12, 0, 21, 5]) vaut 16 (car 16=4+12+0).
##nb_elem_pairs([4, 7, 12, 0, 21, 5]) vaut 3 (car 4, 12 et 0 sont pairs).
##max_pairs([4, 7, 12, 0, 21, 5]) vaut 12.
##min_pairs([4, 7, 12, 0, 21, 5]) vaut 0
##et min_pairs([9, 3, 1]) vaut None.
##indice_de(12, [4, 7, 12, 0, 21, 5]) vaut 2 (car 12 est placé à l'indice 2),
##et indice_de(6, [4, 7, 12, 0, 21, 5]) vaut None.
##trouve_premier_pair([1, 15, 4, 7, 12, 3]) vaut  4
##et trouve_premier_pair([1, 17, 7]) vaut  None.
##extrait_pairs([4, 7, 12, 0, 3]) vaut  [4, 12, 0]
##et extrait_pairs([21, 17, 3]) vaut  [ ].
