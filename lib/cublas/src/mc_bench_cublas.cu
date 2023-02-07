#include <cublas_v2.h>

#include "mc_bench_cublas.h"

int get_state_cublas(
    double *initial_state,
    double *delta,
    double *transition,
    uint64_t n_state,
    uint64_t n_iter,
    double *out) {
    double *d_out_odd = 0;
    cublasHandle_t handle;
    cudaMalloc(&d_out_odd, n_state * sizeof(double));
    cudaMemcpy(
        d_out_odd,
        initial_state,
        n_state * sizeof(double),
        cudaMemcpyHostToDevice
    );
    double *d_delta = 0;
    cudaMalloc(&d_delta, n_state * sizeof(double));
    cudaMemcpy(
        d_delta,
        delta,
        n_state * sizeof(double),
        cudaMemcpyHostToDevice
    );
    double *d_transition = 0;
    cudaMalloc(&d_transition, n_state * n_state * sizeof(double));
    cudaMemcpy(
        d_transition,
        transition,
        n_state * n_state * sizeof(double),
        cudaMemcpyHostToDevice
    );
    double *d_out_even = 0;
    cudaMalloc(&d_out_even, n_state * sizeof(double));
    double alpha = 1;
    double beta = 0;
    cublasCreate(&handle);
    for (uint64_t i = 0; i < n_iter; ++i) {
        cublasDaxpy_v2(
            handle,
            n_state,
            &alpha,
            d_delta,
            1,
            i & 1 ? d_out_even : d_out_odd,
            1
        );
        cublasDgemm_v2(
            handle,
            CUBLAS_OP_N,
            CUBLAS_OP_N,
            n_state,
            1,
            n_state,
            &alpha,
            d_transition,
            n_state,
            i & 1 ? d_out_even : d_out_odd,
            n_state,
            &beta,
            i & 1 ? d_out_odd : d_out_even,
            n_state
        );
    }
    cublasDestroy(handle);
    cudaFree(d_delta);
    cudaFree(d_transition);
    cudaMemcpy(
        out,
        n_iter & 1 ? d_out_even : d_out_odd,
        n_state * sizeof(double),
        cudaMemcpyDeviceToHost
    );
    cudaFree(d_out_odd);
    cudaFree(d_out_even);
    return 0;
}
