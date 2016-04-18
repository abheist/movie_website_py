# This file contains the concepts of inheritence.

# This is the parent class
class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

	# This method is called when to print the info on console about the movie
	def show_info(self):
		print("Last Name - "+self.last_name)
		print("Eye Color - "+self.eye_color)


# This is the child/sub class
class Child(Parent):
	def  __init__(self, last_name, eye_color, number_of_toys):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	# This is basically showing the method overriding mechanism
	# After inheriting the function from the parent class, it overriding it.
	def show_info(self):
		print("Last Name - "+self.last_name)
		print("Eye Color - "+self.eye_color)
		print("Number of toys = "+self.number_of_toys)


# Making instances of the classes and calling them
billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)
billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)