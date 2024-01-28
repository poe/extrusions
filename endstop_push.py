#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

class EndStopPush():
	def __init__(self,endstop_width = 34,endstop_length = 33,screw_dia = 4, push_thick = 6):
		self.endstop_width = endstop_width
		self.endstop_length = endstop_length
		self.screw_dia = screw_dia
		self.push_thick = push_thick

	def endstop_push(self) -> OpenSCADObject:
		mm = cube([self.endstop_width,self.endstop_length,self.push_thick], center=True)
		mm = rotate(a = 90,v = (0,1,0))(mm)
		mm = translate([2,-28,17])(mm)
		return mm

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(20)
	m = EndStopPush()
	a = m.endstop_push()
	t = e.tube()
	t = rotate(a = 90,v = (0,1,0))(t)
	t = translate([15.3,0,30])(t)
	t = translate([0,0,-12])(t)
	a += t
	a = rotate(a = 90, v = (0,1,0))(a)
	a = translate([0,0,5])(a)
	a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
