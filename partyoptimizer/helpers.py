#!/usr/bin/python
# -*- coding: utf-8 -*-

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