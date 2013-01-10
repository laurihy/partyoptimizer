#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
import json
import datetime

from partyoptimizer import helpers

from partyoptimizer.genetics.generation import simulateGenerations


if len(sys.argv)<2:
  raise SystemExit, 'Provide source for participants in arguments'



# read first argument and use it as source for participants
sourcepath = sys.argv[1]
participantFile = open(sourcepath,'r')
participants = json.loads(participantFile.read())

participantFile.close()

# generate table to match participants
# NOTE: must be even number, otherwise raises ValueError
table = helpers.genTable(len(participants))

# determine population size
populationSize = len(participants)*3
if len(sys.argv)>2:
  populationSize = int(sys.argv[2])


# determine how many generations to run
generations = len(participants)*50
if len(sys.argv)>3:
  generations = int(sys.argv[3])

target = ''
if len(sys.argv)>4:
  target = sys.argv[4]

# run the algo
print 'Start running'
print ''

bestReached, scores = simulateGenerations(generations, participants, table, populationSize)
print scores

print ''
print 'Done'

# if we have target file, save bestReached there
if target!='':

  print 'Saving results to '+str(target)
  open(target,'w').write(json.dumps(bestReached))

print 'DONE, 4real'







