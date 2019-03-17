import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import username 
from game_over import GameOver


def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# Make the Play button.
	play_button = Button(ai_settings, screen, "Play")
	# Make a ship.
	ship = Ship(ai_settings, screen)	
	# Make a group to store bullets in.
	bullets = Group()
	aliens = Group()
	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	# Start the main loop for the game.
	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)	
	# Ask for username
	name = username.ask(screen, "Enter your name?")
	
	while True:
	# Watch for keyboard and mouse events. We check settings, update the 
	# ship and bullets and then update the screen. 
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
		aliens, bullets, name)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
			bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
			bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
		play_button)
run_game()
