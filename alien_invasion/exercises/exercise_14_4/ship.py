import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	""" Initialization takes two parameters: the self and the screen where 
	we'll draw the ship. """
	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		# Pygame lets you treat elements like rectangles even though they're
		# not rectangles and this is efficient since rectangles are simple
		# object.
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Start each new ship at the bottom center of the screen.
		# Here we say that the ships (rect) center equals the screens center.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)
		# Movement flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the ship's position based on the movement flag."""
		""" Remark upper row below:
		This code checks the position of the ship before changing the value of
		self.center. The code self.rect.right returns the x-coordinate value of the
		right edge of the ship’s rect. If this value is less than the value returned
		by self.screen_rect.right, the ship hasn’t reached the right edge of the
		screen. The same goes for the left edge: if the value of the left side of
		the rect is greater than zero, the ship hasn’t reached the left edge of the
		screen. This ensures the ship is within these bounds before adjusting
		the value of self.center.
		"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		# Update rect object from self.center.
		self.rect.centerx = self.center
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		"""Center the ship on the screen."""
		self.center = self.screen_rect.centerx
