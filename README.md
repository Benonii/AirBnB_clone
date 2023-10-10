This project is the first step towards creating a clone of AirBnB. This project
will be accessed and executed throuhg a custom made CLI(command line interface).

This AirBnB console clone (we'll call it hbnb) is going to look like this:

	* It will have a class BaseModel that defines all common attributes/
	  methods for other classed
	* Public instance attributes : `id`, `created_at` and `updated_at`
	* `__str__` will print `[<class name>] (<self.id>) <self.__dict__>
	* Public instance methods: `save(self)`, `to_dict(self)`
	* Sub classes: `User`, `State`, `City`, `Amenity`, `Place`, `Review`

Presistence is maintained through a file storage system. Objects are stored in
a file using a JSON format.

The CLI will inherit from the cmd module. Type "./console.py" to run it.

It will have the following capabilities:

	* quit or EOF  to exit the program.
	* help.
	* A custom prompt "(hbnb)".
	* An empty line + `ENTER` shouldn't execute anything.
	* Will not be executed when imported.
	* create: Creates a new instance of BaseModel
	* show: Prints the string representation of an instance based on the
	  class name and `id`. EX: (hbnb) show BaseModel 1234-1234-1234
	* destroy: Deletes an instance based on the class name and `id`(save
	  the change into the JSON file).
	  Ex: (hbnb) destroy BaseModle 1234-1234-1234
	* all: Prints all string representation of all instances based or not
	  on the class name. Ex: (hbnb) all `BaseModel` or (hbnb) all
	* update: Updates an instance based on the class name and id by adding
	  or updating attributes(save the change into the JSON file).
	  EX: (hbnb) update BaseModel 1234-1234 email "hbnb@mail.com"
	* Arguments msut always be given in the right order
	* Each arguents are separated by a space
	* A string argument with a space must ne netween double quotes
	* The error management starts from the first argument to the last one.

EXAMPLE:

	./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) help quit
	Quit command to exit the program

	(hbnb) 
	(hbnb) 
	(hbnb) quit

