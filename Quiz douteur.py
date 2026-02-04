import random
import time
import json
import os

# --- Constantes ---
DIFFICULTES = {
    "Facile": 10,
    "Moyen": 20,
    "Expert": 50
}

THEMES = {
    "Art": [
        {
            "question": "Qui a peint la Joconde ?",
            "reponses": ["Léonard de Vinci", "Michel-Ange", "Raphaël", "Donatello"],
            "bonne_reponse": 1,
            "explication": "La Joconde a été peinte par Léonard de Vinci entre 1503 et 1506."
        },
        {
            "question": "Quel artiste a sculpté la statue de David ?",
            "reponses": ["Michel-Ange", "Donatello", "Bernini", "Léonard de Vinci"],
            "bonne_reponse": 1,
            "explication": "La statue de David a été sculptée par Michel-Ange entre 1501 et 1504."
        }
    ],
    "Science": [
        {
            "question": "Qui a inventé le télescope ?",
            "reponses": ["Galilée", "Newton", "Copernic", "Kepler"],
            "bonne_reponse": 1,
            "explication": "Galilée a perfectionné le télescope en 1609, bien que Hans Lippershey en ait breveté un en 1608."
        },
        {
            "question": "Quel savant a décrit la circulation sanguine ?",
            "reponses": ["William Harvey", "Galien", "Hippocrate", "Vésale"],
            "bonne_reponse": 1,
            "explication": "William Harvey a décrit la circulation sanguine en 1628."
        }
    ],
    "Philosophie": [
        {
            "question": "Qui a écrit 'Le Prince' ?",
            "reponses": ["Machiavel", "Platon", "Aristote", "Socrate"],
            "bonne_reponse": 1,
            "explication": "'Le Prince' a été écrit par Nicolas Machiavel en 1532."
        },
        {
            "question": "Quel philosophe a dit 'Je pense, donc je suis' ?",
            "reponses": ["Descartes", "Socrate", "Platon", "Kant"],
            "bonne_reponse": 1,
            "explication": "Cette citation est de René Descartes, dans 'Discours de la méthode' (1637)."
        }
    ]
}

# --- Classes ---
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0
        self.vies = 3
        self.niveau = "Moyen"
        self.historique = []
        self.derniere_question = None

    def ajouter_score(self, points):
        self.score += points
        print(f"Bravo ! +{points} points. Score total : {self.score}")

    def perdre_vie(self):
        self.vies -= 1
        print(f"Mauvaise réponse ! Il te reste {self.vies} vies.")
        if self.vies <= 0:
            print("Game Over !")
            return False
        return True

    def sauvegarder_score(self):
        if not os.path.exists("scores.json"):
            with open("scores.json", "w") as f:
                json.dump([], f)

        with open("scores.json", "r+") as f:
            scores = json.load(f)
            scores.append({"nom": self.nom, "score": self.score})
            f.seek(0)
            json.dump(scores, f, indent=4)
        print("Score sauvegardé !")

    def charger_classement(self):
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as f:
                scores = json.load(f)
                scores_sorted = sorted(scores, key=lambda x: x["score"], reverse=True)
                print("\n--- Classement ---")
                for i, entry in enumerate(scores_sorted[:5], 1):
                    print(f"{i}. {entry['nom']} : {entry['score']} points")
        else:
            print("Aucun score sauvegardé.")

# --- Fonctions ---
def choisir_theme():
    return random.choice(list(THEMES.keys()))

def choisir_question(theme):
    return random.choice(THEMES[theme])

def poser_question(question_data):
    print(f"\nQuestion : {question_data['question']}")
    for i, reponse in enumerate(question_data["reponses"], 1):
        print(f"{i}. {reponse}")

    # Minuterie
    for i in range(10, 0, -1):
        print(f"Temps restant : {i} secondes   ", end="\r")
        time.sleep(1)
    print("                                       ", end="\r")

    # Réponse du joueur
    try:
        choix = int(input("\nTa réponse (1/2/3/4) : ")) - 1
        if 0 <= choix < 4:
            return choix == question_data["bonne_reponse"]
        else:
            print("Choix invalide. Réponse comptée comme fausse.")
            return False
    except ValueError:
        print("Entrée invalide. Réponse comptée comme fausse.")
        return False

def afficher_explication(question_data):
    print(f"Explication : {question_data['explication']}")

def choisir_difficulte():
    print("\nChoisis une difficulté :")
    for i, diff in enumerate(DIFFICULTES.keys(), 1):
        print(f"{i}. {diff}")
    choix = int(input("1/2/3 : ")) - 1
    return list(DIFFICULTES.keys())[choix]

def afficher_regles():
    print("""
    --- Règles du Quiz Renaissance ---
    1. Réponds correctement aux questions pour gagner des points.
    2. Tu as 3 vies. Une mauvaise réponse = -1 vie.
    3. Chaque question a un temps limité (10 secondes).
    4. Plus la difficulté est élevée, plus les points sont importants.
    5. Sauvegarde ton score pour figurer dans le classement !
    """)

# --- Boucle principale ---
def main():
    print("Bienvenue dans le Quiz Renaissance ! 🎨🔬")
    nom = input("Quel est ton nom, érudit ? ")
    joueur = Joueur(nom)

    while True:
        print("\n--- Menu Principal ---")
        print("1. Jouer")
        print("2. Voir le classement")
        print("3. Quitter")
        choix = input("Choisis une option (1/2/3) : ")

        if choix == "1":
            afficher_regles()
            joueur.niveau = choisir_difficulte()
            joueur.vies = 3
            joueur.score = 0

            while joueur.vies > 0:
                theme = choisir_theme()
                print(f"\nThème : {theme}")
                question = choisir_question(theme)
                joueur.derniere_question = question

                if poser_question(question):
                    joueur.ajouter_score(DIFFICULTES[joueur.niveau])
                    afficher_explication(question)
                else:
                    if not joueur.perdre_vie():
                        break

            joueur.sauvegarder_score()

        elif choix == "2":
            joueur.charger_classement()

        elif choix == "3":
            print("À bientôt, érudit !")
            break

        else:
            print("Option invalide. Réessaye.")

if __name__ == "__main__":
    main()
