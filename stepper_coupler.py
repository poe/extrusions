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

import numpy as np

# ============
# = GEOMETRY =
# ============



if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	tolerance = .5
	ch = 10 # coupler height
	od = 20 # outer diameter
	ind = 5 + tolerance # inner diameter
	ssd = 3 + tolerance # set srew diameter

	main_body = cylinder(r = od/2, h = ch, segments = 32) # main body
	shaft_hole = cylinder(r = ind/2, h = ch+1, segments = 32)
	set_screw_hole = cylinder(r = ssd/2, h = od / 2, segments = 32)
	set_screw_hole = rotate(90,v=FORWARD_VEC)(set_screw_hole)
	set_screw_hole = translate([0,0,ch/2])(set_screw_hole)
	a = main_body
	a -= shaft_hole
	a -= set_screw_hole

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
