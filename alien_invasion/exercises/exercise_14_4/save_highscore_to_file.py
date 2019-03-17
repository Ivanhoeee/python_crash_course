def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
	bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button,
			ship, aliens, bullets, mouse_x, mouse_y)
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
			
def save_highscore(filename): 
	"""
	After we close the game after say 5 games, the high_score should be 
	saved to a file only if the high score up to then is lower than the 
	new high_score. Otherwise it's not saved. 
	"""
	with open(filename, 'w') as file_object: 
		file_object.write(str(stats.high_score))
		

def ask_username(): 
	"""
	Ask for username before the game starts, save this name with the highscore
	and show it in the game. 
	"""
