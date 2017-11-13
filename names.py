import random

firstMaleNames   = ['Peter', 'Philip', 'Josh']
firstFemaleNames = ['Sally', 'Miranda', 'Amanda']
lastNames        = ['Rohde', 'Bremhorst', 'Katzke']

class Names():

	def random(gender, inheritedName = None):

		firstName = ''
		lastNamer = ''

		if gender == 'male':
			firstName = random.choice(firstMaleNames)

		if gender == 'female':
			firstName = random.choice(firstFemaleNames)

		if inheritedName == None:
			lastName = random.choice(lastNames)
		else:
			lastName = inheritedName

		fullName = firstName + ' ' + lastName

		return [firstName, lastName, fullName]