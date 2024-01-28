#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

class ClipMount():
	def __init__(self,clip_size = 35,screw_dia = 4.4, mount_thick = 6):
		self.clip_size = clip_size
		self.screw_dia = screw_dia
		self.mount_thick = mount_thick

	def screws(self) -> OpenSCADObject:
		screw = cylinder(r=self.screw_dia/2, h=20, segments = 32, center=True)
		return screw

	def clip_mount(self) -> OpenSCADObject:
		mm = cube([self.clip_size,self.clip_size,self.mount_thick], center=True)
		mm -= self.screws()
		return mm

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(10)
	m = ClipMount()
	a = m.clip_mount()
	t = e.one_end_tube()
	t = rotate(a = 90,v = (0,1,0))(t)
	# t = translate([-53,0,-30])(t)
	t = translate([0,0,-12])(t)
	a += t
	a = rotate(a = 45, v = (0,1,0))(a)
	a = translate([0,0,5])(a)
	a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
