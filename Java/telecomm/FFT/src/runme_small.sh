#!/bin/sh
javac FFT.java
java FFT 4 4096 > output_small.txt
java FFT 4 4096 -i > output_small.inv.txt
