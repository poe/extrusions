#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

class mount():
	def __init__(self,board_length = 160,board_width = 100,screw_offset = 10,screw_dia = 3.5,mount_thickness = 10):
		self.board_length = board_length
		self.board_width = board_width
		self.screw_offset = screw_offset
		self.screw_length = board_length - screw_offset
		self.screw_width = board_width - screw_offset
		self.screw_dia = screw_dia
		self.mount_thickness = mount_thickness

	def screws(self) -> OpenSCADObject:
		c = cylinder(r=self.screw_dia/2, h=20, segments = 32, center=True)
		screw = OpenSCADObject(name="union",params={})
		screw += translate([self.screw_length/2,self.screw_width/2,self.mount_thickness/2])(c)
		screw += translate([-self.screw_length/2,self.screw_width/2,self.mount_thickness/2])(c)
		screw += translate([self.screw_length/2,-self.screw_width/2,self.mount_thickness/2])(c)
		screw += translate([-self.screw_length/2,-self.screw_width/2,self.mount_thickness/2])(c)
		return screw

	def plate(self) -> OpenSCADObject:
		p = cube([self.board_length,self.board_width,self.mount_thickness],center = True)
		p-= self.screws()
		return p

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(35)
	a = e.tube()
	a = rotate(a=90,v=[0,0,1])(a)
	m = mount()	
	a = translate([90,0,-11])(a)
	a += m.plate()
	a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
