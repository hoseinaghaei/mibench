#!/bin/sh
python3 fft.py 8 32768 > output_small.txt
python3 fft.py 8 32768 -i > output_large.inv.txt
