#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
from partyoptimizer import helpers
from partyoptimizer.dummyFitness import fitness
from partyoptimizer.crossover import crossover

def smartMutate(a, minIndex, mutationcount):
	"""
	Switches two random indices in an array a 
	"""
	
	n = random.randint(0,len(a)-1)
	b = a.pop(minIndex)
	a.insert(n, b)

	return a

def mutate(a,modifier):
	if modifier==0: modifier=1
	if random.random()>(1-(1/float(modifier))):
		n = random.randint(0,len(a)-1)
		a = a[n:len(a)]+a[0:n]

	if random.random()>(1-(1/modifier)):
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

def extinct(prevGen,participants):
	"""
	choose few survivors and generate completely new generation
	"""
	prevGen = reverseList(sorted(prevGen))
	newGen = []
	newgen = [x[1] for x in prevGen[0:20]]
	newgen += genRandomGeneration(participants, len(prevGen)-10)
	return newgen


def breedAnotherGeneration(prevGen,modifier=0):
	"""
	generates new set of potential solutions. Take best 25% of the previous one, and have 4 mutations
	"""
	prevGen = reverseList(sorted(prevGen))
	newGen = []
	
	for i in range((len(prevGen)-1)/2):
		g = prevGen[i]
		for j in range(2):
			a = crossover(list(g[1]),prevGen[i+1][1])
			a = mutate(a, modifier)
			newGen.append(a)

	newGen.append(prevGen[0][1])
	return newGen

def simulateGenerations(n, participants, seats):
	gen = genRandomGeneration(participants, 1000)
	c = 0
	best = (0,[])
	generationsWithoutImprovement = 0
	while c < n:
		gen = getFitnessForGeneration(gen,participants,seats)
		g = reverseList(sorted(gen))
		if (abs(best[0]-g[0][0]))<0.00000001: generationsWithoutImprovement+=1
		if g[0][0] > best[0]: 
			best = g[0]
			generationsWithoutImprovement = 0
		print best[0]
		gen = breedAnotherGeneration(gen,generationsWithoutImprovement)
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
bestReached = simulateGenerations(700, participants, seats)
print bestReached


