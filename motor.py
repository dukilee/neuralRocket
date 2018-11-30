import config

class Motor:
	def __init__(self):
		self.power = 0;
	
	'''
	' Emulates a real engine
	' expectedPower between 0 and 1:
	'	0 -> off
	'	1 -> full power
	'''
	def update(self, expectedPower):
		if expectedPower > 1:
			expectedPower = 1
		elif expectedPower < 0:
			expectedPower = 0

		self.power = (self.power + expectedPower)/2
		return self.power
	
	'''
	' Returns the power in newtons
	'''
	def getPowerSI(self):
		return self.power*config.rocket['motorPower']
		

