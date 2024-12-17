import pygame
from pygame.sprite import Sprite

class Ship(pygame.sprite.Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen.get_rect().midbottom

        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags"""
        screen_rect = self.screen.get_rect()
        if self.moving_right and self.rect.right < screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > screen_rect.left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.x = float(self.rect.x)