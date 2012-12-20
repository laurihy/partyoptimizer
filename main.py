#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
from partyoptimizer import helpers
from partyoptimizer.fitness import fitness
from partyoptimizer.crossover import crossover

tableSize = int(sys.argv[1])
print 'Table size: '+str(tableSize)

generations = int(sys.argv[2])
print 'Generations: '+str(generations)

populationSize = int(sys.argv[3])
print 'Population size: '+str(populationSize)

def smartMutate(a, i, j):
	"""
	Switches worst slots to some other place
	"""

	a = list(a)

	a[i],a[j] = a[j],a[i]

	return a

def mutate(a):
	n1, n2 = random.randint(0,len(a)-1), random.randint(0,len(a)-1)
	a[n1],a[n2] = a[n2],a[n1]

	return a

def getFitnessForGeneration(generation, participants, seats):
	"""
	Calculates fitness for a generation, which is a list of potential solutions
	"""
	ret = []
	for g in generation:
		fit, perSeat = fitness(g,participants,seats)
		ret.append((fit,g,perSeat))
	return ret

def genRandomGeneration(participants,size=0):
	"""
	generates a random set of solutions. Used to seed the algorithm
	"""
	if size==0: size=len(participants)*2
	ret = []
	for i in range(size):
		p = list(participants)
		random.shuffle(p)
		ret.append(p)
	return ret

def breedAnotherGeneration(prevGen,modifier=0):
	"""
	generates new set of potential solutions. Take best 25% of the previous one, and have 4 mutations
	"""
	prevGen = reverseList(sorted(prevGen))
	newGen = []
	c = 2
	for i in range((len(prevGen)-1)/c):
		#g = list(prevGen[i])
		g = (prevGen[i][0],prevGen[i][1],prevGen[i][2])
		i1 = g[2].index(min(g[2]))
		g[2].pop(i1)
		i2 = g[2].index(min(g[2]))+1

		g = smartMutate(g[1],i1,i2)
		
		for j in range(c):
			b = list(prevGen[i][1])
			if random.random()>0.95:
				b = mutate(b)
			a = crossover(b,list(prevGen[i+1][1]),participants)
			newGen.append(a)

	newGen.append(prevGen[0][1])
	return newGen

def simulateGenerations(n, participants, seats, populationSize):
	gen = genRandomGeneration(participants, populationSize)
	c = 0
	best = (0,[])
	generationsWithoutImprovement = 0
	while c < n:
		gen = getFitnessForGeneration(gen,participants,seats)
		g = reverseList(sorted(gen))
		#print g[0]
		if (abs(best[0]-g[0][0]))<0.00000001: generationsWithoutImprovement+=1
		if g[0][0] > best[0]: 
			best = g[0]
			generationsWithoutImprovement = 0
		if random.random()>0.9: print 'gen: '+str(c)
		gen = breedAnotherGeneration(gen,generationsWithoutImprovement)
		c+=1
	return best

def reverseList(list):
	return [x for x in reversed(list)]

def averageFitness(population):
	s = reduce(lambda x, y: x+y, [x[0] for x in population])
	return s/float(len(population))


# generate data
seats = helpers.genTable(tableSize)
participants = helpers.genParticipants(tableSize)

# run the algo
bestReached = simulateGenerations(generations, participants, seats, populationSize)
print bestReached


