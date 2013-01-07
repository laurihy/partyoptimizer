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
  
  def test_genParticipantsNumber(self):
    """
    make sure correct number of participants is generated
    """
    for n in [2,6,12]:
      participants = helpers.genParticipants(n)
      self.assertEqual(n,len(participants))

  def test_genParticipantsHasAttributes(self):
    """
    make sure, that participants have all required attributes
    """
    attributes = ['gender', 'id', 'avec', 'friends']
    participants = helpers.genParticipants(4)
    for p in participants:
      a = p.keys()
      self.assertEqual(sorted(attributes), sorted(a))


