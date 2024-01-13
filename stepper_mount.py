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
	def __init__(self,stepper_size = 42.3,screw_dist = 31,screw_dia = 3.5,motor_thickness = 23.5, bump_dia = 22, mount_thick = 6):
		self.stepper_size = stepper_size
		self.screw_dist = screw_dist
		self.screw_dia = screw_dia
		self.motor_thickness = motor_thickness
		self.bump_dia = bump_dia
		self.total_size = stepper_size + mount_thick*2
		self.total_thick = motor_thickness + mount_thick*2

	def screws(self) -> OpenSCADObject:
		screw = cylinder(r=self.screw_dia/2, h=20, segments = 32, center=True)
		screw = translate([self.screw_dist/2,self.screw_dist/2,self.motor_thickness/2])(screw)
		screw += rotate(a=90,v=(0,0,1))(screw)
		screw += rotate(a=180,v=(0,0,1))(screw)
		screw += rotate(a=270,v=(0,0,1))(screw)
		return screw

	def bump(self) -> OpenSCADObject:
		bump = cylinder(r = self.bump_dia/2,h=6,segments = 32,center=True)
		slot = cube([self.bump_dia,self.bump_dia,6],center=True)
		slot = translate([self.bump_dia/2,0,0])(slot)
		bump += slot
		bump = translate([0,0,self.motor_thickness/2])(bump)
		return bump

	def shaft(self) -> OpenSCADObject:
		shaft = cylinder(r = 3,h=20,segments=32,center=True)
		slot = cube([self.total_size/2,6,20],center=True)
		slot = translate([self.total_size/4,0,-4])(slot)
		shaft += slot
		shaft = translate([0,0,self.motor_thickness])(shaft)
		return shaft

	def motor_cutout(self) -> OpenSCADObject:
		mc = cube([self.stepper_size,self.stepper_size,self.motor_thickness], center=True)
		mc += self.screws()
		mc += self.bump()
		mc += self.shaft()
		return mc

	def motor_mount(self) -> OpenSCADObject:
		mm = cube([self.total_size,self.total_size,self.total_thick], center=True)
		mm -= self.motor_cutout()
		return mm

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(35)
	m = mount()	
	a = m.motor_mount()
	t = e.tube()
	t = rotate(a = 90,v = (0,1,0))(t)
	t = translate([-39,0,-18])(t)
	a += t
	a = rotate(a = 25, v = (0,1,0))(a)
	a = translate([0,0,-4])(a)
	a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
