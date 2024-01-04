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


shell_thickness = 6
e_thickness = 20
tolerance = .3
gap_size = 3 - tolerance
inner_corner = e_thickness/2 + tolerance;
nub_length = 6 - tolerance

class Cutout:
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

	def make_three_e(self,extrusion_profile) -> OpenSCADObject:
		three_extrusions = translate([0,0,10+shell_thickness])(extrusion_profile)
		three_extrusions += translate([10+shell_thickness,0,0])(rotate(a=90, v=FORWARD_VEC)(extrusion_profile))
		three_extrusions += translate(([0,50,0]))(rotate(a=90, v=RIGHT_VEC)(extrusion_profile))
		return three_extrusions

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

	def pyramid(self,size = 15) -> OpenSCADObject:
		base_pts = [[size,size,0],[-size,size,0],[-size,-size,0],[size,-size,0]]
		path_pts = [[0,0,0],[0,0,size]]
		pyramid =  extrude_along_path(shape_pts = base_pts, path_pts = path_pts, scales = [1,0])
		pyramid = rotate(-90,v=RIGHT_VEC)(pyramid())
		pyramid = translate([0,-10,0])(pyramid)
		return pyramid

	def star_profile(self) -> List[Point3]:
		corner = inner_corner
		profile_pts = [[corner,corner,0],[corner,gap_size,0],
						[corner - nub_length,0,0],[0,0,0]]

		return profile_pts

	def star_spike(self) -> OpenSCADObject:
		spike = self.extrude_and_mirror_profile(self.star_profile(),20,0)
		spike = rotate(-90,v=RIGHT_VEC)(spike())
		spike = translate([0,11.9,0])(spike)
		return spike

	def cutouts(self,ends = [1,1,1,1,1,1,1,1],length = 100) -> OpenSCADObject:
		extrusion_offset = 10
		extrusion_profile = self.extrude_and_mirror_profile(self.e_profile(),length+extrusion_offset,1)
		extrusion_profile = translate([0,-extrusion_offset,0])(rotate(-90, v=RIGHT_VEC)(extrusion_profile))

		cutouts = self.pyramid(15) + self.star_spike()
		cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( self.pyramid(15) + self.star_spike() )))  
		
		if ends[0]:
			cutouts += rotate(180,v=FORWARD_VEC)(self.slot())
		if ends[1]:
			cutouts += rotate(90,v=FORWARD_VEC)(self.slot())
		if ends[2]:
			cutouts += self.slot()
		if ends[3]:
			cutouts += rotate(270,v=FORWARD_VEC)(self.slot())
		if ends[4]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(180,v=FORWARD_VEC)(self.slot()) )))
		if ends[5]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(90,v=FORWARD_VEC)(self.slot()) )))
		if ends[6]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))((self.slot())))
		if ends[7]:
			cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(270,v=FORWARD_VEC)(self.slot()) )))
		cutouts += extrusion_profile
		cutouts = rotate(90,v=UP_VEC)(cutouts)
		return cutouts

	def cutout_pos(self,first_pt = np.array([10,10,10]),second_pt = np.array([100,100,100]),ends = [1,1,1,1,1,1,1,1]) -> OpenSCADObject:
		offset = 10
		if type(first_pt) == list:
			first_pt = np.array(first_pt)
		if type(second_pt) == list:
			second_pt = np.array(second_pt)
		norm_v = second_pt - first_pt
		length = np.linalg.norm(norm_v)
		cube_shell = (self.cutouts(ends=ends,length = length - offset))
		cube_shell = rotate(-90,BACK_VEC)(cube_shell)
		cube_shell = translate([0,0,offset])(cube_shell)
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

class Shell:
	instances = []
	def __init__(self,start_pt,end_pt):
		self.start_pt = start_pt
		self.end_pt = end_pt
		Shell.instances.append(self)

	def make_shell(self,length) -> OpenSCADObject:
		total = (e_thickness/2 + shell_thickness)*2
		return cube([total, total, length], center=True)

	def shell_pos(self) -> OpenSCADObject:
		cube_shell = reposition(self.start_pt,self.end_pt,self.make_shell)
		return cube_shell

	def union_all_shells() -> OpenSCADObject:
		all_shells = OpenSCADObject(name="union",params={})
		for i in Shell.instances:
			all_shells += i.shell_pos()
			print(i)
			print(i.shell_pos())
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

if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	points = [[60,0,0],[-60,0,0]],[[0,0,0],[0,60,0]],[[0,0,60],[0,0,0]]
	center = [0,0,0]

	tt = shell_thickness + e_thickness/2
	shell1 = Shell(points[0][0],points[0][1]) 
	shell2 = Shell(points[1][0],points[1][1]) 
	shell3 = Shell(points[2][0],points[2][1]) 
	cutout1 = Cutout()
	cutout2 = Cutout()
	cutout3 = Cutout()
	cutout = cutout1.cutout_pos(points[0][0],points[0][1],[0,1,1,0,0,0,0,0])
	cutout += cutout2.cutout_pos(points[1][0],points[1][1],[0,0,0,0,1,1,0,0])
	cutout += cutout3.cutout_pos(points[2][0],points[2][1],[0,0,1,1,0,0,0,0])
	gusset1 = Gusset(points[1][0],points[1][1],points[2][0],points[2][1])
	gusset2 = Gusset(points[1][0],points[1][1],center,points[0][0])
	gusset3 = Gusset(points[2][0],points[2][1],center,points[0][0])

	a = Shell.union_all_shells()
	a += Gusset.union_all_gussets()
	a -= cutout

	# a = Gusset.union_all_gussets()

	a = balance_on_corner_and_cutoff(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
