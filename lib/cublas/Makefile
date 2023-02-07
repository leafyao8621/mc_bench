NVCC = nvcc
CC = g++
SRC = src/mc_bench_cublas.cu
OBJ = $(SRC:.cu=.o)
LIB = libmcbenchcublas.a
BIN = test

%.o: %.cu
	$(NVCC) -O2 -c $< -o $@

$(LIB): $(OBJ)
	ar rcs $(LIB) $(OBJ)
	cp src/mc_bench_cublas.h ../../include

$(BIN): $(LIB)
	$(CC) src/test.cpp -O2 -o $(BIN) -I ../../include -L . -lmcbenchcublas -lcublas -lcudart

.PHONY: clean
clean:
	@rm $(OBJ)
	@rm $(LIB)
	@rm $(BIN)
