import numpy
import mcbench.numpy
import mcbench.blas
import mcbench.cublas

if __name__ == "__main__":
    res =\
        mcbench.numpy.get_state(
            numpy.array([5, 0, 0], dtype=numpy.double),
            numpy.array([10, 0, 0], dtype=numpy.double),
            numpy.array(
                [
                    [0.9, 0.1, 0],
                    [0, 0.7, 0.3],
                    [0, 0, 1]
                ],
                dtype=numpy.double
            ),
            100000
        )
    print(res)
    res =\
        mcbench.blas.get_state(
            numpy.array([5, 0, 0], dtype=numpy.double),
            numpy.array([10, 0, 0], dtype=numpy.double),
            numpy.array(
                [
                    [0.9, 0.1, 0],
                    [0, 0.7, 0.3],
                    [0, 0, 1]
                ],
                dtype=numpy.double
            ),
            100000
        )
    print(res)
    res =\
        mcbench.cublas.get_state(
            numpy.array([5, 0, 0], dtype=numpy.double),
            numpy.array([10, 0, 0], dtype=numpy.double),
            numpy.array(
                [
                    [0.9, 0.1, 0],
                    [0, 0.7, 0.3],
                    [0, 0, 1]
                ],
                dtype=numpy.double
            ),
            100000
        )
    print(res)
