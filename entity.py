class Entity:

	def __init__(self):

		self.name       = ''
		self.geometry   = Geometry()
		self.supply     = []
		self.demand     = []
		self.contracts  = []
		self.age        = 0
		self.supply     = []
		self.demand     = []
		self.possesions = []

	def __str__(self):

		string = 'Entity' + \
		'\n Name: '    + self.name + \
		' Age: '       + self.age + \
		' Geometry: '  + self.geometry.str() + \
		' Supply: '    + self.supply + \
		' Demand: '    + self.demand + \
		' Contracts: ' + self.contracts

		return string

	def evolve(self):

		self.age += 1

	def updateSupplyDemand(self):

		return