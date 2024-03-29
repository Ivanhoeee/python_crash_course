import pygame.font

class Button():
	def __init__(self, ai_settings, screen, msg):
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		"""prepare a font attribute for rendering text. The None argument
		tells Pygame to use the default font, and 48 determines the size of 
		the text."""	
		self.font = pygame.font.SysFont(None, 48)
		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		# The button message needs to be prepped only once.
		"""Pygame works with text by rendering the string you want to display as
		an image."""
		self.prep_msg(msg)
	
	def prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button.
		The prep_msg() method needs a self parameter and the text to be rendered
		as an image (msg). The call to font.render() turns the text stored in
		msg into an image, which we then store in msg_image"""
		self.msg_image = self.font.render(msg, True, self.text_color,
		self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
