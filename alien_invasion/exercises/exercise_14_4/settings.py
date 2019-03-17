class Settings():
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's static settings."""
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (255, 255, 255)
		# Ship settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 2
		# Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		# Alien settings
		self.alien_speed_factor = 1.5
		self.fleet_drop_speed = 70
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		# How quickly the game speeds up
		"""we add a speedup_scale setting to control how quickly the
		game speeds up: a value of 2 will double the game speed every time the
		player reaches a new level; a value of 1 will keep the speed constant"""
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()
		# How quickly the alien point values increase
		self.score_scale = 1.5
		
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		# Scoring
		self.alien_points = 50
		
	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
