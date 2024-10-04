FILE1 = qsort_small.c
FILE2 = qsort_large.c

all: qsort_small qsort_large qsort_arm

qsort_small: qsort_small.c Makefile
	gcc -static qsort_small.c -O3 -o qsort_small.o -lm
qsort_large: qsort_large.c Makefile
	gcc -static qsort_large.c -O3 -o qsort_large.o -lm

qsort_arm:
	aarch64-none-linux-gnu-gcc -static qsort_small.c -o qsort-arm

clean:
	rm -rf qsort_small.o qsort_large.o output* qsort-arm
