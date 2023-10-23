#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    PyListObject *list;
    Py_ssize_t size, i;

    printf("[*] Python list info\n");

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_GET_SIZE(p);

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %zd: %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
        if (strcmp(Py_TYPE(PyList_GET_ITEM(p, i))->tp_name, "bytes") == 0) {
            printf("[.] bytes object info\n");
            print_python_bytes(PyList_GET_ITEM(p, i));
        }
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_GET_SIZE(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", bytes->ob_sval[i] & 0xff);
        if (i + 1 < size && i + 1 < 10) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    printf("[.] float object info\n");

    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = ((PyFloatObject *)p)->ob_fval;
    printf("  value: %f\n", value);
}
