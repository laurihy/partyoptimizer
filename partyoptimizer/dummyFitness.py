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

import math

def getNeighboursForSeat(seats, participants, seatingorder, seat):
  """
  returns participants who are sitting next to the seat
  """
  return [seatingorder[x] for x in seats[seat]]

def diff(target, neighbours):
  """
  returns average difference of target value to all other values
  """
  return sum([abs(target-x) for x in neighbours]) / float(len(neighbours))

def fitnessForOneSeat(seats, participants, seatingorder, seat):
  """
  returns normalized 0-1 fitness for one seat
  """
  neighbours = getNeighboursForSeat(seats, participants, seatingorder, seat)
  d = diff(seatingorder[seat], neighbours)
  return 1/d

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
