class Manager:
	def __init__(self, name, department, age):
		self.name = name
		self.department = department
		self.age = age
		Manager.say_hello_everytime()

	def say_hello_everytime():
		print("hi, how are you? Regardless whatever you are.")

manager = Manager('Suresh', 'CSE', 25)