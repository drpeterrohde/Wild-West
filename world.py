class World:

	def __init__(self):

		self.entities = []

	def __str__(self):

		return ''

	def evolve(self):

		self.time += 1

	def addEntity(self, entity):

		self.entities.append(entity)

	def removeEntity(self, entity):

		self.entities.remove(entity)
