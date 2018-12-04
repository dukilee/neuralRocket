import pygame
import config

class Info:
	def __init__(self):
		pygame.font.init()
		self.font = pygame.font.SysFont('Comic Sans MS', 30)
	
	def draw(self, display, toGo, generation, fitness):
		toGoText = self.font.render('To go '+str(toGo), False, config.colors['white'])
		genText = self.font.render('Generation '+str(generation), False, config.colors['white'])
		fitText = self.font.render('Fitness '+str(fitness), False, config.colors['white'])
		display.blit(toGoText, (0, 0))
		display.blit(genText, (0, 40))
		display.blit(fitText, (0, 80))

	
