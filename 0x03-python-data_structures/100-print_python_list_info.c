#include <stdio.h>
#include <python.h>
/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject pointer (a Python list)
 */
{
	long int s, a, i;
    PyObject *pyitem;

	s = PyList_Size(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", a);

	for (i = 0; i < s; i++)
	{
		pyitem = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(pyitem)->tp_name);

	}
}
