FILE = bitcnt_1.c bitcnt_2.c bitcnt_3.c bitcnt_4.c bitcnts.c bitfiles.c bitstrng.c bstr_i.c 

all : bitcnts arm

bitcnts: ${FILE} Makefile
	gcc -static ${FILE} -O3 -o bitcnts

arm:
	aarch64-none-linux-gnu-gcc -static ${FILE}  -o bitcnts-arm

clean:
	rm -rf bitcnts output*
