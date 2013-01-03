#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Edge Recombination Operator
http://en.wikipedia.org/wiki/Edge_recombination_operator
"""

import random

def buildGraph(a):
	ret = {}
	for i in range(len(a)):
		ret[a[i]['id']] = []
		if i>0: ret[a[i]['id']].append(a[i-1]['id'])
		if i<len(a)-1: ret[a[i]['id']].append(a[i+1]['id'])
	return ret 

def buildUnion(a,b):
	ret = {}
	for i in a:
		ret[i] = list(set(a[i]+b[i]))
	return ret

def recombinate(u):
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

#a = [3,2,4,1,5,6,7]
#b = [2,3,1,4,5,6,7]

def crossover(a,b,participants):
	u = buildUnion(buildGraph(a),buildGraph(b))
	neworder = recombinate(u)
	return [participants[i] for i in neworder]



