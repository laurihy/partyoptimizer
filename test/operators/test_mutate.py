#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from collections import Counter
from partyoptimizer.operators import mutate

class test_Mutate(unittest.TestCase):
  
  def setUp(self):
    self.a = [1,2,3,4]

  def test_doesntModifyOriginal(self):
    b = mutate.smartMutate(self.a,1,2)
    self.assertEqual(self.a,[1,2,3,4])

  def test_swapsRightIndices(self):
    b = mutate.smartMutate(self.a,1,2)
    self.assertEqual(b,[1,3,2,4])

  def test_randomMutateWorks(self):
    """ check that mutate produces different results """
    results = []
    for i in range(100):
      results.append(mutate.mutate(self.a))

    lists = []
    for r in results:
      if r not in lists: lists.append(r)

    self.assertTrue(len(lists)>3)





