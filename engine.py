import config
import math
import utils
from motor import Motor
from point import Point


class PhysicsRocket:
	def __init__(self):
		self.x = config.initialPosition['x'] 
		self.y = config.initialPosition['y']

		self.angle = config.initialPosition['angle'];
		self.angle = utils.wrapToPi(self.angle);

		self.linSpd = Point(0, 0) # linear speed
		self.linAcc = Point(0, 0) # linear acceleration
		self.angSpd = 0 # angular speed
		self.angAcc = 0 # angular acceleration

		self.leftMotor = Motor()
		self.rightMotor = Motor()

		self.mass = config.rocket['mass']
		self.width = config.rocket['width']
		self.height = config.rocket['height']
		self.dt = 1.0/config.game['fps']


		#considering the rocket as a cilinder
		self.inertia = self.mass/4*(self.width*self.width/4 + self.height*self.height/3)

	def update(self, leftPower, rightPower):
		self.leftMotor.update(leftPower)
		self.rightMotor.update(rightPower)
		
		#Angular update
		torque = (self.rightMotor.getPowerSI() - self.leftMotor.getPowerSI())*self.width/4
		self.angAcc = torque/self.inertia
		self.angle += (self.angAcc*self.dt/2 + self.angSpd)*self.dt
		self.angSpd += self.angAcc*self.dt


		#Linear update
		force = Point(
			(self.rightMotor.getPowerSI() + self.leftMotor.getPowerSI())*math.cos(self.angle),
			-self.mass * config.physics['gravity'] + (self.rightMotor.getPowerSI() + self.leftMotor.getPowerSI())*math.sin(self.angle)
			)

		self.linAcc.x = force.x/self.mass
		self.linAcc.y = force.y/self.mass
		self.x += (self.linAcc.x*self.dt/2 + self.linSpd.x)*self.dt
		self.y += (self.linAcc.y*self.dt/2 + self.linSpd.y)*self.dt
		self.linSpd.x += self.linAcc.x*self.dt
		self.linSpd.y += self.linAcc.y*self.dt
		#print("----")
		#print("acc:", self.linAcc.x, self.linAcc.y)
		#print("spd:",self.linSpd.x, self.linSpd.y)
		#print("pos:", self.x, self.y)


		

class Engine:
	def __init__(self):
		self.rocket = PhysicsRocket()
		self.crashed = False;

	def checkIfCrashed(self):
		pSin = abs(math.sin(self.rocket.angle))
		pCos = abs(math.cos(self.rocket.angle))
		lowestPointY = self.rocket.y-self.rocket.width/2*pCos-self.rocket.height/2*pSin
		if lowestPointY < 0:
			self.crashed = True


	'''
	' Given the power in each motor, updates the rocket position and speed
	'''
	def update(self, leftPower, rightPower):
		if not self.crashed:
			self.rocket.update(leftPower, rightPower)
			self.checkIfCrashed()








