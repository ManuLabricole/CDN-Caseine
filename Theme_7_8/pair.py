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
            
    if len(pairList) > 0:
        return pairList
    else:
        return None

def somme_pairs(numList:list) -> int:

    numListCopy = numList.copy()
    pairList = make_pair_list(numListCopy)
    
    return sum(pairList)
    

def nb_elem_pairs(numList:list) -> int:
    
    numListCopy = numList.copy()
    pairList = make_pair_list(numListCopy)
    
    if pairList is not None:
        return len(pairList)
    else:
        return 0

def max_pair(numList:list) -> list:
    
    numListCopy = numList.copy()
    pairList = make_pair_list(numListCopy)
    
    if pairList is not None:
        return max(pairList)
    else:
        return None

def min_pair(numList:list) -> list:
    
    numListCopy = numList.copy()
    pairList = make_pair_list(numListCopy)
    
    if pairList is not None:
        return min(pairList)
    else:
        return None
    
def indice_de(position:int, numList:list):
    numListCopy = numList.copy()
    if position in numListCopy:
        return numListCopy.index(int(position))
    
    else:
        return None
    
def trouve_premier_pair(numList:list) -> list:
    
    for el in numList:
        if is_pair(el):
            return el
    else:
        return None
    
def extrait_pairs(numList:list) -> list:
    
    listPair = make_pair_list(numList)
    
    if listPair is not None:
        return listPair
    else:
        return []



if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    print(is_pair(8))
    print(make_pair_list([4, 5, 10, 12, 7, 13, 20]))
    print(somme_pairs([4, 7, 12, 0, 21, 5]))
    
    print(indice_de(32, [4, 6, 102, 5, 25, 14, 50, 16]))


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
