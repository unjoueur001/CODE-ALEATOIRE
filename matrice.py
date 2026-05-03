import os
import random
import time

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def main():
    # Passer en plein écran (simulé)
    os.system("mode con: cols=200 lines=50")

    # Changer la couleur de fond en vert
    os.system("color 0A")

    # Afficher un message pour simuler une activité
    print("\n" * 10)
    print(" " * 60 + "IP en cour de rechercher")
    print(" " * 55 + "fichier en cour de recherche...")
    print("\n" * 2)

    # Boucle infinie pour générer des IP
    try:
        while True:
            ip = generate_random_ip()
            print(f"IP trouvée : {ip} - infiltration en cours...")
            time.sleep(0.02)
    except KeyboardInterrupt:
        print("\n\nFermeture du programme...")

if __name__ == "__main__":
    main()
