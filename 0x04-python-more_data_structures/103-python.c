#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects.
 * @p: Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size, max_bytes;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    max_bytes = (size < 10) ? size : 10;

    printf("  size: %ld\n", size);
    printf("  trying string: ");
    for (i = 0; i < max_bytes; i++)
    {
        printf("%02x", ((unsigned char *)PyBytes_AsString(p))[i]);
        if (i < max_bytes - 1)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_list - Print information about Python lists.
 * @p: Python list.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;

    printf("[*] Python list info\n");
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyList_Check(item))
            print_python_list(item);
        else if (PyTuple_Check(item))
            print_python_list(item);
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyLong_Check(item))
            printf("int\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else
            printf("%s\n", Py_TYPE(item)->tp_name);
    }
}
