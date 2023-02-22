# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

def ajoute1(stock:dict, fruit:str) -> dict:
    
    newStock = dict(stock)
    
    if fruit in newStock:
        newStock[fruit] += 1
    else:
       newStock[fruit] = 1 
    
    return newStock

def enleve1(stock:dict, fruit:str) -> dict:
    newStock = dict(stock)
    
    if fruit in newStock:
        if newStock[fruit] > 1:
            newStock[fruit] -= 1
        elif newStock[fruit] == 1:
            del newStock[fruit]
    
    else:
        print(f'Quantite insuffisante de {fruit}')
         
    return newStock

def ajoute(stock:dict, fruit:str, quantite:int) -> dict:
    
    newStock = dict(stock)
    
    for i in range(quantite):
        newStock = ajoute1(newStock, fruit)

    return newStock

def enleve(stock:dict, fruit:str, quantite:int) -> dict:
    
    newStock = dict(stock)
    
    if fruit in newStock and newStock[fruit] >= quantite:
    
        for i in range(quantite):
            newStock = enleve1(newStock, fruit)
            
    else:
        print(f'Quantite insuffisante de {fruit}')

    return newStock
        
def apres_livraison(stock: dict,  livraison:dict) -> dict:
    
    newStock = dict(stock)
    
    for fruit in livraison:
        newStock = ajoute(stock=newStock, fruit=fruit, quantite=livraison[fruit])
    
    return newStock
        
def commande(stock:dict, stockVoulu:dict) -> dict:
    
    stockCommande = {}
    
    for fruit in stockVoulu:
        if fruit in stock:
            if stock[fruit] < stockVoulu[fruit]:
                stockCommande[fruit] = stockVoulu[fruit] - stock[fruit]
            else:
                pass
        
        else:
            stockCommande[fruit] = stockVoulu[fruit]
                
    return stockCommande

def total(stock:dict) -> int:
    totalFruit = 0
    for fruit in stock:
        totalFruit += stock[fruit]
    
    return totalFruit

def quantite(stock:dict, fruitList:list) -> int:
    quantiteFruits = 0
    
    for fruit in fruitList:
        if fruit in stock:
            quantiteFruits += stock[fruit]
        else:
            pass
    
    return quantiteFruits

def quantite_agrumes(stock:dict) -> int:
    agrumes=['orange', 'citron', 'mandarine', 'clementine', 'pamplemousse']
    
    return quantite(stock=stock, fruitList=agrumes)

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    agrumes=['orange', 'citron', 'mandarine', 'clementine', 'pamplemousse']
    print(enleve1({'pomme' : 2, 'banane' : 6, 'poire' : 1} , 'poire'))

# Copier-coller des exemples:
##ajoute1(stock , 'pomme') renvoie {'pomme' : 3, 'banane' : 6}
##ajoute1(stock , 'poire') renvoie {'pomme' : 2, 'banane' : 6, 'poire' : 1}
##
##enleve1(stock , 'pomme') renvoie {'pomme' : 1, 'banane' : 6}
##enleve1(stock , 'poire') affiche "Erreur: Quantité insuffisante de poire"
##et renvoie {'pomme' : 2, 'banane' : 6}
##
##ajoute(stock , 'pomme', 5) renvoie {'pomme' : 7, 'banane' : 6}
##ajoute(stock , 'poire', 4) renvoie {'pomme' : 2, 'banane' : 6, 'poire' : 4}
##
##enleve(stock , 'pomme', 2) renvoie {'banane' : 6}
##enleve(stock , 'banane', 10) affiche "Erreur: Quantité insuffisante de banane"
##et renvoie {'pomme' : 2, 'banane' : 6}
##
##apres_livraison(stock , {'peche' : 4, 'pomme' : 5}) renvoie {'pomme' : 7, 'banane' : 6, 'peche' : 4}
##
##En supposant que stock_voulu={'pomme': 15, 'orange': 20},
##alors commande(stock , stock_voulu) renvoie {'pomme' : 13, 'orange' : 20}.
##En supposant que stock_voulu={'pomme': 10, 'banane': 4},
##alors commande(stock , stock_voulu) renvoie {'pomme' : 8}.
##
##total(stock) renvoie 8.
##
##En supposant que stock_bis={'pomme': 15, 'peche': 4, 'citron': 3, 'orange': '20'},
##alors quantite(stock_bis , ['pomme', 'citron', 'poire']) renvoie 18.
##
##En supposant que stock_bis={'pomme': 15, 'peche': 4, 'citron': 3, 'orange': '20'},
##alors quantite_agrumes(stock_bis) renvoie 23.

