#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

#from solid import *
#from solid.utils import *

from solid2 import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

from solid2.extensions.bosl2 import gears, cube, sphere, xcyl, union, xcopies, \
                                    attachable, show_anchors, \
                                    CENTER, LEFT, TOP, UP

class disk():
	def __init__(self,diameter = 200, cyl_sides = 128, thickness = 12):
		self.diameter = diameter
		self.radius = diameter/2
		self.thickness = thickness
		self.cyl_sides = cyl_sides

	def outer_disk(self):
		oc = cylinder(r = self.radius,h=1,center = True, _fn = 256)
		uc = cylinder(r = self.radius - self.thickness/2,h=1,center = True, _fn = self.cyl_sides)
		uc = translate([0,0,self.thickness/2])(uc)
		lc = cylinder(r = self.radius - self.thickness/2,h=1,center = True, _fn = self.cyl_sides)
		lc = translate([0,0,-self.thickness/2])(lc)
		fc = hull()(oc+uc+lc)
		ic = cylinder(r = self.diameter/4, h = self.thickness*5,center = True, _fn = self.cyl_sides)
		d_gear = self.gear_ring()
		fc += d_gear
		return fc - ic
		
	def gear_ring(self):
		top_gear = gears.spur_gear(pitch=8, teeth=70, thickness=5, helical=30, slices=5, pressure_angle=20)
		bottom_gear = gears.spur_gear(pitch=8, teeth=70, thickness=5, helical=30, slices=5, pressure_angle=20)
		bottom_gear = mirrorZ()(bottom_gear)
		bottom_gear = translate([0,0,5])(bottom_gear)
		d_gears = top_gear + bottom_gear
		d_gears = translate([0,0,9])(d_gears)
		return d_gears

	def drive_ring(self):
		top_gear = gears.spur_gear(pitch=8, teeth=29, thickness=5, helical=30, slices=5, pressure_angle=20)
		bottom_gear = gears.spur_gear(pitch=8, teeth=29, thickness=5, helical=30, slices=5, pressure_angle=20)
		bottom_gear = mirrorZ()(bottom_gear)
		bottom_gear = translate([0,0,5])(bottom_gear)
		d_gears = top_gear + bottom_gear
		d_gears = translate([0,0,-4])(d_gears)
		# ic = cylinder(r = 30, h = self.thickness*5,center = True, _fn = self.cyl_sides)
		return d_gears

	def motor_connector(self):
		mount = cylinder(r = 12.5,h=14,center = True, _fn = 256)
		shaft = cylinder(r = 2.75,h=30,center = True, _fn = 256)		
		set_screw = cylinder(r = 2,h=16,center = True, _fn = 256)
		set_screw = rotate(a=90,v=[1,0,0])(set_screw)
		set_screw = rotate(a=90,v=[0,0,1])(set_screw)
		set_screw = translate([8,0,0])(set_screw)
		flat = cube([6,6,40],center = True)
		flat = translate(5.2,0,0)(flat)
		shaft = shaft - flat
		mount = mount - shaft
		mount = mount - set_screw
		mount = translate([0,0,8])(mount)
		return mount

	def drive_ring_cutoff(self):
		drc = cube([80,80,self.thickness],center=True)
		drc = translate([0,0,self.thickness-4])(drc)
		return drc

if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(25)
	d = disk()
	# post = e.tube()
	# a = d.outer_disk()
	# post = rotate(a=90,v=[0,1,0])(post)
	# post = translate([68,0,20])(post)
	# posts = post
	# posts += rotate(a=90,v=[0,0,1])(post)
	# posts += rotate(a=180,v=[0,0,1])(post)
	# posts += rotate(a=270,v=[0,0,1])(post)
	# a += posts
	# a = d.outer_disk()
	a = d.drive_ring()
	a -= d.drive_ring_cutoff()
	a += d.motor_connector()

	file_out = scad_render_to_file(a,  out_dir=out_dir)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
