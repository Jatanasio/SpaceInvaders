import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/enemies.png").convert_alpha()  # Load enemy image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 3

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right >= 800 or self.rect.left <= 0:  # Bounce when hitting screen edge
            self.speed_x = -self.speed_x
            self.rect.y += 20  # Drop down when changing direction
