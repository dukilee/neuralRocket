import math
import utils

class KPController:
	def __init__(self):
		self.goalAngle = math.pi/2
		self.goalY = 5 #in meters
		self.goalX = 0
		self.ka = 1.5 
		self.kv = 2
		self.kh = 0.5
		self.k2v = 0.5 
		self.kxp = 0.2 
		self.kxv = 1.1 
		self.limitX = 1
		self.limitVX = 1
	
	def nextAction(self,x, y, angle, linearSpeed, angularSpeed):
		diffAngle = utils.wrapToPi(angle - self.goalAngle)
		diffHeight = self.goalY - y

		diffWidth = x
		if diffWidth>self.limitX:
			diffWidth = self.limitX
		elif diffWidth<-self.limitX:
			diffWidth = -self.limitX


		vx = linearSpeed.x
		if linearSpeed.x>self.limitVX:
			vx = self.limitVX
		elif linearSpeed.x<-self.limitVX:
			vx = -self.limitVX
		vxl = -vx*self.kxv
		vxr = vx*self.kxv
		
		if vxl < 0:
			vxl = 0
		if vxr < 0:
			vxr = 0



		if diffHeight<0:
			diffHeight = 0

		leftMotorPower = diffAngle*self.ka + diffHeight*self.kh + angularSpeed*self.kv - linearSpeed.y*self.k2v - diffWidth*self.kxp + vxl
		rightMotorPower = -diffAngle*self.ka + diffHeight*self.kh - angularSpeed*self.kv - linearSpeed.y*self.k2v + diffWidth*self.kxp + vxr

		if leftMotorPower>1:
			leftMotorPower = 1
		elif leftMotorPower<0:
			leftMotorPower = 0

		if rightMotorPower>1:
			rightMotorPower = 1
		elif rightMotorPower<0:
			rightMotorPower = 0

		return [leftMotorPower, rightMotorPower]


		
