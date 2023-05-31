## 0-square.py:

Write an empty class Square that defines a square:

You are not allowed to import any module


	guillaume@ubuntu:~/0x06$ cat 0-main.py
	#!/usr/bin/python3
	Square = __import__('0-square').Square
	
	my_square = Square()
	print(type(my_square))
	print(my_square.__dict__)
	
	guillaume@ubuntu:~/0x06$ ./0-main.py
	<class '0-square.Square'>
	{}
	guillaume@ubuntu:~/0x06$ 

-----------------------------------------------------------------------------------------------------------------------------------------------------

## 1-square.py:

Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size

Instantiation with size (no type/value verification)

You are not allowed to import any module

Why?


Why size is private attribute?


The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.


	guillaume@ubuntu:~/0x06$ cat 1-main.py
	#!/usr/bin/python3
	Square = __import__('1-square').Square
	
	my_square = Square(3)
	print(type(my_square))
	print(my_square.__dict__)
	
	try:
	    print(my_square.size)
	except Exception as e:
	    print(e)
	
	try:
	    print(my_square.__size)
	except Exception as e:
	    print(e)
	
	guillaume@ubuntu:~/0x06$ ./1-main.py
	<class '1-square.Square'>
	{'_Square__size': 3}
	'Square' object has no attribute 'size'
	'Square' object has no attribute '__size'
	guillaume@ubuntu:~/0x06$ 

-----------------------------------------------------------------------------------------------------------------------------------------------------
