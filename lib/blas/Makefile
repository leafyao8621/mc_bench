CPP = g++
SRC = src/mc_bench_blas.cpp
OBJ = $(SRC:.cpp=.o)
LIB = libmcbenchblas.a
BIN = test

%.o: %.cpp
	$(CPP) -c $< -o $@

$(LIB): $(OBJ)
	ar rcs $(LIB) $(OBJ)
	cp src/mc_bench_blas.h ../../include

$(BIN): $(LIB)
	$(CPP) src/test.cpp -o $(BIN) -I ../../include -lmcbenchblas -pthread -lblis

.PHONY: clean
clean:
	@rm $(OBJ)
	@rm $(LIB)
	@rm $(BIN)
