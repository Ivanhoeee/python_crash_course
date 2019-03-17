from game_functions import load_highscore

class GameStats():
	"""Track statistics for Alien Invasion."""
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		# Start game in an inactive state.
		self.game_active = False
		# High score should never be reset.
		"""Because the high score should never be reset, we initialize 
		high_score in __init__() rather than in reset_stats()."""
		self.high_score = load_highscore('highscores.txt')
		# Define it's the first game played in this round because then
		# we only display the Play button and not game over. 
		self.first_game = True
				
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		self.first_game = False
