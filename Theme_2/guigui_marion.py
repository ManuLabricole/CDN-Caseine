# Ecrivez votre programme ci-dessous
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


print("Lancement de la gestion des comptes? ")
answer = input()

if answer == "oui":
    print("Solde du compte de Guillaume?")
    accountGui = float(input())

    print("Solde du compte de Marion?")
    accountMar = float(input())

    # Both are positive
    if (accountGui > 0 and accountMar > 0):
        print("Tous les deux en positif!")

    # Both are negative
    elif (accountGui < 0 and accountMar < 0):
        print("Tous les deux en negatif !")

    # Guillaume is negative
    elif accountGui < 0 and accountMar > 0:
        print("Guillaume est en negatif")
        # Guillaume peut l aider
        if abs(accountGui) < abs(accountMar):
            print("Marion peut lui transférer : " + str(abs(accountGui)))
            print("(Il lui restera :" + " " +
                  str(abs(accountMar)-abs(accountGui)) + "euros)")
        else:
            print("Impossible de retablir la situation")

    elif accountMar < 0 and accountGui > 0:
        print("Marion est en negatif")
    # Guillaume peut l aider
        if abs(accountMar) < abs(accountGui):
            print("Guillaume peut lui transférer : " + str(abs(accountMar)))
            print("(Il lui restera :" + " " +
                  str(abs(accountGui)-abs(accountMar)) + "euros)")
        else:
            print("Impossible de retablir la situation")


elif answer == "non":
    print("Ok, A bientot.")

else:
    print("Please answer by 'oui' ou 'non'")
