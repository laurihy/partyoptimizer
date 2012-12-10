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
    if i<n/2:
      ret[i].append(i+n/2)
    elif i>=n/2:
      ret[i].append(i-n/2)
    if i not in [0,n/2]:
      ret[i].append(i-1)
    if i not in [n/2-1, n-1]:
      ret[i].append(i+1)
  return ret