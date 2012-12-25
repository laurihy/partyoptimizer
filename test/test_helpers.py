import unittest
from partyoptimizer import helpers

class test_genTable(unittest.TestCase):
  """
  Unit tests for genTable
  """

  def test_genTableWorks(self):
    model = [[2, 1], [3, 0], [0, 3], [1, 2]]
    table = helpers.genTable(4)
    self.assertEqual(model, table)

  def test_genTableWorksBigger(self):
    model = [[2, 1], [3, 0], [0, 4, 3], [1, 5, 2], [2, 5], [3, 4]]
    table = helpers.genTable(6)
    self.assertEqual(model,table)

  def test_genTableRaisesError(self):
    self.assertRaises(ValueError,helpers.genTable,3)


class test_genParticipants(unittest.TestCase):
  """
  Unit tests for genParticipants
  """
  
  def test_genParticipantsWorks(self):
    model = [{'gender': 'M', 'id': 0}, {'gender': 'F', 'id': 1}, {'gender': 'M', 'id': 2}, {'gender': 'F', 'id': 3}]
    participants = helpers.genParticipants(4)
    self.assertEqual(model,participants)

