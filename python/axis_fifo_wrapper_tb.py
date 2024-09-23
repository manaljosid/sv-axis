from pathlib import Path
import random

import vunit_common

# NOTE: This assumes the location of the directories relative to where this is run from
WORKSPACE = Path(__file__).parent / ".." / ".." / ".." / ".." / "workspace" / "modelsim"
LIB_ROOT = Path(__file__).parent / ".." / "lib"
SYN_ROOT = Path(__file__).parent / ".." / "syn"
SIM_ROOT = Path(__file__).parent / ".." / "sim"

vu, lib = vunit_common.init(WORKSPACE)

vunit_common.add_source(lib, LIB_ROOT / "./verilog-axis/rtl/axis_fifo.v")
vunit_common.add_source(lib, SYN_ROOT / "./axis_if/axis_if.sv")
vunit_common.add_source(lib, SYN_ROOT / "./axis_fifo_wrapper/axis_fifo_wrapper.sv")
vunit_common.add_source(lib, SIM_ROOT / "./axis_bfm/axis_bfm.sv")
vunit_common.add_source(lib, SIM_ROOT / "./axis_fifo_wrapper/axis_fifo_wrapper_tb.sv")

# Create testbench
tb = lib.test_bench("axis_fifo_wrapper_tb")

tb.add_config("TDATA=0x08", parameters={
    "TDATA"             : 8,
    "TSTRB"             : 1,
    "TKEEP"             : 1,
    "AXIS_TID_WIDTH"    : 8,
    "TID"               : 5,
    "AXIS_TDEST_WIDTH"  : 8,
    "TDEST"             : 3,
    "AXIS_TUSER_WIDTH"  : 3,
    "TUSER"             : 2
    })

tb.add_config("TDATA_WIDTH=64_TDATA=0x25", parameters={
    "AXIS_TDATA_WIDTH"  : 64,
    "TDATA"             : 0x25,
    "TSTRB"             : 1,
    "TKEEP"             : 1,
    "AXIS_TID_WIDTH"    : 8,
    "TID"               : 5,
    "AXIS_TDEST_WIDTH"  : 8,
    "TDEST"             : 3,
    "AXIS_TUSER_WIDTH"  : 3,
    "TUSER"             : 2
    })

vu.main()