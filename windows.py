
# Laurence doit gérer les stocks d'un entrepôt de fenêtres, semaine par semaine.
# Le stock de la semaine 1 est 1024 fenêtres. De plus, elle a réussi à obtenir les prévisions suivantes :
# pendant la semaine n, le nombre de fenêtres qui partent de l'entrepôt (en direction des magasins) est 20+n.
# De plus, si le numéro de semaine est un multiple de 4, alors l'entrepôt reçoit une livraison de 500 fenêtres
# venant de l'usine de production.
# Donc le stock de la semaine 1 est 1024, le stock de la semaine 2 est 1024-(20+2)=1002,
# le stock de la semaine 3 est 1002-(20+3)=979, le stock de la semaine 4 est 979-(20+4)+500=1455, etc.
# Cet exercice est dédié à la conception d'un programme aidant Laurence dans sa gestion des stocks et suivant le cahier des charges décrit ci-dessous.

# Le programme doit commencer par afficher le menu suivant:

# --> a. Prévisions de stock
# --> b. Stock maximal
# --> (q pour quitter)
# Si Laurence tape q , le programme s'arrête.
# Si Laurence tape a , le programme lui demande un numéro de semaine n puis affiche les prévisions de stock de la semaine 1 à la semaine n.


def computeWeeklyStock(week):

    stock = 1024
    stock_week_1 = 1024

    for i in range(1, week):
        if (i % 4 == 0):
            stock += 500 - (20+i)
            print("Semaine " + str(i) + " : stock " + str(stock))
        else:
            stock += stock - (20+i)
            print("Semaine " + str(i) + " : stock " + str(stock))


def predictStock(week):

    stock = 1024
    stock_week_1 = 1024

    stockList = []
    stockList.append(stock_week_1)

    for i in range(1, week):
        if (i % 4 == 0):
            stock += 500 - (20+i)
        else:
            stock += stock - (20+i)
        stockList.append(stock)

    maxStock = max(stockList)
    print(maxStock)

    return None


def computeMaximalStock(n: int) -> int:
    return None


def getMenuChoice(answer) -> str:

    if answer == "a":
        week = int(input("Week number for stock amount ? : "))
        predictStock(week)

    elif answer == "b":
        week = int(input("Week number for max stock in between ? : "))
        computeMaximalStock(week)

    elif answer == "q":
        return

    else:
        answerErr = input("Choix incorrect, recommencez ")
        getMenuChoice(answerErr)

    return


# Display Menu
print("a. Prévisions de stock")
print("b. Stock maximal")
print("(q pour quitter)")

answer = input()
getMenuChoice()
