#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Edge Recombination Operator
http://en.wikipedia.org/wiki/Edge_recombination_operator
"""

import random

def buildGraph(a):
  """
  Builds a graph, where adjacent items in list are marked as adjacent nodes
  """
  ret = {}
  for i in range(len(a)):
    ret[a[i]['id']] = []
    if i>0: ret[a[i]['id']].append(a[i-1]['id'])
    if i<len(a)-1: ret[a[i]['id']].append(a[i+1]['id'])
  return ret 

def buildUnion(a,b):
  """
  Combines two graphs into one and removes duplicated edges
  """
  ret = {}
  for i in a:
    ret[i] = list(set(a[i]+b[i]))
  return ret

def recombinate(u):
  """
  Recombines graph into a list
  Good explanation at http://en.wikipedia.org/wiki/Edge_recombination_operator
  """
  ret = []
  origLen = len(u.keys())
  n = random.choice(u.keys())
  while len(ret)<origLen:
    ret.append(n)
    neighbours = u.pop(n)
    minNeighbours = 99999999999 # a very laarge number :)
    newNeighbour = -1
    for a in neighbours:
      u[a].pop(u[a].index(n))
      if len(u[a]) < minNeighbours:
        newNeighbour = a
        minNeighbours = len(u[a])
    if newNeighbour<0 and len(u.keys())>0:
      newNeighbour = random.choice(u.keys())
    if newNeighbour<0 and len(u.keys())==0:
      break
    n = newNeighbour
  return ret

def crossover(a,b,participants):
  """
  Performs edge recombination for two lists. 
  This way of crossover preserves order and count of the elements
  """
  u = buildUnion(buildGraph(a),buildGraph(b))
  neworder = recombinate(u)
  return [participants[i] for i in neworder]



