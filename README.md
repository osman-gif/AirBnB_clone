                          Welcome to the AirBnB clone project!
In this project we will build a command line interpreter to manage our objects.

A command line interpreter is just line the shell, we use it to run our commands from
terminal.

In our case, we want to be able to manage the objects of our project:
	• Create a new object (ex: a new User or a new Place)
	• Retrieve an object from a file, a database etc…
	• Do operations on objects (count, compute stats, etc…)
	• Update attributes of an object
	• Destroy an object

What we will build.
	1- A Base class (BaseModel) to take care of the serialization and deserialization
		of future instances
	2- create a simple flow of serialization/deserialization:
		Instance <-> Dictionary <-> JSON string <-> file
	3- create all classes used for AirBnB ( User , State , City , Place …)
		that inherit from BaseModel
	4- create the first abstracted storage engine of the project: File storage.
	5- create all unittests to validate all our classes and storage engine

How to start it.
	1- InterActive mode
		Type ./console.py in your terminal
	1- NoneInteractive mode
		example:
			Type echo "help" | ./console.py

