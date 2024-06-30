#!/bin/sh
javac FFT.java
java FFT 8 32768 > output_large.txt
java FFT 8 32768 -i > output_large.inv.txt