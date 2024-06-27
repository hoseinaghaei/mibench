#!/bin/sh
python3 fft.py 4 4096 > output_small.txt
python3 fft.py 4 4096 -i > output_large.inv.txt

