# In this project, I encapsulated skills in Python object-oriented programming by coding three connected classes to represent rectangles and squares. I wrote my own test suite using the unittest module to test all functionality for each class.


## tests/:

All your files, classes and methods must be unit tested and be PEP 8 validated.


	guillaume@ubuntu:~/$ python3 -m unittest discover tests
	...................................................................................
	...................................................................................
	.......................
	----------------------------------------------------------------------
	Ran 189 tests in 13.135s
	
	OK
	guillaume@ubuntu:~/$

-----------------------------------------------------------------------------------------------------------------------------------------------------


## base.py:

Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:

private class attribute __nb_objects = 0

class constructor: def __init__(self, id=None)::

if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it

otherwise, increment __nb_objects and assign the new value to the public instance attribute id

This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)


	guillaume@ubuntu:~/$ cat 0-main.py
	#!/usr/bin/python3
	""" 0-main """
	from models.base import Base
	
	if __name__ == "__main__":
	
	    b1 = Base()
	    print(b1.id)
	
	    b2 = Base()
	    print(b2.id)
	
	    b3 = Base()
	    print(b3.id)
	
	    b4 = Base(12)
	    print(b4.id)
	
	    b5 = Base()
	    print(b5.id)
	
	guillaume@ubuntu:~/$ ./0-main.py
	1
	2
	3
	12
	4
	guillaume@ubuntu:~/$ 

-----------------------------------------------------------------------------------------------------------------------------------------------------

