#! /usr/bin/env python3
# from solid.solidpython import *
from solid.solidpython import Path, scad_render_to_file
import sys

import extrusion_fittings as ef

if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	a = ef.corner_three_way()

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
