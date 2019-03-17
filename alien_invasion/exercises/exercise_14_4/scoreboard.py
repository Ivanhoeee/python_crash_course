import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""A class to report scoring information.we give __init__() the 
	parameters ai_settings,screen, and stats so it can report the values 
	we’re tracking"""
	def __init__(self, ai_settings, screen, stats):
		"""Initialize scorekeeping attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		# Font settings for scoring information.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		# Prepare the initial score image, this turns text into an image.
		self.prep_score()
		"""The high score will be displayed separately from the score, 
		so we need a new method, prep_high_score(), to prepare the high 
		score image"""
		self.prep_high_score()
		self.prep_level()
		"""Because we’re making a group of ships, we import the Group and Ship
		classes."""
		self.prep_ships()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		# First turn score into a string
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)		
		"""Then pass this string to render(), which creates the image. 
		To display the score clearly onscreen, we pass the screen’s 
		background color to render() as well as a text color."""
		self.score_image = self.font.render(score_str, True, self.text_color,
		self.ai_settings.bg_color)
		# Display the score at the top right of the screen.
		"""To make sure the score always lines up with the right side of the
		screen, we create a rect called score_rect w and set its right 
		edge 20 pixels from the right screen edge"""
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def show_score(self):
		"""Draw scores and level to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		# Draw ships To display the ships on the screen, we call draw() on the group, and Pygame draws each ship..
		self.ships.draw(self.screen)
		
	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
		self.text_color, self.ai_settings.bg_color)
		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""Turn the level into a rendered image.The method prep_level 
		creates an image from the value stored in stats.level and sets 
		the image’s right attribute to match the score’s right attribute"""
		self.level_image = self.font.render(str(self.stats.level), True,
		self.text_color, self.ai_settings.bg_color)
		# Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	def prep_ships(self):
		"""Show how many ships are left.The prep_ships() method creates 
		an empty group, self.ships, to hold the ship instances. To fill 
		this group, a loop runs once for every ship the player has left. 
		Inside the loop we create a new ship and set
		each ship’s x-coordinate value so the ships appear next to each other
		with a 10-pixel margin on the left side of the group of ships"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
