all: patricia arm

patricia: patricia.c patricia_test.c
	gcc -static patricia.c patricia_test.c -O3 -o patricia -ltirpc


arm:
	aarch64-none-linux-gnu-gcc -static patricia.c patricia_test.c -o patricia-arm

clean:
	rm -rf patricia output* patricia-arm
