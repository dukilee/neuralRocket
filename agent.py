import math
import random

class Agent:
	def __init__(self):
		self.numberOfInputs = 6
		self.numberInMiddle = 10
		self.genes = [];
		self.fitness = 0
		for i in range(self.numberInMiddle*(self.numberOfInputs+2)):
			self.genes.append(self.randomGene())


	
	def randomGene(self):
		return random.uniform(-4, 4)

	def sigmoid(self, x):
		return 1/(1+math.exp(-x))

	def inner(self, a, b):
		if(len(a) != len(b)):
			print(a, b, self.genes)
			print("Lengths are different");
			return 0
		ans = 0
		for i in range(len(a)):
			ans += a[i]*b[i]
		return self.sigmoid(ans)

	def inner2(self, a, b):
		if(len(a) != len(b)):
			print(a, b, self.genes)
			print("Lengths are different");
			return 0
		ans = 0
		for i in range(len(a)):
			ans += a[i]*b[i]
		if ans<0:
			return 0
		return ans



	def decide(self,  x, y, angle, v, w):
		goalY = 5;

		inp = [x, goalY-y, angle - math.pi*0.5, v.x, v.y, w]

		middle = []
		sz = len(inp)
		aux = 0
		for i in range(self.numberInMiddle):
			middle.append(self.inner2(
				inp,
				self.genes[aux:(aux+sz)]))
			aux += sz


		sz = self.numberInMiddle
		output = []
		for i in range(2):
			output.append(self.inner(
				middle,
				self.genes[aux:(aux+sz)]))
			aux += sz


		return output
		
