#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

class HoldingBlock:
	def __init__(self,b_thickness = 7.5,i_diameter = 8,o_diameter=22,cyl_sides = 32,tolerance = .1):
		self.radius = i_diameter/2 - tolerance
		self.b_thickness = b_thickness
		self.o_diameter = o_diameter
		self.cyl_sides = cyl_sides

	def peg(self) -> OpenSCADObject:
		peg = cylinder(r=self.radius, h=self.b_thickness*2, segments = self.cyl_sides, center=True)
		nub = cube([1,1,1],center=True)
		nub = rotate(a = 45, v=(0,1,0))(nub)
		nub = translate([self.radius,0,self.b_thickness])(nub)
		nubs = nub
		nubs += rotate(a = 90, v=(0,0,1))(nub)		
		nubs += rotate(a = 180, v=(0,0,1))(nub)		
		nubs += rotate(a = 270, v=(0,0,1))(nub)		
		slot = cube([3,3,3],center=True) - cube([1,1,5],center=True)
		slot = translate([self.radius,0,self.b_thickness])(slot)
		slots = slot
		slots += rotate(a = 90, v=(0,0,1))(slot)		
		slots += rotate(a = 180, v=(0,0,1))(slot)		
		slots += rotate(a = 270, v=(0,0,1))(slot)		

		return peg + nubs - slots

	def diagonal_block(self) -> OpenSCADObject:
		upper_peg = self.peg()
		upper_peg = translate([0,0,self.o_diameter/2])(upper_peg)
		lower_peg = self.peg()
		lower_peg = rotate(a = 270, v=(1,0,0))(lower_peg)
		lower_peg = translate([0,self.o_diameter/2,0])(lower_peg)
		block = cube([self.o_diameter/2,self.o_diameter,self.o_diameter], center = True)
		block = rotate(a = 45, v=(1,0,0))(block)
		block *= cube([self.o_diameter/2,self.o_diameter,self.o_diameter], center = True)
		block += lower_peg + upper_peg + block
		block = rotate(a = 45, v=(1,0,0))(block)
		block = translate([0,0,1])(block)
		return block 

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor

if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	h = HoldingBlock()
	a = h.diagonal_block()
	a = h.bisect_floor(a)
	f = ef.Fittings(35)
	a = translate([0,0,15])(a)
	a += rotate(a=90,v=(0,0,1))(f.tube())	
	# a = rotate(a=15,v=(1,0,0))(a)
	a = translate([0,0,-11])(a)
	a = h.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
