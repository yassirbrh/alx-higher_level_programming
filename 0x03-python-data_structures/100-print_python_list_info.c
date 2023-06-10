#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
        PyListObject *pl = (PyListObject *)p;
        int size = (int)Py_SIZE(pl), i;

        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", (int)pl->allocated);
        for (i = 0; i < size; i++)
                printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
