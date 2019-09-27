import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # Class managing bullets fired from a ship

    def __init__(self, ai_settings, screen, ship):
        # Create bullet object at ships current location
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet's decimal position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullets_speed_factor

    def update(self):
        # Move bullet up screen when shooting
        self.y -= self.speed_factor
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw bullet to screen
        pygame.draw.rect(self.screen, self.color, self.rect)
