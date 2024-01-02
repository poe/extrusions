#! /usr/bin/env python3
from solid.objects import *
from solid.solidpython import *
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from euclid3 import Point2, Point3, Vector3

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

def bisect_floor(input) -> OpenSCADObject:
	size = 300
	floor = translate([0,0,-150])(cube([300,300,300],center = True))
	return input - floor

if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent
	hole = translate([0,0,7])(cylinder(r = 11.1, h = 18))
	hole +=  translate([0,0,6.5])(cylinder(r = 10.9, h = 20))

	mount = cube([25,25,25],center=True) - (hole)
	a = bisect_floor(mount)
#	a = hole
	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
