#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

# from solid import *
# from solid.utils import *
from solid2 import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

class StandMount():
	def __init__(self,height = 100,mount_dia = 85, thickness = 10):
		self.height = height
		self.mount_dia = mount_dia
		self.thickness = thickness

	def mount(self):
		bg = cylinder(r = (self.mount_dia)/2, h = self.thickness, _fn = 256, center = True)
		return bg


	def bisect_floor(self,input):
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(70)
	m = StandMount()
	a = m.mount()
	t = e.one_end_tube()
	t = rotate(a = -90,v = (0,1,0))(t)
	t = translate([0,0,36])(t)
	a += t
	a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
