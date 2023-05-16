#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* header */

/**
* print_python_list_info - prints some basic info about python lists
*
* @p: PyObject
*
* Return: basic info about a Python lists
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t p_size = 0;
	int i = 0;

	if(PyList_CheckExact(p))
	{
		p_size = PyList_Size(p);
		printf("[*] Size of the Python List = %zd\n", p_size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (i < p_size)
		{
			printf("Element %d: %s\n",
					i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
			i++;
		}
	}
}
