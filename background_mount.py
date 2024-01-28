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

class BackgroundMount():
	def __init__(self,background_height = 190,background_dia = 200, thickness = 2):
		self.background_height = background_height
		self.background_dia = background_dia
		self.thickness = thickness

	def background(self):
		bg = cylinder(r = (self.background_dia+self.thickness)/2, h = self.background_height-self.thickness, _fn = 256, center = True)
		bg_cutout = cylinder(r = self.background_dia/2, h = self.background_height, _fn = 256, center = True)
		bg_cutoff = cube(self.background_dia*2,self.background_dia*2,self.background_height*2,center = True)
		bg_cutoff = translate([self.background_dia,0,0])(bg_cutoff)
		return bg - (bg_cutout + bg_cutoff)

	def shade(self):
		shade = cylinder(r = self.background_dia/2+10, h = self.background_height, _fn = 256, center = True)
		shade_cutout = cylinder(r = self.background_dia/2-20, h = self.background_height + 10, _fn = 256, center = True)
		shade_cutoff = cube(self.background_dia*2,self.background_dia*2,self.background_height*2,center = True)
		shade_cutoffs = translate([self.background_dia,0,0])(shade_cutoff)
		shade_cutoffs += translate([0,0,-100])(shade_cutoff)
		return shade  - (shade_cutout + shade_cutoffs)

	def bisect_floor(self,input):
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor

	def cutoff_cube(self):
		cc = cube([120,40,60],center = True)
		cc = rotate(a=45,v=[0,45,0])(cc)
		cc = translate([0,0,-20])(cc)
		return cc


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(40)
	m = BackgroundMount()
	a = m.background()
	a += translate([0,0,-184])(m.shade())
	t = e.one_end_tube()
	t = rotate(a = 270,v = (0,1,0))(t)
	t -= m.cutoff_cube()
	t = translate([-114,0,56])(t)
	a += t
	# a = rotate(a = 15, v = (0,1,0))(a)
	a = translate([0,0,92])(a)
	# a = m.bisect_floor(a)
	# a = m.shade()

	file_out = scad_render_to_file(a,  out_dir=out_dir)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
