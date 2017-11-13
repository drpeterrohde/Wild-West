from entity import *
from names import *
import random

class Person(Entity):

	def __init__(self, inheritedName = None):

		super().__init__()
		self.gender    = random.choice(['male', 'female'])
		[self.firstName, self.lastName, self.name] = Names.random(self.gender, inheritedName)

	def __str__(self):

		return #super().str() + '\n Gender: ' + self.gender

