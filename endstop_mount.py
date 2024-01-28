#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

class EndStopMount():
	def __init__(self,endstop_size = 34,screw_dia = 4, mount_thick = 6):
		self.endstop_size = endstop_size
		self.screw_dia = screw_dia
		self.mount_thick = mount_thick

	def screws(self) -> OpenSCADObject:
		screw = cylinder(r=self.screw_dia/2, h=20, segments = 32, center=True)
		screws = translate([10,-10,0])(screw)
		screws += translate([-10,-10,0])(screw)
		return screws

	def endstop_mount(self) -> OpenSCADObject:
		mm = cube([self.endstop_size,self.endstop_size,self.mount_thick], center=True)
		mm -= self.screws()
		mm = rotate(a = 90,v = (0,1,0))(mm)
		mm = translate([2,-10,17])(mm)
		return mm

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(31)
	m = EndStopMount()
	a = m.endstop_mount()
	t = e.tube()
	t = rotate(a = 90,v = (0,1,0))(t)
	t = translate([15,0,30])(t)
	t = translate([0,0,-12])(t)
	a += t
	a = rotate(a = 90, v = (0,1,0))(a)
	a = translate([0,0,5])(a)
	a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
