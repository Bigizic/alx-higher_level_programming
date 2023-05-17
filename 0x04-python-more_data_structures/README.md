## 0-square_matrix_simple.py:

Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):

matrix is a 2 dimensional array

Returns a new matrix:

Same size as matrix

Each value should be the square of the value of the input

Initial matrix should not be modified

You are not allowed to import any module

You are allowed to use regular loops, map, etc.



	guillaume@ubuntu:~/0x04$ cat 0-main.py
	#!/usr/bin/python3
	square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple
	
	matrix = [
	    [1, 2, 3],
	    [4, 5, 6],
	    [7, 8, 9]
	]
	
	new_matrix = square_matrix_simple(matrix)
	print(new_matrix)
	print(matrix)
	
	guillaume@ubuntu:~/0x04$ ./0-main.py
	[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
	[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	guillaume@ubuntu:~/0x04$

-----------------------------------------------------------------------------------------------------------------------------------------------------

## 1-search_replace.py:

Write a function that replaces all occurrences of an element by another in a new list.

Prototype: def search_replace(my_list, search, replace):

my_list is the initial list

search is the element to replace in the list

replace is the new element

You are not allowed to import any module


	guillaume@ubuntu:~/0x04$ cat 1-main.py
	#!/usr/bin/python3
	search_replace = __import__('1-search_replace').search_replace
	
	my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
	new_list = search_replace(my_list, 2, 89)
	
	print(new_list)
	print(my_list)
	
	guillaume@ubuntu:~/0x04$ ./1-main.py
	[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
	[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
	guillaume@ubuntu:~/0x04$ 

-----------------------------------------------------------------------------------------------------------------------------------------------------
