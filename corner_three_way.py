#! /usr/bin/env python3
from solid.objects import *
from solid.solidpython import *
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from euclid3 import Point2, Point3, Vector3

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

# ============
# = GEOMETRY =
# ============

# shell_thickness = 6
e_thickness = 20
tolerance = .3
gap_size = 3 - tolerance
inner_corner = e_thickness/2 + tolerance;
nub_length = 6 - tolerance

class ExtrusionCutouts:
	def __init__(self):
		pass

	def e_profile(self) -> List[Point3]:
		profile_pts = [[inner_corner,inner_corner,0],[inner_corner,gap_size,0],[inner_corner - nub_length, gap_size,0],
						[inner_corner - nub_length,0,0],[0,0,0]]
		return profile_pts

	def extrude_and_mirror_profile(self,e_profile,length,scale) -> OpenSCADObject:
		path = [[0,0,0],[0,0,length]]
		shape = e_profile
		extruded = extrude_along_path( shape_pts=shape, path_pts=path, scales = [1,scale])
		extruded += mirror(v=(0,1))(extruded)
		extruded += mirror(v=(1,1))(extruded)
		extruded += mirror(v=(1,-1))(extruded)
		return extruded

	def cutouts(self,length) -> OpenSCADObject:
		extrusion_offset = 10
		extrusion_profile = self.extrude_and_mirror_profile(self.e_profile(),length+extrusion_offset,1)
		extrusion_profile = translate([0,-extrusion_offset,0])(rotate(-90, v=RIGHT_VEC)(extrusion_profile))
		return extrusion_profile

class Slots:
	def __init__(self,ends):
		self.ends = ends 

	def hammer_nut_hole(self) -> OpenSCADObject:
		inset_length = 12
		extrusion_size = 20 + tolerance
		hes = extrusion_size/2
		hammer_nut_pts = [[0,0,0],[hes,hes,0],[hes,-hes,0]]
		hammer_nut_path = [[0,-10,0],[0,inset_length,0]]
		hammer_nut_hole = extrude_along_path(shape_pts=hammer_nut_pts, path_pts=hammer_nut_path)
		hammer_nut_hole = rotate(-90, v=FORWARD_VEC)(hammer_nut_hole)
		shape = hammer_nut_hole
		return shape

	def head_slot(self) -> OpenSCADObject:
		head_height = 14
		head_diameter = 7.75
		cyl_sides = 32
		inset_length = 12
		head_hole = translate([0,0,head_height])(cylinder(r = head_diameter/2, h = 4, segments = cyl_sides))
		head_slot = translate([head_diameter/-2,-inset_length,head_height+1])(cube([head_diameter,inset_length,4]))
		shape = head_hole
		shape += head_slot
		return shape

	def screw_slot(self) -> OpenSCADObject:
		screw_diameter = 4
		screw_height = 19
		cyl_sides = 16
		inset_length = 12
		screw_hole = cylinder(r = screw_diameter/2, h = screw_height, segments = cyl_sides) 
		screw_slot = translate([screw_diameter/-2,-inset_length,0])(cube([screw_diameter,inset_length,screw_height]))
		shape = screw_hole
		shape +=  screw_slot
		return shape

	def slot(self) -> OpenSCADObject:
		return self.head_slot() + self.screw_slot() + self.hammer_nut_hole()

	def screw_slots(self,sides = []) -> OpenSCADObject:
		screw_slots = OpenSCADObject()
		screw_slots = slot()
		screw_slots+= rotate(90,v=FORWARD_VEC)(slot())
		screw_slots+= rotate(180,v=FORWARD_VEC)(slot())
		screw_slots+= rotate(270,v=FORWARD_VEC)(slot())
		return screw_slots

	def cutouts(self,length) -> OpenSCADObject:
		cutouts = OpenSCADObject(name="union",params={})
		if self.ends[0]:
			cutouts += rotate(180,v=FORWARD_VEC)(self.slot())
		if self.ends[1]:
			cutouts += rotate(90,v=FORWARD_VEC)(self.slot())
		if self.ends[2]:
			cutouts += self.slot()
		if self.ends[3]:
			cutouts += rotate(270,v=FORWARD_VEC)(self.slot())
		if self.ends[4]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(180,v=FORWARD_VEC)(self.slot()) )))
		if self.ends[5]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(90,v=FORWARD_VEC)(self.slot()) )))
		if self.ends[6]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))((self.slot())))
		if self.ends[7]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(270,v=FORWARD_VEC)(self.slot()) )))
		return cutouts

class EndCutouts:
	def __init__(self,blind_ends = [0,0]):
		self.blind_ends = blind_ends

	def pyramid(self,size = 15) -> OpenSCADObject:
		base_pts = [[size,size,0],[-size,size,0],[-size,-size,0],[size,-size,0]]
		path_pts = [[0,0,0],[0,0,size]]
		pyramid =  extrude_along_path(shape_pts = base_pts, path_pts = path_pts, scales = [1,0])
		pyramid = rotate(-90,v=RIGHT_VEC)(pyramid())
		pyramid = translate([0,-10,0])(pyramid)
		return pyramid

	def cutouts(self,length) -> OpenSCADObject:
		cutouts = OpenSCADObject(name="union",params={})
		if self.blind_ends[0]:
			cutouts += self.pyramid(15)
		if self.blind_ends[1]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( self.pyramid(15) )))
		return cutouts 


class Cutout:
	instances = []
	def __init__(self,start_pt = [-60,0,0],end_pt = [60,0,0],ends = [1,1,1,1,0,0,0,0],blind_ends = [0,0]):
		self.start_pt = start_pt
		self.end_pt = end_pt
		self.ends = ends
		self.blind_ends = blind_ends
		Cutout.instances.append(self)

	def cutouts(self,length = 100) -> OpenSCADObject:
		cutouts = EndCutouts(self.blind_ends).cutouts(length)
		cutouts += ExtrusionCutouts().cutouts(length)
		cutouts += Slots(self.ends).cutouts(length)

		cutouts = rotate(90,v=UP_VEC)(cutouts)
		return cutouts

	def cutout_pos(self) -> OpenSCADObject:
		offset = 10
		if type(self.start_pt) == list:
			self.start_pt = np.array(self.start_pt)
		if type(self.end_pt) == list:
			self.end_pt = np.array(self.end_pt)
		norm_v = self.end_pt - self.start_pt
		length = np.linalg.norm(norm_v)
		cube_shell = (self.cutouts(length = length - offset))
		cube_shell = rotate(-90,BACK_VEC)(cube_shell)
		cube_shell = translate([0,0,offset])(cube_shell)
		x = norm_v[0]
		y = norm_v[1]
		z = norm_v[2]
		b = np.degrees(np.arccos(z/length))
		c = np.degrees(np.arctan2(y,x))
		cube_shell = rotate([0,b,c])(cube_shell)

		x = self.start_pt[0]
		y = self.start_pt[1]
		z = self.start_pt[2]
		cube_shell = translate([x,y,z])(cube_shell)

		return cube_shell

	def union_all_cutouts() -> OpenSCADObject:
		all_cutouts = OpenSCADObject(name="union",params={})
		for i in Cutout.instances:
			all_cutouts += i.cutout_pos()
		return all_cutouts


class Shell:
	instances = []
	def __init__(self,start_pt,end_pt,shell_thickness = 6):
		self.start_pt = start_pt
		self.end_pt = end_pt
		self.shell_thickness = shell_thickness
		Shell.instances.append(self)

	def make_shell(self,length) -> OpenSCADObject:
		total = (e_thickness/2 + self.shell_thickness)*2
		return cube([total, total, length], center=True)

	def shell_pos(self) -> OpenSCADObject:
		cube_shell = reposition(self.start_pt,self.end_pt,self.make_shell)
		return cube_shell

	def union_all_shells() -> OpenSCADObject:
		all_shells = OpenSCADObject(name="union",params={})
		for i in Shell.instances:
			all_shells += i.shell_pos()
		return all_shells


class Gusset:
	instances = []
	def __init__(self,start_pt_one,end_pt_one,start_pt_two,end_pt_two,thickness= 10):
		self.start_pt_one = start_pt_one
		self.end_pt_one = end_pt_one
		self.start_pt_two = start_pt_two
		self.end_pt_two = end_pt_two
		self.thickness = thickness
		Gusset.instances.append(self)

	def make_stick_one(self,length) -> OpenSCADObject:
		length_one = get_length(self.start_pt_one,self.end_pt_one)
		stick_one = cube([self.thickness,self.thickness,length_one],center=True)
		return stick_one

	def make_stick_two(self,length) -> OpenSCADObject:
		length_two = get_length(self.start_pt_two,self.end_pt_two)
		stick_two = cube([self.thickness,self.thickness,length_two],center=True)
		return stick_two

	def gusset_sticks(self) -> OpenSCADObject:
		stick_one = reposition(self.start_pt_one,self.end_pt_one,self.make_stick_one)
		stick_two = reposition(self.start_pt_two,self.end_pt_two,self.make_stick_two)
		return stick_one + stick_two

	def hull_gusset(self) -> OpenSCADObject:
		gusset = hull()(self.gusset_sticks())
		return gusset

	def union_all_gussets() -> OpenSCADObject:
		all_gussets = OpenSCADObject(name="union",params={})
		for i in Gusset.instances:
			all_gussets += i.hull_gusset()
		return all_gussets

def bisect_floor(input) -> OpenSCADObject:
	size = 300
	floor = translate([0,0,-150])(cube([300,300,300],center = True))
	return input - floor

def get_length(first_pt,second_pt):
	if type(first_pt) == list:
		first_pt = np.array(first_pt)
	if type(second_pt) == list:
		second_pt = np.array(second_pt)
	norm_v = second_pt - first_pt
	return np.linalg.norm(norm_v)

def reposition(first_pt,second_pt,func) -> OpenSCADObject:
	if type(first_pt) == list:
		first_pt = np.array(first_pt)
	if type(second_pt) == list:
		second_pt = np.array(second_pt)
	norm_v = second_pt - first_pt
	length = np.linalg.norm(norm_v)
	cube_shell = func(length)
	cube_shell = translate([0,0,length/2])(cube_shell)
	x = norm_v[0]
	y = norm_v[1]
	z = norm_v[2]
	b = np.degrees(np.arccos(z/length))
	c = np.degrees(np.arctan2(y,x))
	cube_shell = rotate([0,b,c])(cube_shell)

	x = first_pt[0]
	y = first_pt[1]
	z = first_pt[2]
	cube_shell = translate([x,y,z])(cube_shell)
	return cube_shell

def balance_on_corner_and_cutoff(a) -> OpenSCADObject:
	a = rotate(a = 45, v=(1,0,0))(a) 
	a = rotate(a = -35.26, v=(0,1,0))(a)
	a = bisect_floor(a)
	return a

def corner_three_way() -> OpenSCADObject:
	points = [[60,0,0],[-60,0,0]],[[0,14,0],[0,60,0]],[[0,0,60],[0,0,14]]
	center = [0,0,0]

	shell1 = Shell(points[0][0],points[0][1]) 
	shell2 = Shell(points[1][0],points[1][1])
	shell3 = Shell(points[2][0],points[2][1]) 
	cutout1 = Cutout(points[0][0],points[0][1],[0,1,1,0,0,0,0,0],[1,0])
	cutout2 = Cutout(points[1][0],points[1][1],[0,0,0,0,1,1,0,0],[0,1])
	cutout3 = Cutout(points[2][0],points[2][1],[0,0,1,1,0,0,0,0],[1,0])

	gusset1 = Gusset(points[1][0],points[1][1],points[2][0],points[2][1])
	gusset2 = Gusset(points[1][0],points[1][1],center,points[0][0])
	gusset3 = Gusset(points[2][0],points[2][1],center,points[0][0])

	a = merge_everything()

	return a

def cross() -> OpenSCADObject:
	points = [[[-60,0,0],[60,0,0]],[[0,-60,0],[0,60,0]]]
	shell1 = Shell(points[0][0],points[0][1]) 
	shell2 = Shell(points[1][0],points[1][1])
	cutout1 = Cutout(points[0][0],points[0][1],[0,0,0,0,1,1,1,1],[1,1])
	cutout2 = Cutout(points[1][0],points[1][1],[0,0,0,0,1,1,1,1],[1,1])
	gusset1 = Gusset(points[0][0],points[0][1],points[1][0],points[1][1])

	a = merge_everything()
	return a

def offset_cross() -> OpenSCADObject:
	points = [[[-60,0,30],[60,0,30]],[[0,-60,0],[0,60,0]]]
	shell1 = Shell(points[0][0],points[0][1]) 
	shell2 = Shell(points[1][0],points[1][1])
	cutout1 = Cutout(points[0][0],points[0][1],[0,0,0,0,1,1,1,1],[1,1])
	cutout2 = Cutout(points[1][0],points[1][1],[0,0,0,0,1,1,1,1],[1,1])
	gusset1 = Gusset(points[0][0],points[0][1],points[1][0],points[1][1])

	a = merge_everything()
	return a


def merge_everything() -> OpenSCADObject:
	a = Shell.union_all_shells()
	a += Gusset.union_all_gussets()
	a -= Cutout.union_all_cutouts()
	return a

if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	a = corner_three_way()
	# a = cross()
	# a = offset_cross()
	a = balance_on_corner_and_cutoff(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
