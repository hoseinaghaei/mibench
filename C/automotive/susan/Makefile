all: susan arm

susan: susan.c Makefile
	gcc -static -O4 -o susan susan.c -lm 

arm:
	aarch64-none-linux-gnu-gcc -static susan.c  -o susan-arm -lm

clean:
	rm -rf susan susan-arm output*
