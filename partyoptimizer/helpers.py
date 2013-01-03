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
  return ret

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

def splitDict(d, k, val):
  ret = {}
  for key,item in d.items():
    newkey = item[k]
    if newkey not in ret:
      ret[newkey] = []
    ret[newkey].append(item[val])
  return ret 

