#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from partyoptimizer.genetics.fitness import getFitnessForGeneration

from partyoptimizer.operators.crossover import crossover
from partyoptimizer.operators.mutate import mutate
from partyoptimizer.operators.mutate import smartMutate

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

def breedAnotherGeneration(prevGen, participants):
  """
  generates new set of potential solutions.
  """
  prevGen = reverseList(sorted(prevGen))
  newGen = []
  c = 2
  for i in range((len(prevGen)-1)/c):
    #g = list(prevGen[i])
    g = (prevGen[i][0],prevGen[i][1],prevGen[i][2])
    i1 = g[2].index(min(g[2]))
    g[2].pop(i1)
    #i2 = g[2].index(min(g[2]))+1
    i2 = random.randint(0,len(participants)-1)

    g = smartMutate(g[1],i1,i2)
    
    for j in range(c):
      b = list(prevGen[i][1])
      if random.random()>0.85:
        b = mutate(b)
      a = crossover(b,list(prevGen[i+1][1]),participants)
      newGen.append(a)

  newGen.append(prevGen[0][1])
  return newGen

def simulateGenerations(n, participants, seats, populationSize):
  """
  Returns best reached solution. Simulates n generations, with given participants and available seats.
  Each generation has populationSize amount of solutions
  """
  gen = genRandomGeneration(participants, populationSize)
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
    if random.random()>0.9: print 'gen: '+str(c)
    gen = breedAnotherGeneration(gen, participants)
    c+=1
    if (abs(best[0]-1.0))<0.000000001: break
  print c
  return best


def reverseList(list):
  """
  Return new list, which is reversed copy of the original
  """
  return [x for x in reversed(list)]

def averageFitness(population):
  """
  Returns average of fitnesses in population.
  Population is [(fitness, x, y), (fitness...)...]
  """
  s = reduce(lambda x, y: x+y, [x[0] for x in population])
  return s/float(len(population))


