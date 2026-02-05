import random

def jeu_du_nombre_mystere():
    nombre = random.randint(1, 100)
    essais = 0

    print("Devinez le nombre mystère entre 1 et 100 !")

    while True:
        essai = int(input("Votre proposition : "))
        essais += 1

        if essai < nombre:
            print("Trop petit !")
        elif essai > nombre:
            print("Trop grand !")
        else:
            print(f"Bravo ! Vous avez trouvé en {essais} essais.")
            break

jeu_du_nombre_mystere()

