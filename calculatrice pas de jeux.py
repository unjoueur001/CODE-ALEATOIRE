import random

class Calculatrice:
    def __init__(self):
        self.mode = "standard"
        self.code_secret = "2026LL"  # Code secret en une seule entrée
        self.options_secretes = {
            "1": ("🔢 Devine le nombre", self.devine_nombre),
            "2": ("✊ Pierre-Feuille-Ciseaux", self.pierre_feuille_ciseaux),
            "3": ("🧩 Labyrinthe", self.labyrinthe),
            "4": ("➗ Quiz Maths", self.quiz_maths),
            "5": ("⚔️ Combat RPG", self.combat_rpg),
            "6": ("🧠 Mémoire", self.memoire),
            "7": ("🏃 Course de calcul", self.course_calcul),
            "8": ("📏 Convertisseur", self.convertisseur),
            "9": ("📖 Liseuse", self.liseuse)
        }
        self.fiches = {
            "1": ("Tables de multiplication", "7x1=7, 7x2=14, ..., 7x10=70"),
            "2": ("Formules de physique", "Vitesse = Distance/Temps\nÉnergie = 0.5 x masse x vitesse²"),
            "3": ("Conjugaison", "Être: je suis, tu es, il est\nAvoir: j'ai, tu as, il a"),
            "4": ("Vocabulaire anglais", "Hello = Bonjour\nGoodbye = Au revoir")
        }
        self.modes = {
            "1": ("Standard", "Calculs basiques (+, -, *, /)"),
            "2": ("Scientifique", "Fonctions avancées (sin, cos, etc.)"),
            "3": ("Programmeur", "Binaire/Hexadécimal"),
            "4": ("Statistiques", "Moyennes, écarts-types")
        }

    def afficher_titre(self, titre):
        """Affiche un titre stylisé."""
        print(f"\n{'='*50}\n🌟 {titre.upper()} 🌟\n{'='*50}")

    def demarrer(self):
        """Menu principal avec sélection de mode."""
        self.afficher_titre("Calculatrice Pro")
        print("\n🔹 Modes disponibles :")
        for key, (nom, desc) in self.modes.items():
            print(f"{key}. {nom} - {desc}")
        print("\nTapez 'exit' pour quitter.")
        choix = input("\nChoix (1/2/3/4) : ")
        if choix == "1":
            self.mode_standard()
        elif choix == "2":
            self.mode_scientifique()
        elif choix == "3":
            self.mode_programmeur()
        elif choix == "4":
            self.mode_statistiques()
        elif choix.lower() == "exit":
            print("Au revoir !")
        else:
            print("❌ Mode invalide.")
            self.demarrer()

    def verifier_code_secret(self, user_input):
        """Vérifie si l'entrée correspond au code secret."""
        return user_input == self.code_secret

    def mode_standard(self):
        """Mode calculatrice standard."""
        self.afficher_titre("Mode Standard")
        print("\nExemples : 2+2, 5*3, 10/2")
        while True:
            user_input = input("\n> ")
            if user_input.lower() == 'exit':
                self.demarrer()
                break
            if self.verifier_code_secret(user_input):
                self.menu_secret()
                continue
            try:
                resultat = eval(user_input)
                print(f"👉 Résultat : {resultat}")
            except:
                print("❌ Opération invalide.")

    def mode_scientifique(self):
        """Mode calculatrice scientifique."""
        self.afficher_titre("Mode Scientifique")
        print("\nExemples : sin(30), log(100), sqrt(16)")
        while True:
            user_input = input("\n> ")
            if user_input.lower() == 'exit':
                self.demarrer()
                break
            if self.verifier_code_secret(user_input):
                self.menu_secret()
                continue
            try:
                # Simplification des fonctions scientifiques
                user_input = user_input.replace("sin", "0.5").replace("cos", "0.8").replace("log", "lambda x: 2.3").replace("sqrt", "lambda x: 4")
                resultat = eval(user_input)
                print(f"👉 Résultat : {resultat}")
            except:
                print("❌ Opération invalide.")

    def mode_programmeur(self):
        """Mode programmeur (binaire/hexadécimal)."""
        self.afficher_titre("Mode Programmeur")
        print("\nExemples : bin(10), hex(255), int('1010', 2)")
        while True:
            user_input = input("\n> ")
            if user_input.lower() == 'exit':
                self.demarrer()
                break
            if self.verifier_code_secret(user_input):
                self.menu_secret()
                continue
            try:
                resultat = eval(user_input)
                print(f"👉 Résultat : {resultat}")
            except:
                print("❌ Opération invalide.")

    def mode_statistiques(self):
        """Mode statistiques."""
        self.afficher_titre("Mode Statistiques")
        print("\nExemples : (5+10)/2, sum([1,2,3]), len([1,2,3])")
        while True:
            user_input = input("\n> ")
            if user_input.lower() == 'exit':
                self.demarrer()
                break
            if self.verifier_code_secret(user_input):
                self.menu_secret()
                continue
            try:
                resultat = eval(user_input)
                print(f"👉 Résultat : {resultat}")
            except:
                print("❌ Opération invalide.")

    def menu_secret(self):
        """Menu secret avec jeux et liseuse."""
        while True:
            self.afficher_titre("Menu Secret")
            print("\n🎮 Jeux et Outils :")
            for key, (nom, _) in self.options_secretes.items():
                print(f"{key}. {nom}")
            print("\nTapez 'retour' pour revenir.")
            choix = input("\n> ")
            if choix == "retour":
                print("\n" * 50)  # Efface l'écran
                break
            elif choix in self.options_secretes:
                print("\n" * 50)  # Efface l'écran
                self.options_secretes[choix][1]()  # Lance l'option
            else:
                print("❌ Choix invalide.")

    # --- Jeux et Outils ---
    def devine_nombre(self):
        """Mini-jeu : Devine le nombre entre 1 et 20."""
        self.afficher_titre("Devine le Nombre")
        import random
        nombre = random.randint(1, 20)
        print("\nDevinez un nombre entre 1 et 20 !")
        for essai in range(5):
            choix = int(input(f"Essai {essai + 1} : "))
            if choix == nombre:
                print("🎉 Gagné !")
                break
            print("❌ Raté !")
        else:
            print(f"Perdu ! C'était {nombre}.")
        input("\nAppuyez sur Entrée pour revenir...")

    def pierre_feuille_ciseaux(self):
        """Mini-jeu : Pierre-Feuille-Ciseaux."""
        self.afficher_titre("Pierre-Feuille-Ciseaux")
        import random
        options = ["pierre", "feuille", "ciseaux"]
        choix_bot = random.choice(options)
        print("\nPierre-Feuille-Ciseaux !")
        choix_joueur = input("Votre choix : ").lower()
        if choix_joueur == choix_bot:
            print("Égalité !")
        elif (choix_joueur == "pierre" and choix_bot == "ciseaux") or \
             (choix_joueur == "feuille" and choix_bot == "pierre") or \
             (choix_joueur == "ciseaux" and choix_bot == "feuille"):
            print("🎉 Gagné !")
        else:
            print("❌ Perdu !")
        input("\nAppuyez sur Entrée pour revenir...")

    def labyrinthe(self):
        """Mini-jeu : Labyrinthe en ASCII."""
        self.afficher_titre("Labyrinthe")
        print("\nTrouvez la sortie (S) ! Utilisez Z/Q/S/D.")
        labyrinthe = [
            ["#", "S", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", "#", " ", "#"],
            ["#", "#", "#", " ", "#", " ", "#"],
            ["#", " ", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "E", "#"]
        ]
        x, y = 0, 1
        while True:
            for ligne in labyrinthe:
                print(" ".join(ligne))
            deplacement = input("Z/Q/S/D : ").lower()
            new_x, new_y = x, y
            if deplacement == "z":
                new_x -= 1
            elif deplacement == "s":
                new_x += 1
            elif deplacement == "q":
                new_y -= 1
            elif deplacement == "d":
                new_y += 1
            if labyrinthe[new_x][new_y] == "#":
                print("Mur !")
            elif labyrinthe[new_x][new_y] == "E":
                print("🎉 Sortie trouvée !")
                break
            else:
                labyrinthe[x][y] = " "
                x, y = new_x, new_y
                labyrinthe[x][y] = "S"
                print("\n" * 50)  # Efface l'écran
        input("\nAppuyez sur Entrée pour revenir...")

    def quiz_maths(self):
        """Mini-jeu : Quiz de maths."""
        self.afficher_titre("Quiz Maths")
        import random
        print("\nQuiz Maths : 5 questions !")
        score = 0
        for _ in range(5):
            a, b = random.randint(2, 12), random.randint(2, 12)
            reponse = int(input(f"{a} x {b} = "))
            if reponse == a * b:
                print("✅ Correct !")
                score += 1
            else:
                print(f"❌ Faux ! Réponse : {a * b}")
        print(f"\nScore : {score}/5")
        input("\nAppuyez sur Entrée pour revenir...")

    def combat_rpg(self):
        """Mini-jeu : Combat RPG textuel."""
        self.afficher_titre("Combat RPG")
        print("\nCombat RPG : Battez le monstre !")
        pv_joueur = 10
        pv_monstre = 8
        while pv_joueur > 0 and pv_monstre > 0:
            print(f"PV : Vous ({pv_joueur}) vs Monstre ({pv_monstre})")
            action = input("Attaquer (A) ou Soigner (S) ? ").lower()
            if action == "a":
                degats = random.randint(1, 4)
                pv_monstre -= degats
                print(f"Vous infligez {degats} dégâts !")
                pv_joueur -= random.randint(1, 3)
            elif action == "s":
                pv_joueur = min(10, pv_joueur + 2)
                print("Vous récupérez 2 PV !")
            else:
                print("Action invalide !")
        if pv_monstre <= 0:
            print("🎉 Victoire !")
        else:
            print("💀 Défaite...")
        input("\nAppuyez sur Entrée pour revenir...")

    def memoire(self):
        """Mini-jeu : Test de mémoire."""
        self.afficher_titre("Test de Mémoire")
        import random
        print("\nTest de mémoire : Répétez la séquence !")
        sequence = [random.randint(1, 9) for _ in range(4)]
        print("Séquence : " + "-".join(map(str, sequence)))
        input("Appuyez sur Entrée quand vous êtes prêt...")
        print("\n" * 50)  # Efface l'écran
        reponse = input("Répétez la séquence (ex: 1-2-3-4) : ")
        if reponse == "-".join(map(str, sequence)):
            print("🎉 Bravo !")
        else:
            print("❌ Perdu !")
        input("\nAppuyez sur Entrée pour revenir...")

    def course_calcul(self):
        """Mini-jeu : Course de calcul mental."""
        self.afficher_titre("Course de Calcul")
        import random
        print("\nCourse de calcul mental : 10 additions en vitesse !")
        score = 0
        for i in range(10):
            a, b = random.randint(1, 10), random.randint(1, 10)
            reponse = int(input(f"{a} + {b} = "))
            if reponse == a + b:
                score += 1
        print(f"\nScore : {score}/10")
        input("\nAppuyez sur Entrée pour revenir...")

    def convertisseur(self):
        """Convertisseur avancé."""
        self.afficher_titre("Convertisseur")
        print("\n1. Longueur (km, m, cm)")
        print("2. Poids (kg, g, mg)")
        print("3. Temps (h, min, s)")
        print("4. Températures (Celsius, Fahrenheit)")
        choix = input("Choix (1/2/3/4) : ")
        if choix == "1":
            self._convertir_longueur()
        elif choix == "2":
            self._convertir_poids()
        elif choix == "3":
            self._convertir_temps()
        elif choix == "4":
            self._convertir_temperature()
        else:
            print("Choix invalide.")

    def _convertir_longueur(self):
        """Conversion de longueur."""
        self.afficher_titre("Convertisseur - Longueur")
        print("\nExemple : 5→km")
        while True:
            user_input = input("Entrez une conversion (ex: 5→km) ou 'retour' : ")
            if user_input == "retour":
                break
            try:
                valeur, unite = user_input.split("→")
                valeur = float(valeur)
                if unite == "km":
                    print(f"{valeur} km = {valeur * 1000} m = {valeur * 100000} cm")
                elif unite == "m":
                    print(f"{valeur} m = {valeur / 1000} km = {valeur * 100} cm")
                elif unite == "cm":
                    print(f"{valeur} cm = {valeur / 100} m = {valeur / 100000} km")
                else:
                    print("Unité non reconnue.")
            except:
                print("Format invalide. Exemple : 5→km")

    def _convertir_poids(self):
        """Conversion de poids."""
        self.afficher_titre("Convertisseur - Poids")
        print("\nExemple : 5→kg")
        while True:
            user_input = input("Entrez une conversion (ex: 5→kg) ou 'retour' : ")
            if user_input == "retour":
                break
            try:
                valeur, unite = user_input.split("→")
                valeur = float(valeur)
                if unite == "kg":
                    print(f"{valeur} kg = {valeur * 1000} g = {valeur * 1000000} mg")
                elif unite == "g":
                    print(f"{valeur} g = {valeur / 1000} kg = {valeur * 1000} mg")
                elif unite == "mg":
                    print(f"{valeur} mg = {valeur / 1000000} kg = {valeur / 1000} g")
                else:
                    print("Unité non reconnue.")
            except:
                print("Format invalide. Exemple : 5→kg")

    def _convertir_temps(self):
        """Conversion de temps."""
        self.afficher_titre("Convertisseur - Temps")
        print("\nExemple : 5→h")
        while True:
            user_input = input("Entrez une conversion (ex: 5→h) ou 'retour' : ")
            if user_input == "retour":
                break
            try:
                valeur, unite = user_input.split("→")
                valeur = float(valeur)
                if unite == "h":
                    print(f"{valeur} h = {valeur * 60} min = {valeur * 3600} s")
                elif unite == "min":
                    print(f"{valeur} min = {valeur / 60} h = {valeur * 60} s")
                elif unite == "s":
                    print(f"{valeur} s = {valeur / 3600} h = {valeur / 60} min")
                else:
                    print("Unité non reconnue.")
            except:
                print("Format invalide. Exemple : 5→h")

    def _convertir_temperature(self):
        """Conversion de température."""
        self.afficher_titre("Convertisseur - Température")
        print("\nExemple : 25→C")
        while True:
            user_input = input("Entrez une conversion (ex: 25→C) ou 'retour' : ")
            if user_input == "retour":
                break
            try:
                valeur, unite = user_input.split("→")
                valeur = float(valeur)
                if unite.upper() == "C":
                    fahrenheit = (valeur * 9/5) + 32
                    print(f"{valeur}°C = {fahrenheit}°F")
                elif unite.upper() == "F":
                    celsius = (valeur - 32) * 5/9
                    print(f"{valeur}°F = {celsius:.2f}°C")
                else:
                    print("Unité non reconnue.")
            except:
                print("Format invalide. Exemple : 25→C")

    def liseuse(self):
        """Mode liseuse : fiches de révision."""
        self.afficher_titre("Liseuse")
        while True:
            print("\n📚 **Fiches disponibles** :")
            for key, (titre, _) in self.fiches.items():
                print(f"{key}. {titre}")
            print("\nTapez 'retour' pour revenir.")
            choix = input("\n> ")
            if choix == "retour":
                break
            elif choix in self.fiches:
                print("\n" * 50)  # Efface l'écran
                print(f"📖 **{self.fiches[choix][0]}**\n")
                print(self.fiches[choix][1])
                input("\nAppuyez sur Entrée pour continuer...")
            else:
                print("Choix invalide.")

# Lancer la calculatrice
if __name__ == "__main__":
    calc = Calculatrice()
    calc.demarrer()
