import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien within the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize alien and its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set rect attribute
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()

        # Start new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw alien at its current location"""
        self.screen.blit(self.image, self.rect)
