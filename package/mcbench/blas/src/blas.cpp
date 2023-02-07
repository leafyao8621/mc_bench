#include <Python.h>
#include <numpy/arrayobject.h>
#include <mc_bench_blas.h>

#define GETSTATE(m) ((struct module_state*)PyModule_GetState(m))

struct module_state {
    PyObject* error;
};

static PyObject* get_state(PyObject* self, PyObject* args) {
    int64_t n_state, n_iter;
    PyObject *initial_state_raw, *delta_raw, *transition_raw, *out_raw;
    if (!PyArg_ParseTuple(args, "O!O!O!llO!",
                          &PyArray_Type,
                          &initial_state_raw,
                          &PyArray_Type,
                          &delta_raw,
                          &PyArray_Type,
                          &transition_raw,
                          &n_state,
                          &n_iter,
                          &PyArray_Type,
                          &out_raw)) {
        return NULL;
    }
    double *initial_state = (double*)PyArray_DATA(initial_state_raw);
    double *delta = (double*)PyArray_DATA(delta_raw);
    double *transition = (double*)PyArray_DATA(transition_raw);
    double *out = (double*)PyArray_DATA(out_raw);
    get_state_blas(
        initial_state,
        delta,
        transition,
        n_state,
        n_iter,
        out
    );
    Py_RETURN_NONE;
}

static PyMethodDef _blas_methods[] = {
    {"get_state", (PyCFunction)get_state, METH_VARARGS, NULL},
    {0}
};

static int _blas_traverse(PyObject *m, visitproc visit, void *arg) {
    Py_VISIT(GETSTATE(m)->error);
    return 0;
}

static int _blas_clear(PyObject *m) {
    Py_CLEAR(GETSTATE(m)->error);
    return 0;
}

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "mcbench_blas",
    NULL,
    sizeof(struct module_state),
    _blas_methods,
    NULL,
    _blas_traverse,
    _blas_clear,
    NULL
};

PyMODINIT_FUNC PyInit__blas(void) {
    PyObject *module = PyModule_Create(&moduledef);
    if (!module) return NULL;
    import_array();
    return module;
}
