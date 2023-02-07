#ifndef CUBLAS_MC_BENCH_CUBLAS_H_
#define CUBLAS_MC_BENCH_CUBLAS_H_

#include <stdint.h>

int get_state_cublas(
    double *initial_state,
    double *delta,
    double *transition,
    uint64_t n_state,
    uint64_t n_iter,
    double *out);

#endif
