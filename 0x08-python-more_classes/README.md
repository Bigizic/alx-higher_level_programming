## 0-rectangle.py:

Write an empty class Rectangle that defines a rectangle:

You are not allowed to import any module


	guillaume@ubuntu:~/0x08$ cat 0-main.py
	#!/usr/bin/python3
	Rectangle = __import__('0-rectangle').Rectangle
	
	my_rectangle = Rectangle()
	print(type(my_rectangle))
	print(my_rectangle.__dict__)
	
	guillaume@ubuntu:~/0x08$ ./0-main.py
	<class '0-rectangle.Rectangle'>
	{}
	guillaume@ubuntu:~/0x08$ 

-------------------------------------------------------------------------------------------------------------------------------------------------

## 1-rectangle.py:

Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

Private instance attribute: width:

property def width(self): to retrieve it

property setter def width(self, value): to set it:

width must be an integer, otherwise raise a TypeError exception with the message width must be an integer

if width is less than 0, raise a ValueError exception with the message width must be >= 0

Private instance attribute: height:

property def height(self): to retrieve it

property setter def height(self, value): to set it:

height must be an integer, otherwise raise a TypeError exception with the message height must be an integer

if height is less than 0, raise a ValueError exception with the message height must be >= 0

Instantiation with optional width and height: def __init__(self, width=0, height=0):

You are not allowed to import any module


	guillaume@ubuntu:~/0x08$ cat 1-main.py
	#!/usr/bin/python3
	Rectangle = __import__('1-rectangle').Rectangle
	
	my_rectangle = Rectangle(2, 4)
	print(my_rectangle.__dict__)
	
	my_rectangle.width = 10
	my_rectangle.height = 3
	print(my_rectangle.__dict__)
	
	guillaume@ubuntu:~/0x08$ ./1-main.py
	{'_Rectangle__height': 4, '_Rectangle__width': 2}
	{'_Rectangle__height': 3, '_Rectangle__width': 10}
	guillaume@ubuntu:~/0x08$ 

---------------------------------------------------------------------------------------------------------------------------------------------------
