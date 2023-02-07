#include <cstring>
#include <cblas.h>
#include "mc_bench_blas.h"

int get_state_blas(
    double *initial_state,
    double *delta,
    double *transition,
    uint64_t n_state,
    uint64_t n_iter,
    double *out) {
    double *temp = new double[n_state];
    for (uint64_t i = 0; i < n_iter; ++i) {
        cblas_daxpy(n_state, 1, delta, 1, i & 1 ? temp : initial_state, 1);
        cblas_dgemm(
            CblasColMajor,
            CblasNoTrans,
            CblasNoTrans,
            n_state,
            1,
            n_state,
            1,
            transition,
            n_state,
            i & 1 ? temp : initial_state,
            n_state,
            0,
            i & 1 ? initial_state : temp,
            n_state
        );
    }
    memcpy(out, n_iter & 1 ? temp : initial_state, n_state * sizeof(double));
    delete[] temp;
    return 0;
}
