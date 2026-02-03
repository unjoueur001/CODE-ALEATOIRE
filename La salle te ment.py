import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nAppuie sur Entrée...")

enigmes_faciles = [
    ("La sortie est ici", True),
    ("Cette porte est un piège", False),
    ("La sortie n'est pas ici", False),
]

enigmes_moyennes = [
    ("Au moins une autre porte ment", True),
    ("Toutes les portes disent vrai", False),
    ("Cette porte est sûre seulement si les autres mentent", False),
]

enigmes_dures = [
    ("Si cette phrase est fausse alors cette porte est sûre", True),
    ("Cette porte n'est pas fausse", False),
    ("Aucune porte sûre n'est fausse", False),
]

score = 0

while True:
    clear()

    if score < 3:
        pool = enigmes_faciles
        niveau = "FACILE"
    elif score < 6:
        pool = enigmes_moyennes
        niveau = "MOYEN"
    else:
        pool = enigmes_dures
        niveau = "DUR"

    bonne_porte = random.randint(1, 3)

    print("🧩 LA SALLE QUI MENT")
    print(f"🎯 Score : {score} | 🔥 Difficulté : {niveau}\n")

    portes = {}
    for i in range(1, 4):
        phrase, verite = random.choice(pool)
        portes[i] = (phrase, verite if i == bonne_porte else not verite)
        print(f"Porte {i} : {phrase}")

    choix = input("\nQuelle porte choisis-tu ? (1-3) : ")

    if choix.isdigit() and int(choix) == bonne_porte:
        score += 1
        print("\n✅ Bonne porte. La salle tremble...")
        pause()
    else:
        print("\n💀 MAUVAIS CHOIX.")
        print(f"🏁 Score final : {score}")
        break
