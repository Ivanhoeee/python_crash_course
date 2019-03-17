import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""
	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet object at the ship's current position."""
		""" explanation super(Bullet,self).__init__()
		The Bullet class inherits from Sprite, which we import from the
		pygame.sprite module. When you use sprites, you can group related elements
		in your game and act on all the grouped elements at once. To
		create a bullet instance, __init__() needs the ai_settings, screen, and ship
		instances, and we call super() to inherit properly from Sprite.
		"""
		super(Bullet, self).__init__()
		self.screen = screen
		
		# Create a bullet rect at (0, 0) and then set correct position.
		""" explain line below
		The bullet is not based on an image so we have to build a rect from 
		scratch using the pygame.Rect() class.
		This class requires the x- and y-coordinates of the top-left corner of the
		rect, and the width and height of the rect. We initialize the rect at (0, 0),
		but we’ll move it to the correct location in the next two lines, because the
		bullet’s position is dependent on the ship’s position.
		"""
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
		ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		"""
		The bullet should emerge from the top of the ship, so we set the top of the
		bullet’s rect to match the top of the ship’s rect, making it look like the bullet
		is fired from the ship
		"""
		self.rect.top = ship.rect.top
		
		# Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""When a bullet is fired, it moves up the screen, which corresponds to a decreasing
		y-coordinate value; so to update the position, we subtract the amount
		stored in self.speed_factor from self.y"""
		# Update the decimal position of the bullet.
		self.y -= self.speed_factor
		# Update the rect position.
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
