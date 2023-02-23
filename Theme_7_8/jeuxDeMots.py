# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


def commence_par(lettre: str, mot: str) -> bool:
    listMot = list(mot)

    if len(listMot) > 0:
        #
        if listMot[0] == lettre:
            return True
        else:
            return False

    else:
        raise ValueError("Empty string")


def is_voyelle(letter: str) -> bool:
    voyelleList = ["a", "e", "i", "o", "u", "y"]

    if letter in voyelleList:
        # return not
        return True
    else:
        return False


def contient_voyelle(mot: str) -> bool:

    listMot = list(mot)
    boolValue = False

    for letter in listMot:

        if is_voyelle(letter):
            boolValue = True
        else:
            pass

    return boolValue


def get_consonne_index(mot: str) -> list:
    listMot = list(mot)
    indexConsonne = list()

    for i in range(len(listMot)):
        if is_voyelle(listMot[i]):
            pass
        else:
            indexConsonne.append(i)

    return indexConsonne


def derniere_consonne(mot: str) -> tuple:

    indexConsonne = get_consonne_index(mot)

    if indexConsonne is not None:
        return max(indexConsonne), list(mot)[max(indexConsonne)]
    else:
        return None


def double_consonne(mot: str):
    listMot = list(mot)
    indexConsonne = get_consonne_index(mot)

    for i in range(len(indexConsonne)-1):
        if (indexConsonne[i+1]-indexConsonne[i] == 1) and listMot[indexConsonne[i+1]] == listMot[indexConsonne[i]]:
            return True, listMot[indexConsonne[i]]

    return (False, None)


def envers(List: list) -> list:
    return list(reversed(List))


def palindrome(mot: str) -> bool:
    listMot = list(mot)

    if listMot == envers(listMot):
        return True
    else:
        return False


def mot_autorise(mot, listInterdit: str) -> bool:
    autorise = True

    if mot in listInterdit:
        autorise = False

    return autorise


if __name__ == "__main__":  # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")

    # Exemple de transformation d'un mot en liste

    print(double_consonne("reussite"))
