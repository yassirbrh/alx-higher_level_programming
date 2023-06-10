#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - Function
 *
 * Description: Prints same basic info about Python lists.
 *
 * @p: Pointer to the Python list object.
 *
 * Return: No return because it's a void function.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *pl = (PyListObject *)p;
	int size = (int)Py_SIZE(pl), i;
	const char *type;

	printf("[*] Size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)pl->allocated);
	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(PyList_GetItem(p, (Py_ssize_t)i))->tp_name;
		printf("Element %d: %s\n", i, type);
	}
}
