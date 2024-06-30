# MiBench Project

## Overview

This project is an extension of the [MiBench Version 1.0 benchmark suite](https://vhosts.eecs.umich.edu/mibench/), which provides a set of benchmark programs intended for evaluating the performance of microcontrollers and embedded systems. This repository includes the original C implementations of MiBench benchmarks, as well as their corresponding implementations in Python and Java.

Additionally, this project features scripts for obtaining performance outputs from the gem5 simulator and converting those outputs into inputs for the McPAT power, area, and timing modeling tool.

## Directory Structure

- `C/`: Contains the original MiBench Version 1.0 sample C code.
- `Python/`: Contains the MiBench benchmark implementations in Python.
- `Java/`: Contains the MiBench benchmark implementations in Java.
- `gem5ToMcPat/`: Contains scripts and templates for converting gem5 outputs to McPAT inputs.
  - `templates/`: Contains template files for x86 and ARM architectures.
  - `mcpat.py`: Script for converting gem5 outputs to McPAT inputs.
  - `mcpat.sh`: Example script for running the converter.
- `gem5_script.py`: A sample script to run python codes in x86 gem5.
  - `build/X86/gem5.opt -d output_dir_name gem5_script.py` 

## Getting Started

### Prerequisites

- [gem5](https://github.com/gem5/gem5/releases/tag/v23.1.0.0) simulator (Version: 23.1.0.0)
- Python 3.x
- Java Development Kit (JDK)
- [McPAT](https://github.com/HewlettPackard/mcpat/releases/tag/v1.3.0) tool (Version: 1.3)

### Running Benchmarks

1. Navigate to the specific language directory.
2. find your application
3. Run the runme_small.sh or runme_large.sh file
