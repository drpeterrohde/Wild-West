class Coordinate:

	def __init__(self, x, y):

		self.x = x
		self.y = y

	def __str__(self):

		return 'x = ' + this.x + ', y = ' + this.y

	def rotate(self, rotAngle):

		radius = math.sqrt(this.x^2 + this.y^2)
		theta  = math.atan2(this.y, this.x)

		theta += rotAngle

		self.x = radius * math.cos(theta)
		self.y = radius * math.sin(theta)

	def translate(self, deltaX, deltaY):

		self.x += deltaX
		self.y += deltaY
