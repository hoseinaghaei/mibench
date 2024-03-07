#!/bin/sh
python3 susan.py ../../../C/automotive/susan/input_small.pgm output_small.smoothing.pgm -s
python3 susan.py ../../../C/automotive/susan/input_small.pgm output_small.edges.pgm -e
python3 susan.py ../../../C/automotive/susan/input_small.pgm output_small.corners.pgm -c

