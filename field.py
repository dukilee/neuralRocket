import pygame
import config

class Field:
	def __init__(self):
		self.height = config.game['floorHeight'];

	def draw(self, display):
		pygame.draw.rect(
			display,
			config.colors['red'],
			[
				0,
				config.game['height']-self.height,
				config.game['width'],
				self.height
			]

		);
