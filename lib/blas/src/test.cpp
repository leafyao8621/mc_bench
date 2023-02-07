#include <iostream>

#include <mc_bench_blas.h>

int main(void) {
    double initial_state[3] = {
        5,
        0,
        0
    };
    double delta[3] = {
        10,
        0,
        0
    };
    double transition[9] = {
        0.9, 0.1, 0,
        0, 0.7, 0.3,
        0, 0, 1
    };
    double out[3] = {0};
    get_state_blas(initial_state, delta, transition, 3, 100000, out);
    double *iter = out;
    std::cout.precision(15);
    for (int i = 0; i < 3; ++i, ++iter) {
        std::cout << *iter << std::endl;
    }
    return 0;
}
