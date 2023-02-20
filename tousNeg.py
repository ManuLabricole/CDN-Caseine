# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.


number = float(input("Nombre ? "))
numberList = []
numberList.append(float(number))

if number == 0:
    print("Seulement 0")

else:
    while number != 0:

        number = float(input("Nombre ? "))
        numberList.append(number)

    if (all(val > 0 for val in numberList)):
        print("Tous +")
