# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

# M. Bizarre est rédacteur-en-chef d’un journal, et a souvent des idées farfelues. Suivant les jours de la semaine,
# il souhaite que les articles de son journal suivent des règles qu’il a inventées.

# Chaque lundi, il souhaite que les mots soient répétés deux fois, séparés par un espace.
# Ecrivez une fonction lundi qui prend en argument un mot et qui transforme ce mot selon la règle du lundi.
# Par exemple, lundi("bonjour") doit valoir "bonjour bonjour".

# Chaque mardi, il faut que les mots de longueur paire soit répétés 6 fois, en séparant par un tiret,
# alors que les mots de longueur impaire doivent être répétés 3 fois, en séparant par des virgules.
# Ecrire la fonction mardi qui prend en argument un mot et qui renvoie la chaîne de caractères suivant la règle du mardi.
#
# Rappel : la longueur d’une chaîne de caractères est donnée par len(chaine).

# Chaque mercredi, il faut que les mots de longueur impaire soit remplacés par le mot "impair".
# Les mots pairs doivent rester tels qu’ils sont.
# Ecrire la fonction mercredi (qui prend en argument un mot et qui renvoie la bonne chaîne de caractères).

# Chaque jeudi, il faut que les mots soient répétés autant de fois que leur longueur modulo 3 (à la suite, sans espace).
# Ecrire la fonction jeudi. Par exemple, jeudi("merci") vaut "mercimerci", jeudi("bonbon") vaut "", jeudi("comment") vaut "comment".

# Le vendredi, il faut que les mots soient écrits normalement. Et heureusement, il n’y a pas de journal le week-end
# Ecrire une fonction transforme(mot, num_jour) qui prend en argument un mot et le numéro du jour (1 pour lundi, 2 pour mardi, etc....)
# et qui renvoie le mot transformé selon la règle du jour correspondant.
# (Exercice proposé par Aurélie Lagoutte)

def lundi(word: str) -> str:
    transformedWord = word + " " + word
    return transformedWord


def mardi(word):
    transformedWord = word
    if len(word) % 2 == 0:
        for i in range(1, 6):
            transformedWord += "-" + word
    else:
        for i in range(1, 3):
            transformedWord += "," + word

    return transformedWord


def mercredi(word):
    if len(word) % 2 == 0:
        return word
    else:
        return "impair"


def jeudi(word):
    moduloNum = len(word) % 3
    return moduloNum*word


if __name__ == "__main__":  # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")

    print(lundi("bonjour"))
    print(mardi("deux"))
    print(mercredi("impairetrr"))
    print(jeudi("comment"))
