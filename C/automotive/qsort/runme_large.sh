#!/bin/sh
make clean
make
./qsort_large.o input_large.dat > output_large.txt
