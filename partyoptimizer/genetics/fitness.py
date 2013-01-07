#!/usr/bin/python
# -*- coding: utf-8 -*-


def getNeighboursForSeat(seats, participants, seatingorder, seat):
  """
  returns participants who are sitting next to the seat
  """
  return [seatingorder[x] for x in seats[seat]]

def fitnessForOneSeat(seats, participants, seatingorder, seat):
  """
  returns normalized 0-1 fitness for one seat
  """
  cur = seatingorder[seat]
  neighbours = getNeighboursForSeat(seats, participants, seatingorder, seat)
  
  avecfit = avecFitness(cur,neighbours)

  genderfit = genderFitness(cur,neighbours)

  friendfit = friendFitness(cur,neighbours)

  return (genderfit*0.4)+(avecfit*0.4)+(friendfit*0.2)

def avecFitness(cur, neighbours):
  """
  Returns 0 if cur HAS avec and IS NOT seated next to it, otherwise 1
  """
  avecfit = 0
  if not cur['avec']: 
    avecfit = 1
  elif cur['avec'] in [x['id'] for x in neighbours]: 
    avecfit = 1
  return avecfit

def genderFitness(cur,neighbours):
  """
  Checks, how many neighbours are opposite gender. The more the better. From 0 (none) to 1 (all)
  """
  genderfit = 0
  for n in neighbours:
    if cur['gender'] != n['gender']: genderfit+=1
  genderfit = genderfit/float(len(neighbours))
  return genderfit

def friendFitness(cur,neighbours):
  """
  Checks how many of the neighbours are friends of cur. From 0 (none) to 1 (all)
  """
  friendfit = 0
  for n in neighbours:
    if n['id'] in cur['friends']: friendfit+=1
  friendfit = friendfit/float(len(neighbours))
  return friendfit

def getFitnessBySeats(seatingorder, participants, seats):
  """
  get array of fitnesses, for each seat
  """
  return [fitnessForOneSeat(seats,participants,seatingorder, x) for x in range(0,len(seats))]

def fitness(seatingorder,participants,seats):
  """
  returns normalized 0-1 sum of all individual fitnesses
  """
  fitnesses = getFitnessBySeats(seatingorder, participants, seats)
  return sum(fitnesses)/len(fitnesses), fitnesses

def getFitnessForGeneration(generation, participants, seats):
  """
  Calculates fitness for a generation, which is a list of potential solutions
  """
  ret = []
  for g in generation:
    fit, perSeat = fitness(g,participants,seats)
    ret.append((fit,g,perSeat))
  return ret


