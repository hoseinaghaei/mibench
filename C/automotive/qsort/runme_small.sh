#!/bin/sh
make clean
make
./qsort_small.o input_small.dat > output_small.txt
