import config
import math
import pygame
import utils

class Rocket:
	def  __init__(self):
		self.x = config.initialPosition['x']*config.game['scale'] + config.game['width']/2;
		self.y = config.game['height'] - config.game['floorHeight'] - config.initialPosition['y']*config.game['scale'];

		self.angle = config.initialPosition['angle'];
		self.angle = utils.wrapToPi(self.angle);
		self.dh = config.game['scale']*config.rocket['height']/2; #half display height
		self.dw = config.game['scale']*config.rocket['width']/2; # half display height

	def draw(self, display):
		pSin = math.sin(self.angle); # precalculated sin
		pCos = math.cos(self.angle); # precalculated cos
		pygame.draw.polygon(
			display,
			config.colors['green'],
			[
				[
					self.x+self.dw*pSin+self.dh*pCos,
					self.y+self.dw*pCos-self.dh*pSin,
				], [
					self.x-self.dw*pSin+self.dh*pCos,
					self.y-self.dw*pCos-self.dh*pSin,
				], [
					self.x-self.dw*pSin-self.dh*pCos,
					self.y-self.dw*pCos+self.dh*pSin,
				], [
					self.x+self.dw*pSin-self.dh*pCos,
					self.y+self.dw*pCos+self.dh*pSin,
				]
			]
		
		);

	def update(self, x, y, angle):
		self.x = x*config.game['scale'] + config.game['width']/2;
		self.y = config.game['height'] - config.game['floorHeight'] - y*config.game['scale'];

		self.angle = angle
		self.angle = utils.wrapToPi(self.angle);

	
