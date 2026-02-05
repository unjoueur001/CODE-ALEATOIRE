import random

def choisir_mot():
    mots = ["python", "programmation", "ordinateur", "clavier", "jeu", "devine", "algorithme"]
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    return " ".join(lettre if lettre in lettres_trouvees else "_" for lettre in mot)

def jeu_du_pendu():
    mot = choisir_mot()
    lettres_trouvees = set()
    essais = 6
    lettres_essayees = set()

    print("Bienvenue au jeu du Pendu ! Devinez le mot.")

    while essais > 0:
        print("\nMot :", afficher_mot_cache(mot, lettres_trouvees))
        print(f"Lettres essayées : {', '.join(sorted(lettres_essayees))}")
        print(f"Essais restants : {essais}")

        if all(lettre in lettres_trouvees for lettre in mot):
            print("\nFélicitations, vous avez gagné ! Le mot était :", mot)
            break

        lettre = input("Proposez une lettre : ").lower()

        if lettre in lettres_essayees:
            print("Vous avez déjà essayé cette lettre.")
            continue

        lettres_essayees.add(lettre)

        if lettre in mot:
            lettres_trouvees.add(lettre)
        else:
            essais -= 1
            print("Lettre incorrecte !")

    if essais == 0:
        print("\nDésolé, vous avez perdu ! Le mot était :", mot)

jeu_du_pendu()

