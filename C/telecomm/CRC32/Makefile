all: crc arm

crc: crc_32.c Makefile
	gcc -static crc_32.c -O3 -o crc 

arm:
	aarch64-none-linux-gnu-gcc -static crc_32.c -o crc-arm

clean:
	rm -rf crc output* crc-arm
