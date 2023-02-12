from setuptools import setup, Extension
import numpy

blas =\
    Extension(
        'mcbench._blas',
        sources=["mcbench/blas/src/blas.cpp"],
        include_dirs=[
            numpy.get_include(),
            "/mnt/vault/mc_bench/include"
        ],
        library_dirs=[
            "/mnt/vault/mc_bench/lib/blas"
        ],
        libraries=["mcbenchblas", "blis"],
        extra_link_args=["-pthread"]
    )

cublas =\
    Extension(
        'mcbench._cublas',
        sources=["mcbench/cublas/src/cublas.cpp"],
        include_dirs=[
            numpy.get_include(),
            "/mnt/vault/mc_bench/include"
        ],
        library_dirs=[
            "/mnt/vault/mc_bench/lib/cublas"
        ],
        libraries=["mcbenchcublas", "cublas", "cudart"],
        extra_link_args=["-pthread"]
    )

setup(
    name="mcbench",
    version="0.1",
    packages=[
        "mcbench",
        "mcbench.numpy",
        "mcbench.blas",
        "mcbench.cublas"
    ],
    ext_modules=[blas, cublas]
)
