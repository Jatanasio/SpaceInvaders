import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Knockoff")

# Colors
BLACK = (0, 0, 0)

# Create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create the player and add it to the sprite group
player = Player()
all_sprites.add(player)

# Create enemies in a grid
for i in range(8):
    for j in range(5):
        enemy = Enemy(50 + i * 80, 50 + j * 50)
        all_sprites.add(enemy)
        enemies.add(enemy)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Set frame rate to 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Shoot bullet
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Update sprites
    all_sprites.update()

    # Check for collisions between bullets and enemies
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)

    # Check for win condition
    if len(enemies) == 0:
        print("You win!")
        running = False

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
  