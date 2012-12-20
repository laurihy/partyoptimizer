#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This provides a dummy fitness function for developing a genetic optimizer.
Later on, when the genetic optimization works, we can develop the fitness function

The basic idea with this one is, that participants are representated as integers.
The match between participants is the difference of 2 integers.


0--1
|  |
2--3

seats = [
  [1,2],
  [0,3],
  [0,2],
  [1,2]
]

"""

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
  
  genderfit = 0
  for n in neighbours:
    if cur['gender'] != n['gender']: genderfit+=1

  return genderfit/float(len(neighbours))

def getFitnessBySeats(seatingorder, participants, seats):
  """
  get fitness per one seat, used to check which seats have worst fitness
  """
  return [fitnessForOneSeat(seats,participants,seatingorder, x) for x in range(0,len(seats))]

def fitness(seatingorder,participants,seats):
  """
  returns normalized 0-1 sum of all individual fitnesses
  """
  fitnesses = getFitnessBySeats(seatingorder, participants, seats)
  return sum(fitnesses)/len(fitnesses), fitnesses

#p = [{'gender':'M'},{'gender':'F'},{'gender':'M'},{'gender':'F'}]
#seatingorder = [p[0],p[1],p[2],p[3]]

#print fitness(seatingorder, p, seats)


