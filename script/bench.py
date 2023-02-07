import timeit
import numpy
import mcbench.numpy
import mcbench.blas
import mcbench.cublas

def generate_data(n_state: int):
    initial_state = numpy.zeros(n_state, dtype=numpy.double)
    initial_state[0] = 5
    delta = numpy.zeros(n_state, dtype=numpy.double)
    delta[0] = 10
    transition = numpy.zeros((n_state, n_state), dtype=numpy.double)
    idx = numpy.arange(0, n_state - 1, dtype=int)
    transition[idx, idx] = 0.9
    transition[idx, idx + 1] = 0.1
    transition[n_state - 1, n_state - 1] = 1
    return initial_state, delta, transition

def bench_numpy(n_state: int, n_iter: int):
    initial_state, delta, transition = generate_data(n_state)
    mcbench.numpy.get_state(initial_state, delta, transition, n_iter)

def bench_blas(n_state: int, n_iter: int):
    initial_state, delta, transition = generate_data(n_state)
    mcbench.blas.get_state(initial_state, delta, transition, n_iter)

def bench_cublas(n_state: int, n_iter: int):
    initial_state, delta, transition = generate_data(n_state)
    mcbench.cublas.get_state(initial_state, delta, transition, n_iter)

if __name__ == "__main__":
    res_cublas =\
        timeit.repeat(
            lambda: bench_cublas(10000, 100),
            repeat=5,
            number=1
        )
    print("cublas")
    print(res_cublas)
    res_blas =\
        timeit.repeat(
            lambda: bench_blas(10000, 100),
            repeat=5,
            number=1
        )
    print("blas")
    print(res_blas)
    res_numpy =\
        timeit.repeat(
            lambda: bench_numpy(10000, 100),
            repeat=5,
            number=1
        )
    print("numpy")
    print(res_numpy)
