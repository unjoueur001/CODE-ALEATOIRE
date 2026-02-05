import random

def jeu_pierre_feuille_ciseaux():
    options = ["pierre", "feuille", "ciseaux"]

    print("Bienvenue au jeu Pierre-Feuille-Ciseaux !")
    print("Choisissez : pierre, feuille ou ciseaux.")

    while True:
        joueur = input("Votre choix : ").lower()
        if joueur not in options:
            print("Choix invalide. Réessayez.")
            continue

        ordinateur = random.choice(options)
        print(f"L'ordinateur a choisi : {ordinateur}")

        if joueur == ordinateur:
            print("Égalité !")
        elif (joueur == "pierre" and ordinateur == "ciseaux") or \
             (joueur == "feuille" and ordinateur == "pierre") or \
             (joueur == "ciseaux" and ordinateur == "feuille"):
            print("Vous gagnez !")
        else:
            print("Vous perdez !")

        if input("Rejouer ? (o/n) ").lower() != "o":
            break

jeu_pierre_feuille_ciseaux()
