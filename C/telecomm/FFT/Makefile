OBJ = main.o fftmisc.o fourierf.o
ARM_OBJ = main-arm.o fftmisc-arm.o fourierf-arm.o
FILE = main.c fftmisc.c fourierf.c
CFLAGS = -static -O3 -g
ARM_CFLAGS = -static -O3 -g
ARM_COMPILER = aarch64-none-linux-gnu-gcc

all: fft arm

# Native FFT target
fft: ${OBJ} Makefile
	gcc ${CFLAGS} ${OBJ} -o fft -lm

# ARM FFT target
arm: ${ARM_OBJ} Makefile
	${ARM_COMPILER} ${ARM_CFLAGS} ${ARM_OBJ} -o fft-arm -lm

# Native object files
fftmisc.o: fftmisc.c
	gcc ${CFLAGS} -c fftmisc.c
fourierf.o: fourierf.c
	gcc ${CFLAGS} -c fourierf.c
main.o: main.c
	gcc ${CFLAGS} -c main.c

# ARM object files
fftmisc-arm.o: fftmisc.c
	${ARM_COMPILER} ${ARM_CFLAGS} -c fftmisc.c -o fftmisc-arm.o
fourierf-arm.o: fourierf.c
	${ARM_COMPILER} ${ARM_CFLAGS} -c fourierf.c -o fourierf-arm.o
main-arm.o: main.c
	${ARM_COMPILER} ${ARM_CFLAGS} -c main.c -o main-arm.o

# Clean up object files and binaries
clean:
	rm -rf *.o fft fft-arm output*

