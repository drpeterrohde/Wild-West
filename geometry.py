from coordinate import *

class Geometry:

	def __init__(self):

		self.location = Coordinate(0,0)
		self.region   = [Coordinate(0,0)]

	def __str__(self):

		string =  'Geometry' + \
		'\n Location: '      + this.location + \
		'\n Region: '        + this.region

		return string

	def rotate(self, theta):

		self.location.rotate(theta)

		for coord in this.region:
			coord.rotate(theta)

	def translate(self, deltaX, deltaY):

		self.location.translate(deltaX, deltaY)

		for coord in this.region:
			coord.translate(deltaX, deltaY)