# Required Files: student.py (Télécharger)
# Nombre maximal de fichiers: 5
# Type de travail: Travail individuel

# Vous partez à la recherche d'un trésor caché dans une pyramide. 
# Vous avez réussi à obtenir des informations sur les épreuves qui vous attendent à l'intérieur de celle-ci:

# - dans le hall d'entrée, une statue de sphinx va vous demander un code secret sous la forme suivante : 

# "Je n'aime que les nombres p qui sont des nombres premiers, tels que p+2 soit aussi un nombre  premier... 
# Et mon nombre préféré de la journée est  *un nombre qui change tous les jours*. 
# 
# Le code secret est le plus petit nombre supérieur ou égal à mon nombre préféré parmi les nombres que j'aime."

# - une fois entré, vous parcourez un labyrinthe dont vous vous êtes déjà procuré le plan, puis vous arrivez face à une statue d'Osiris qui garde la salle du trésor. 
# Il va vous demander un code secret sous la forme suivante: 

# "Je n'aime que les nombres n tels que n+1 soit une puissance de 2.... 
# et il faut également que le reste de la division de n par 5 soit égal à 3... 
# Mon nombre préféré de la journée est *un nombre qui change tous les jours*. 
# Le code secret est le plus petit nombre supérieur ou égal à mon nombre préféré, parmi les nombres que j'aime."

# Pour chacune des deux énigmes, vous n'aurez que 5 secondes pour répondre, sinon la sortie sera verrouillée et vous resterez enfermés dans la pyramide à tout jamais. 
# Pour éviter cela à tout prix, vous décidez d'écrire un programme que vous emporterez sur votre smartphone et qui vous aidera à résoudre les énigmes. Pour cela:

#     Ecrire une fonction est_premier qui prend en argument un entier supérieur ou égal à 2 et qui renvoie True si l'entier en premier, False sinon.
#     Ecrire une fonction sphinx_aime qui prend en argument un entier supérieur ou égal à 2 et qui renvoie True si l'entier est un nombre que le sphinx aime, False sinon.
#     Ecrire une fonction code_hall qui prend en argument le nombre préféré du sphinx ce jour-là (un entier strictement positif) et qui renvoie le code secret du hall.
#     Ecrire une fonction est_puissance2 qui prend en argument un entier positif et qui renvoie True s'il s'agit d'une puissance de 2, False sinon.
#     Ecrire une fonction osiris_aime qui prend en argument un entier positif et qui renvoie True si Osiris aime cet entier, False sinon.
#     Ecrire une fonction code_tresor qui prend en argument le nombre préféré d'Osiris ce jour-là (un entier strictement positif) 
# et qui renvoie le code secret permettant d'accéder au trésor.

# Par exemple, si le nombre préféré du sphinx est 15, alors le code secret du hall ce jour-là est 17 (car 17 et 19 sont premiers). 
# Si le nombre préféré d'Osiris ce jour-là est 20, alors le code secret de la salle du trésor est 63 (car 63+1 est une puissance de 2, et 63= 12 x 5+3).

def est_premier(num:int) -> bool:
    num = int(num)
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                # print("Pas premier, divisible par" + str(i))
                return False

            else:
                pass# print("Premier, non divisible par :" + str(i))
        return True
    
def sphinx_aime(p:int) -> bool:
    if est_premier(p) and est_premier(p+2):
        return True
    else:
        return False
    
def code_hall(p) -> int:
    
    while (sphinx_aime(p) == False):
        p += 1
        
    return p

def est_puissance2(num : int) -> bool:
    
    num = float(num)
    while ( num.is_integer() and num > 1):
        num = num/2

    if num == 1:
        return True
    else:
        return False
    
def osiris_aime(n : int) -> bool:
    
    if est_puissance2(n+1):
        if n%5 == 3:
            return True
    return False

def code_tresor(num : int) -> int:
    
    while (osiris_aime(num) == False):
        num += 1
        
    return num

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    # Vos tests ici
    
    # Fin de vos tests
    # Ci-dessous: programme qui simule votre entree dans la pyramide
    # Vous devez juste appuyer sur Entree lorsque l'on vous le demande.
    import Theme_5.pyramide as pyramide
    # pyramide.entre() # Vous pouvez commenter cette ligne si vous le voulez.
    print(osiris_aime(31))