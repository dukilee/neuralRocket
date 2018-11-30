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
		self.pl = 0 #left motor power
		self.pr = 0 #right motor power

	def draw(self, display):
		pSin = math.sin(self.angle); # precalculated sin
		pCos = math.cos(self.angle); # precalculated cos
		
		#main body
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

		#left motor
		pygame.draw.polygon(
			display,
			config.colors['red'],
			[
				[
					self.x
					+(-self.dh-self.dw*self.pl)*pCos
					+(-self.dw/2)*pSin,
					self.y
					-(-self.dh-self.dw*self.pl)*pSin
					+(-self.dw/2)*pCos,
				],[
					self.x
					+(-self.dh)*pCos
					+(-self.dw/6)*pSin,
					self.y
					-(-self.dh)*pSin
					+(-self.dw/6)*pCos,
				],[
					self.x
					+(-self.dh)*pCos
					+(-5*self.dw/6)*pSin,
					self.y
					-(-self.dh)*pSin
					+(-5*self.dw/6)*pCos,
				]

			]
		)

		#right motor
		pygame.draw.polygon(
			display,
			config.colors['red'],
			[
				[
					self.x
					+(-self.dh-self.dw*self.pr)*pCos
					+(self.dw/2)*pSin,
					self.y
					-(-self.dh-self.dw*self.pr)*pSin
					+(self.dw/2)*pCos,
				],[
					self.x
					+(-self.dh)*pCos
					+(self.dw/6)*pSin,
					self.y
					-(-self.dh)*pSin
					+(self.dw/6)*pCos,
				],[
					self.x
					+(-self.dh)*pCos
					+(5*self.dw/6)*pSin,
					self.y
					-(-self.dh)*pSin
					+(5*self.dw/6)*pCos,
				]

			]
		)

	def update(self, x, y, angle, leftPower, rightPower):
		self.x = x*config.game['scale'] + config.game['width']/2;
		self.y = config.game['height'] - config.game['floorHeight'] - y*config.game['scale'];

		self.angle = angle
		self.angle = utils.wrapToPi(self.angle);

		self.pl = leftPower;
		if(self.pl<0):
			self.pl = 0
		elif self.pl>1:
			self.pl = 1

		self.pr = rightPower;
		if(self.pr<0):
			self.pr = 0
		elif self.pr>1:
			self.pr = 1

	
