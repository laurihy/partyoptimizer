import unittest
from mock import Mock
from partyoptimizer.genetics import fitness

class testFriendFitness(unittest.TestCase):
  """
  Fitness based on friends should work properly
  """
  def setUp(self):
    self.cur = {'friends':[1,2,3]}

  def test_friendFitnessGood(self):
    neighbours = [{'id':x} for x in [1,2,3]]
    fit = fitness.friendFitness(self.cur,neighbours)
    self.assertEqual(1,fit)

  def test_FriendFitnessBad(self):
    neighbours = [{'id':x} for x in [4,5,6]]
    fit = fitness.friendFitness(self.cur,neighbours)
    self.assertEqual(0,fit)

class test_GenderFitness(unittest.TestCase):
  """
  Fitness based on gender should work properly
  """
  def setUp(self):
    self.cur = {'gender':'M'}

  def test_genderFitnessGood(self):
    neighbours = [{'gender':'F'} for x in range(0,2)]
    fit = fitness.genderFitness(self.cur,neighbours)
    self.assertEqual(1,fit)

  def test_genderFitnessBad(self):
    neighbours = [{'gender':'M'} for x in range(0,2)]
    fit = fitness.genderFitness(self.cur,neighbours)
    self.assertEqual(0,fit)

class test_FitnessForOneSeat(unittest.TestCase):

  def setUp(self):

    """ mock other functions """

    self.orig = {}
    self.orig['avecFitness'] = fitness.avecFitness
    self.orig['friendFitness'] = fitness.friendFitness
    self.orig['genderFitness'] = fitness.genderFitness
    self.orig['getNeighboursForSeat'] = fitness.getNeighboursForSeat
    fitness.getNeighboursForSeat = Mock(return_value=[])

  def tearDown(self):
    fitness.avecFitness = self.orig['avecFitness']
    fitness.friendFitness = self.orig['friendFitness']
    fitness.genderFitness = self.orig['genderFitness']
    fitness.getNeighboursForSeat = self.orig['getNeighboursForSeat']

  def setFitnessValues(self,avec=0,friends=0,gender=0):
    fitness.avecFitness = Mock(return_value=avec)
    fitness.friendFitness = Mock(return_value=friends)
    fitness.genderFitness = Mock(return_value=gender)
  
  def test_onlyAvec(self):
    self.setFitnessValues(avec=1)
    fit = fitness.fitnessForOneSeat([],[],[None],0)

    self.assertEqual(0.4,fit)

  def test_onlyFriends(self):
    self.setFitnessValues(friends=1)
    fit = fitness.fitnessForOneSeat([],[],[None],0)

    self.assertEqual(0.2,fit)

  def test_onlyGender(self):
    self.setFitnessValues(gender=1)
    fit = fitness.fitnessForOneSeat([],[],[None],0)

    self.assertEqual(0.4,fit)

class test_getNeighboursForSeat(unittest.TestCase):

  def setUp(self):
    self.seats = [[1,2],[3,0],[0,3],[2,1]]
    self.seating = [1,2,3,4]

  def test_getNeighbours(self):
    expected = [2,3]
    result = fitness.getNeighboursForSeat(self.seats,self.seating,0)
    self.assertEqual(expected,result)
