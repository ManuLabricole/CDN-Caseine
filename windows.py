
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


def predictStock(week):

    stock = 1024
    stock_week_1 = 1024
    print("Semaine 1 : stock " + str(stock))

    for i in range(2, week+1):
        if (i % 4 == 0):
            stock += 500 - (20+i)
            print("Semaine " + str(i) + " : stock " + str(stock))
        else:
            stock -= (20+i)
            print("Semaine " + str(i) + " : stock " + str(stock))
    predictorWindowsApp()


def computeMaximalStock(week):

    print(type(week))

    stock = 1024
    stock_week_1 = 1024

    stockList = []
    stockList.append(stock_week_1)

    for i in range(1, week+1):
        if i == 1:
            pass
        elif (i % 4 == 0):
            stock += 500 - (20+i)
        else:
            stock -= (20+i)

        stockList.append(stock)

    maxStock = max(stockList)
    index = stockList.index(maxStock)
    print("" + str(maxStock) + " , atteint en semaine " + str(index+1))

    predictorWindowsApp()


def getMenuChoice(answer) -> str:

    if answer == "a":
        week = int(input("Choisissez une semaine : "))
        predictStock(week)

    elif answer == "b":
        week = int(input("Choisissez une semaine : "))
        computeMaximalStock(week)

    elif answer == "q":
        return

    else:
        answerErr = input("Choix incorrect, recommencez ")
        getMenuChoice(answerErr)

    return


# -----------------------------------------------------------
# Display Menu
def predictorWindowsApp():
    print("a. Prévisions de stock")
    print("b. Stock maximal")
    print("(q pour quitter)")

    answer = input()
    getMenuChoice(answer)


predictorWindowsApp()
