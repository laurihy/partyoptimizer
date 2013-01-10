#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from partyoptimizer.operators import crossover

class test_Operators(unittest.TestCase):

  def test_buildGraph(self):
    origList = [{'id':x} for x in [1,2,3,4]]    
    expected = {1:[2], 2:[1,3], 3:[2,4], 4:[3]}
    result = crossover.buildGraph(origList)
    self.assertEqual(expected,result)

  def test_buildUnion(self):
    a = b = expected = {1:[2], 2:[1,3], 3:[2,4], 4:[3]}
    result = crossover.buildUnion(a,b)
    self.assertEqual(expected,result)


