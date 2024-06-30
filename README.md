# MiBench Project

## Overview

This project is an extension of the MiBench Version 1.0 benchmark suite, which provides a set of benchmark programs intended for evaluating the performance of microcontrollers and embedded systems. This repository includes the original C implementations of MiBench benchmarks, as well as their corresponding implementations in Python and Java.

Additionally, this project features scripts for obtaining performance outputs from the gem5 simulator and converting those outputs into inputs for the McPAT power, area, and timing modeling tool.

## Directory Structure

- `C/`: Contains the original MiBench Version 1.0 sample C code.
- `Python/`: Contains the MiBench benchmark implementations in Python.
- `Java/`: Contains the MiBench benchmark implementations in Java.
- `gem5ToMcPat/`: Contains scripts and templates for converting gem5 outputs to McPAT inputs.
  - `templates/`: Contains template files for x86 and ARM architectures.
  - `mcpat.py`: Script for converting gem5 outputs to McPAT inputs.
  - `mcpat.sh`: Example script for running the converter.

## Getting Started

### Prerequisites

- gem5 simulator (Version: 23.1.0.0)
- Python 3.x
- Java Development Kit (JDK)
- McPAT tool (Version: 1.3)

### Running Benchmarks

1. Navigate to the specific language directory.
2. find your application
3. Run the runme_small.sh or runme_large.sh file
