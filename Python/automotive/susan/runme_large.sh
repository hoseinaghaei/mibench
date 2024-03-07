#!/bin/sh
python3 susan.py ../../../C/automotive/susan/input_large.pgm output_large.smoothing.pgm -s
python3 susan.py ../../../C/automotive/susan/input_large.pgmoutput_large.edges.pgm -e
python3 susan.py ../../../C/automotive/susan/input_large.pgm output_large.corners.pgm -c

