class Car:
	def __init__(self, model, mileage):
		self.model = model
		self.mileage = mileage
		self.bleh_bleh = "bleh bleh bleh"

	def __str__(self):
		return "{}, {}".format(self.model, self.mileage)

	def __repr__(self):
		return "{}".format(self.model)

	def __add__(self, other, num):
		return self.mileage + other.mileage + num

	def __eq__(self, other):
		return self.mileage == other.mileage


car_1 = Car('Maruti 800', 45)

car_2 = Car('Ferrari 500CC', 45)


print(car_1.__add__(car_2, 10))