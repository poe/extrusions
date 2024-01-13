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
	def __init__(self,board_length = 97,board_width = 63,plate_length = 120,plate_width = 90, mount_thickness = 5,
					fan_gap_length = 94,fan_gap_width = 60):
		self.board_length = board_length
		self.board_width = board_width
		self.plate_length = plate_length
		self.plate_width = plate_width
		self.mount_thickness = mount_thickness
		self.fan_gap_length = fan_gap_length
		self.fan_gap_width = fan_gap_width

	def ziptie_cutouts(self) -> OpenSCADObject:
		zc = cube([4,4,self.mount_thickness*2],center = True)
		cutouts = OpenSCADObject(name="union",params={})
		cutouts += translate([0,(self.plate_width - 20)/2,0])(zc)
		cutouts += translate([0,(self.plate_width - 20)/-2,0])(zc)
		return cutouts

	def plate(self) -> OpenSCADObject:
		p = cube([self.plate_length,self.plate_width,self.mount_thickness],center = True)
		fan_cutout = cube([self.fan_gap_length,self.fan_gap_width,self.mount_thickness*2], center = True)
		cutout = cube([self.board_length,self.board_width,self.mount_thickness],center = True)
		cutout = translate([0,0,1])(cutout)		
		p -= cutout
		p -= fan_cutout
		p -= self.ziptie_cutouts()
		return p

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	# e = ef.Fittings(35)
	# a = e.tube()
	m = mount()	
	# a = translate([0,64,-11])(a)
	a = m.plate()
	a -= m.ziptie_cutouts()
	# a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
