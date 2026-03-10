import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Amélioré")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Chargement des images (à remplacer par tes propres sprites)
# Exemple : player_img = pygame.image.load("vaisseau1.png")
player_imgs = [
    pygame.Surface((50, 30)),  # Remplace par tes images
    pygame.Surface((50, 30))
]
enemy_imgs = [
    pygame.Surface((30, 30)),  # Ennemis rapides
    pygame.Surface((50, 50))   # Tanks
]
projectile_img = pygame.Surface((5, 10))

# Vaisseau du joueur
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 50
player_speed = 5
current_player_img = 0

# Projectiles
projectiles = []
projectile_speed = 7

# Ennemis
enemies = []
enemy_spawn_rate = 30

# Code Konami
konami_code = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN,
               pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT,
               pygame.K_b, pygame.K_a]
konami_index = 0
konami_active = False

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Boucle principale
clock = pygame.time.Clock()
running = True
frame_count = 0

def spawn_enemy():
    enemy_type = random.choice(["rapide", "tank"])
    x = random.randint(0, WIDTH - 50)
    y = random.randint(-50, -10)
    if enemy_type == "rapide":
        enemies.append({"x": x, "y": y, "type": "rapide", "speed": 3, "health": 1})
    else:
        enemies.append({"x": x, "y": y, "type": "tank", "speed": 1, "health": 3})

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectiles.append({"x": player_x + 22, "y": player_y})
            # Vérification du code Konami
            if event.key == konami_code[konami_index]:
                konami_index += 1
                if konami_index == len(konami_code):
                    konami_active = True
                    konami_index = 0
            else:
                konami_index = 0

    # Déplacement du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    # Génération d'ennemis
    frame_count += 1
    if frame_count % enemy_spawn_rate == 0:
        spawn_enemy()

    # Déplacement des ennemis
    for enemy in enemies[:]:
        enemy["y"] += enemy["speed"]
        if enemy["y"] > HEIGHT:
            enemies.remove(enemy)

    # Déplacement des projectiles
    for projectile in projectiles[:]:
        projectile["y"] -= projectile_speed
        if projectile["y"] < 0:
            projectiles.remove(projectile)

    # Collisions
    for projectile in projectiles[:]:
        for enemy in enemies[:]:
            if (projectile["x"] > enemy["x"] and projectile["x"] < enemy["x"] + 50 and
                projectile["y"] > enemy["y"] and projectile["y"] < enemy["y"] + 50):
                projectiles.remove(projectile)
                enemy["health"] -= 1
                if enemy["health"] <= 0:
                    enemies.remove(enemy)
                    score += 10 if enemy["type"] == "rapide" else 30
                break

    # Affichage
    screen.fill(BLACK)
    screen.blit(player_imgs[current_player_img], (player_x, player_y))

    for projectile in projectiles:
        screen.blit(projectile_img, (projectile["x"], projectile["y"]))

    for enemy in enemies:
        img = enemy_imgs[0] if enemy["type"] == "rapide" else enemy_imgs[1]
        screen.blit(img, (enemy["x"], enemy["y"]))

    # Affichage du score et du mode Konami
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    if konami_active:
        konami_text = font.render("MODE KONAMI ACTIF !", True, WHITE)
        screen.blit(konami_text, (WIDTH // 2 - 100, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
