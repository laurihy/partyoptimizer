#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
from partyoptimizer import helpers
from partyoptimizer.dummyFitness import fitness 

def mutate(a):
	"""
	Switches two random indices in an array a 
	"""
	n, n2 = random.randint(0,len(a)-1), random.randint(0,len(a)-1)
	a[n],a[n2] = a[n2],a[n]
	return a

def getFitnessForGeneration(generation, participants, seats):
	"""
	Calculates fitness for a generation, which is a list of potential solutions
	"""
	ret = []
	for g in generation:
		fit = fitness(g,participants,seats)
		ret.append((fit,g))
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

def breedAnotherGeneration(prevGen):
	"""
	generates new set of potential solutions. Take best 25% of the previous one, and have 4 mutations
	"""
	prevGen = reverseList(sorted(prevGen))
	newGen = []
	for g in prevGen[0:len(prevGen)/4-1]:
		# we want 2 mutations
		for j in range(4):
			a = mutate(list(g[1]))
			newGen.append(a)
	for i in range(10): newGen.append(prevGen[i][1])
	return newGen

def simulateGenerations(n, participants, seats):
	gen = genRandomGeneration(participants, 500)
	c = 0
	best = 0
	while c < n:
		gen = getFitnessForGeneration(gen,participants,seats)
		
		print averageFitness(gen)
		g = reverseList(sorted(gen))
		if g[0][0] > best: best = g[0][0]

		gen = breedAnotherGeneration(gen)
		c+=1
	return best

def reverseList(list):
	return [x for x in reversed(list)]

def averageFitness(population):
	s = reduce(lambda x, y: x+y, [x[0] for x in population])
	return s/float(len(population))



# generate data
seats = helpers.genTable(100)
participants = range(0,100)

# best possible seating and fitness
best = fitness(participants, participants, seats)
print 'Best possible: %s' % str(best)

# run the algo
simulateGenerations(500, participants, seats)


