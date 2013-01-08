#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This is a script used to run the algorithm several times, and generate timeseries

"""

import sys
import random
import json
import datetime

from partyoptimizer import helpers

from partyoptimizer.genetics.generation import simulateGenerations

# read first argument and use it as source for participants
sourcepath = './sampleparticipants/80.json'
participantFile = open(sourcepath,'r')

participants = json.loads(participantFile.read())
table = helpers.genTable(len(participants))
generations = 5000

populationSizes = [20,50,100,200,500,800]

for populationSize in populationSizes:
	for i in range(0,4):
		id = str(populationSize)+'_'+str(i)
		print id
		bestReached, scores = simulateGenerations(generations, participants, table, populationSize)
		open('timeseries/'+id+'.json','w').write(json.dumps(scores))		

print 'done'







