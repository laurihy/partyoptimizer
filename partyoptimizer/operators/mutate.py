#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random

def smartMutate(a, i, j):
  """
  Returns new array of a, where incides i and j are swapped
  """

  a = list(a)
  a[i],a[j] = a[j],a[i]
  return a

def mutate(a):
  """
  Returns new array, where two random indices are swapped
  """
  
  n1, n2 = random.randint(0,len(a)-1), random.randint(0,len(a)-1)
  return smartMutate(a,n1,n2)