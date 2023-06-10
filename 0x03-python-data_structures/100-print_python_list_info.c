#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *pl = (PyListObject *)p;
	long int size = PyList_Size(p);
	int i;
	const char *type;

	printf("[*] Size of the python List = %li\n", size);
	printf("[*] Allocated = %d\n", (int)pl->allocated);
	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(pl->ob_item[i])->tp_name;
		printf("Element %d: %s\n", i, type);
	}
}
