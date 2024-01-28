#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

class CameraMount():
	def __init__(self,camera_size = 40,screw_dia = 6.4, mount_thick = 2):
		self.camera_size = camera_size
		self.screw_dia = screw_dia
		self.mount_thick = mount_thick

	def screws(self) -> OpenSCADObject:
		screw = cylinder(r=self.screw_dia/2, h=20, segments = 32, center=True)
		screw = translate([0,50,0])(screw)
		return screw

	def camera_mount(self) -> OpenSCADObject:
		mm = cube([self.camera_size,self.camera_size*2,self.mount_thick], center=True)
		mm = translate([0,self.camera_size/2,0])(mm)
		mm -= self.screws()
		return mm

	def offset_block(self) -> OpenSCADObject:
		ob = cube([20,self.camera_size,self.mount_thick],center=True)
		ob = translate([-self.camera_size/2-8,0,0])(ob)
		return ob

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(10)
	m = CameraMount()
	a = m.camera_mount()
	t = e.one_end_tube()
	t = rotate(a = 90,v = (0,1,0))(t)
	t = translate([-53,0,-10])(t)
	b = m.offset_block()
	a += t + b
	a = rotate(a = 15, v = (0,1,0))(a)
	a = translate([0,0,2])(a)
	a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
