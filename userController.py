import pygame

class UserController:
	def __init__(self):
		self.leftIsDown = False;
		self.rightIsDown = False;
		self.upIsDown = False;
	
	def updateEvent(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.leftIsDown = True
			elif event.key == pygame.K_RIGHT:
				self.rightIsDown = True
			elif event.key == pygame.K_UP:
				self.upIsDown = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.leftIsDown = False
			elif event.key == pygame.K_RIGHT:
				self.rightIsDown = False
			elif event.key == pygame.K_UP:
				self.upIsDown = False
	
	'''
	' 0 -> the left engine is off
	' 1 -> the left engine is at full force
	'''
	def getLeftPower(self):
		if self.upIsDown:
			return 1
		if self.leftIsDown:
			return 1
		return 0
	

	'''
	' 0 -> the right engine is off
	' 1 -> the right engine is at full force
	'''
	def getRightPower(self):
		if self.upIsDown:
			return 1
		if self.rightIsDown:
			return 1
		return 0
			

