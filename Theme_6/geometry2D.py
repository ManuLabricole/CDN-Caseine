    # Écrire une fonction coord_centre_cercle qui prend en arguments les coordonnées x1, y1, x2, y2 
    #   de deux points diamétralement opposés sur un cercle (par exemple, comme sur la figure (a)), 
    #   et qui renvoie les coordonnées x, y du centre du cercle.
    
    # Écrire une fonction coord_bas_losange qui prend en arguments les coordonnées x1,y1,x2,y2 
    #   de deux points placés sur un losange vertical comme à la figure (b) 
    #   (le premier sur le sommet gauche, le second sur le sommet supérieur) et qui 
    #   renvoie les coordonnées x, y du sommet inférieur du losange.
    
    # Écrire une fonction coordDEF qui ne prend pas d'argument, et qui demande à l'utilisateur les coordonnées des points A, B, C 
    #   de la figure (c) (dans cet ordre, en commençant pour chaque point par l'abscisse pour l'ordonnée), 
    #   puis qui renvoie 6 valeurs de retours xD, yD, xE, yE, xF, yF correspondant aux coordonnées des points D, E, F dans cet ordre.

def coord_centre_cercle(x1:float, y1:float, x2:float, y2:float):
    return ((x1+x2)/2 , (y1+y2)/2)

def coord_bas_losange(x1:float, y1:float, x2:float, y2:float):
    return (x2, y1-abs(y2-y1))

def coordDEF():
    xA = float(input("xA = "))
    yA = float(input("yA = "))
    xB = float(input("xB = "))
    yB = float(input("yB = "))
    xC = float(input("xC = "))
    yC = float(input("yC = "))
    
    E = coord_bas_losange(x1=xA, y1=yA, x2=xB, y2=yB)
    xE = E[0]
    yE = E[1]
    
    D = coord_centre_cercle(x1=xA, y1=yA, x2=xB, y2=yB)
    xD = D[0]
    yD = D[1]
    F = coord_centre_cercle(x1=xE, y1=yE, x2=xC, y2=yC)
    xF = F[0]
    yF = F[1]
    
    
    
    return (xD, yD, xE,yE, xF, yF)
    
    
    

if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    coordDEF()




