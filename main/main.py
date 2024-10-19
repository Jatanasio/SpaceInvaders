import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy
from level import Level

# Initialize Pygame
pygame.init()


#Initialize music
pygame.mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Knockoff")

pygame.font.init()
font = pygame.font.Font(None, 36)

# Colors
BLACK = (0, 0, 0)
 
# Music
pygame.mixer.music.load('assets/assets/Music for a Space Inavders-like minigame v1.wav') 
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Create sprite groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create the player and add it to the sprite group
player = Player()
all_sprites.add(player)

# Initialize Timer

level = Level()

# Create enemies in a grid
def spawn_enemies(all_sprites, enemies):
    # Clear previous enemies
    enemies.empty()

    for i in range(8):
        for j in range(5):
            # Positioning enemies (modify based on level if desired)
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
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Shoot bullet
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                
        
    current_level = level.get_current_level()

    # Update sprites
    all_sprites.update()

    # Check for collisions between bullets and enemies
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    

    collisions = pygame.sprite.spritecollide(player, enemies, False)
    
   
    if len(enemies) == 0:  # If all enemies are gone
        if current_level < 3:  # Move to the next level
            level.next_level()
            spawn_enemies(all_sprites, enemies)
        else: 
            screen.fill(BLACK)
            win_text = font.render("You win!", True, (255, 255, 255))
            screen.blit(win_text, (screen.get_width() // 2 - win_text.get_width() // 2, screen.get_height() // 2 - win_text.get_height() // 2))
            pygame.display.flip()

            # Wait for a few seconds before quitting
            pygame.time.delay(2000)  # Wait 2 seconds
            running = False  # End the game if all levels are completed

    if collisions:
        screen.fill(BLACK)
        lose_text = font.render("You lose!", True, (255, 255, 255))
        screen.blit(lose_text, (screen.get_width() // 2 - lose_text.get_width() // 2, screen.get_height() // 2 - lose_text.get_height() // 2))
        pygame.display.flip()

        # Wait for a few seconds before quitting
        pygame.time.delay(2000)  # Wait 2 seconds
        running = False 

    # Draw everything
    screen.fill(BLACK)
    level_text = font.render(f"Level: {current_level}", True, (255, 255, 255))  # White text
    screen.blit(level_text, (10, 10))

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
  