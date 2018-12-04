from agent import Agent
import math
from engine import Engine
import random

class Aincrad:
	def __init__(self):
		self.generation = 0
		self.numberOfAgents = 300
		self.mutationChance = 0.5
		self.agents = []
		self.limit = 700
		for i in range(self.numberOfAgents):
			self.agents.append(Agent())

	def mutation(self, x):
		if random.random()<self.mutationChance:
			self.agents[0].randomGene()
		return x

	def sortFunc(self, a):
		return a.fitness
	
	def gauss(self, x, sigma, mi):
		return 1/(sigma*math.sqrt(2*math.pi))*math.exp(-0.5*((x-mi)/sigma)**2)
	
	def run(self, a):
		engine = Engine()


		fitness = 0;
		cont = 0
		while cont<self.limit:
			cont += 1
			action = a.decide(engine.rocket.x, engine.rocket.y, engine.rocket.angle, engine.rocket.linSpd, engine.rocket.angSpd);
			engine.update(action[0], action[1])
			fitness  = self.gauss(engine.rocket.angle, 0.5, math.pi/2) + 0.9*fitness
			if math.sin(engine.rocket.angle) < -0.9:
				break
			if engine.crashed:
				break
			#fitness+=1

		a.fitness = fitness*10+cont
			
		
	
	def nextGeneration(self):
		self.generation += 1
		a = 0
		b = 1
		c = self.numberOfAgents-1
		d = c-1 
		while(b<c):
			# c and d agents will be deleted
			# a and b will reproduce generating new c and new d
			for i in range(len(self.agents[a].genes)):
				if random.random()>0.5:
					self.agents[c].genes[i] = self.mutation(self.agents[a].genes[i])
					self.agents[d].genes[i] = self.mutation(self.agents[b].genes[i])
				else:
					self.agents[d].genes[i] = self.mutation(self.agents[a].genes[i])
					self.agents[c].genes[i] = self.mutation(self.agents[b].genes[i])

			a+=1
			b+=1
			c-=1
			d-=1
		

		for i in range(len(self.agents)//2, len(self.agents)):
			self.run(self.agents[i])

		self.agents.sort(reverse = True, key = self.sortFunc)


		print("Generation = ", self.generation)
		for i in range(len(self.agents)):
			print(self.agents[i].fitness, end=' ')
		print("\n")




		
		
