class Car(object):
	def __init__(self,name):
		self.name = name

	def say_hello(self):
		print("Hello, " + self.name)


class Scooter(object):
	def __init__(self,name):
		self.name = name

	def say_hello(self):
		print("Hello, " + self.name)
		
		
car_1 = Car('maruti')
scooter_1 = Scooter('hero')

Scooter.say_hello(car_1)