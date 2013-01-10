#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

def genTable(n):
  """
  generates 1 valid table for n people. n must be even.
  """
  if n%2!=0:
    raise ValueError('Argument must be even')

  ret = [[] for x in range(0,n)]
  for i in range(0,n):
    
    if i>1: ret[i].append(i-2)
    if i<n-2: ret[i].append(i+2)
    
    if i>0 and i%2>0: ret[i].append(i-1)
    if i<n-1 and i%2==0: ret[i].append(i+1)
  return ret

def genParticipants(n):
  ret = []
  for i in range(n):
    p = {}
    p['id'] = i
    p['gender'] = 'M' if random.random()>0.51 else 'F'
    p['avec'] = None
    p['friends'] = genFriendlist(n,0.15,i)
    ret.append(p)
  return avecify(ret)

def avecify(people):
  ppl = list(people)
  splitted = splitArray(ppl,'gender')
  used = []
  for p in ppl:
    if random.random()>0.6 and p['id'] not in used:
      opp = splitted['F'] if p['gender']=='M' else splitted['M']
      if len(opp)>0:
        avec = opp.pop(0)
        p['avec'], avec['avec'] = avec['id'], p['id']
        used.extend([p['id'], avec['id']])
        
        # remove current also from list of targets, no one can have multiple avecs :(
        splitted[p['gender']] = filter(lambda x: x['id']!=p['id'], splitted[p['gender']])
  return ppl





def genFriendlist(n,p,cur):
  ret = []
  for i in range(n):
    if random.random()<p and i!=cur: ret.append(i)
  return ret



def dictify(arr, key):
  """ generate dict of array of dicts, based on a given key"""
  ret = {}
  for item in arr:
    if item[key] in ret: raise ValueError('provided key must be unique')
    ret[item[key]] = item
  return ret

def splitArray(d, k):
  ret = {}
  for item in d:
    if item[k] not in ret: ret[item[k]] = []
    ret[item[k]].append(item)
  return ret 

