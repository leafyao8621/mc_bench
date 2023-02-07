#ifndef CUBLAS_MC_BENCH_BLAS_H_
#define CUBLAS_MC_BENCH_BLAS_H_

#include <stdint.h>

int get_state_blas(
    double *initial_state,
    double *delta,
    double *transition,
    uint64_t n_state,
    uint64_t n_iter,
    double *out);

#endif
