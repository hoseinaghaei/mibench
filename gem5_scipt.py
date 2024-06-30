import os

from m5.objects import *
import sys

# Import the cache classes
from caches import L1ICache, L1DCache, L2Cache

# Create the system we are going to simulate
system = System()

# Set the clock frequency of the system (and all of its children)
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = "1GHz"
system.clk_domain.voltage_domain = VoltageDomain()
system.clk_domain.voltage_domain.voltage = "0.9V"

system.cache_line_size = 64

# Set up the system
system.mem_mode = "timing"  # Use timing accesses
system.mem_ranges = [AddrRange("8GB")]  # Create an address range

# Create multiple CPUs
num_cpus = 4  # Number of CPUs
system.cpu = [X86O3CPU() for i in range(num_cpus)]

# Create L1 caches for each CPU
for cpu in system.cpu:
    cpu.icache = L1ICache()
    cpu.dcache = L1DCache()

    # Connect the instruction and data caches to the CPU
    cpu.icache.connectCPU(cpu)
    cpu.dcache.connectCPU(cpu)

# Create a memory bus, a system crossbar, in this case
system.l2bus = L2XBar()

# Hook the CPU ports up to the l2bus
for cpu in system.cpu:
    cpu.icache.connectBus(system.l2bus)
    cpu.dcache.connectBus(system.l2bus)

# Create an L2 cache and connect it to the l2bus
system.l2cache = L2Cache()
system.l2cache.connectCPUSideBus(system.l2bus)

# Create a memory bus
system.membus = SystemXBar()

# Connect the L2 cache to the membus
system.l2cache.connectMemSideBus(system.membus)

for cpu in system.cpu:
    # Create the interrupt controller for the CPU and connect to the membus
    cpu.createInterruptController()
    cpu.interrupts[0].pio = system.membus.mem_side_ports
    cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
    cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Create a DDR3 memory controller and connect it to the membus
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# Connect the system up to the membus
system.system_port = system.membus.cpu_side_ports

# Set the X86 "hello world" binary
binary = "/usr/bin/python3"
# binary = "/home/aghaei/PycharmProjects/mibench/Python/automotive/bitcount/dist/bitcnts"

system.workload = SEWorkload.init_compatible(binary)

# Create a process for the bitcount application
process = Process()
process.cmd = [binary, "/home/aghaei/PycharmProjects/mibench/Python/automotive/basicmath/basicmath_small.py"]

for cpu in system.cpu:
    cpu.workload = process
    cpu.createThreads()

# Set up the root SimObject and start the simulation with fast-forwarding
root = Root(full_system=False, system=system)

m5.instantiate()

print("Beginning simulation with multiple CPUs and two-level cache system!")
exit_event = m5.simulate()

print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")