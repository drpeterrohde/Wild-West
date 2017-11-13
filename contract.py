class Contract:

	def __init__(self, Alice, Bob):

		self.alice = Alice
		self.bob   = Bob
		self.age   = 0

	def __str__(self):

		string = 'Contract' + \
		'\n Alice: '        + this.alice + \
		'\n Bob: '          + this.bob + \
		'\n Age: '          + this.age

		return string

	def execute(self):

		return

	def evolve(self):

		self.age += 1