import pygame
from pygame.sprite import Sprite
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group

class GameOver():
	"""A class to show the image of game over once the game is over."""
	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position."""
		self.screen = screen
		self.ai_settings = ai_settings
		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load('images/game_over.bmp')
		self.rect = self.image.get_rect()
		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width / 2
		self.rect.y = self.rect.height / 2 
		# Store the alien's exact position.
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""Draw game over image."""
		self.screen.blit(self.image, self.rect)
