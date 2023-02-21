# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

def maximum(num1: float, num2: float) -> float:
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return None


def maximum3(num1: float, num2: float, num3: float) -> float:
    return maximum(num1=maximum(num1=num1, num2=num2), num2=num3)


def maximum3_input():
    num1 = float(input("num 1 : "))
    num2 = float(input("num 2 : "))
    num3 = float(input("num 3 : "))

    return maximum3(num1=num1, num2=num2, num3=num3)


if __name__ == "__main__":  # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    print(maximum(3, 4))
    print(maximum3(3, 4, 1))
