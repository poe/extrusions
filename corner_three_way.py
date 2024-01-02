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
outer_corner = inner_corner + shell_thickness
nub_length = 6 - tolerance

def e_profile() -> List[Point3]:
	profile_pts = [[inner_corner,inner_corner,0],[inner_corner,gap_size,0],[inner_corner - nub_length, gap_size,0],
					[inner_corner - nub_length,0,0],[0,0,0]]

	return profile_pts

def extrude_and_mirror_profile(e_profile,length,scale) -> OpenSCADObject:
	path = [[0,0,0],[0,0,length]]
	shape = e_profile
	extruded = extrude_along_path( shape_pts=shape, path_pts=path, scales = [1,scale])
	extruded += mirror(v=(0,1))(extruded)
	extruded += mirror(v=(1,1))(extruded)
	extruded += mirror(v=(1,-1))(extruded)
	return extruded

def make_three_e(extrusion_profile) -> OpenSCADObject:
	three_extrusions = translate([0,0,10+shell_thickness])(extrusion_profile)
	three_extrusions += translate([10+shell_thickness,0,0])(rotate(a=90, v=FORWARD_VEC)(extrusion_profile))
	three_extrusions += translate(([0,50,0]))(rotate(a=90, v=RIGHT_VEC)(extrusion_profile))
	return three_extrusions

def bisect_floor(input) -> OpenSCADObject:
	size = 300
	floor = translate([0,0,-150])(cube([300,300,300],center = True))
	return input - floor

def hammer_nut_hole() -> OpenSCADObject:
	inset_length = 12
	extrusion_size = 20 + tolerance
	hes = extrusion_size/2
	hammer_nut_pts = [[0,0,0],[hes,hes,0],[hes,-hes,0]]
	hammer_nut_path = [[0,-10,0],[0,inset_length,0]]
	hammer_nut_hole = extrude_along_path(shape_pts=hammer_nut_pts, path_pts=hammer_nut_path)
	hammer_nut_hole = rotate(-90, v=FORWARD_VEC)(hammer_nut_hole)
	shape = hammer_nut_hole
	return shape

def head_slot() -> OpenSCADObject:
	head_height = 14
	head_diameter = 7.75
	cyl_sides = 32
	inset_length = 12
	head_hole = translate([0,0,head_height])(cylinder(r = head_diameter/2, h = 4, segments = cyl_sides))
	head_slot = translate([head_diameter/-2,-inset_length,head_height+1])(cube([head_diameter,inset_length,4]))
	shape = head_hole
	shape += head_slot
	return shape

def screw_slot() -> OpenSCADObject:
	screw_diameter = 4
	screw_height = 19
	cyl_sides = 16
	inset_length = 12
	screw_hole = cylinder(r = screw_diameter/2, h = screw_height, segments = cyl_sides) 
	screw_slot = translate([screw_diameter/-2,-inset_length,0])(cube([screw_diameter,inset_length,screw_height]))
	shape = screw_hole
	shape +=  screw_slot
	return shape

def slot() -> OpenSCADObject:
	return head_slot() + screw_slot() + hammer_nut_hole()

def screw_slots(sides = []) -> OpenSCADObject:
	screw_slots = OpenSCADObject()
	screw_slots = slot()
	screw_slots+= rotate(90,v=FORWARD_VEC)(slot())
	screw_slots+= rotate(180,v=FORWARD_VEC)(slot())
	screw_slots+= rotate(270,v=FORWARD_VEC)(slot())
	return screw_slots

def pyramid(size = 15) -> OpenSCADObject:
	base_pts = [[size,size,0],[-size,size,0],[-size,-size,0],[size,-size,0]]
	path_pts = [[0,0,0],[0,0,size]]
	pyramid =  extrude_along_path(shape_pts = base_pts, path_pts = path_pts, scales = [1,0])
	pyramid = rotate(-90,v=RIGHT_VEC)(pyramid())
	pyramid = translate([0,-10,0])(pyramid)
	return pyramid

def star_profile() -> List[Point3]:
	corner = inner_corner
	profile_pts = [[corner,corner,0],[corner,gap_size,0],
					[corner - nub_length,0,0],[0,0,0]]

	return profile_pts

def star_spike() -> OpenSCADObject:
	spike = extrude_and_mirror_profile(star_profile(),20,0)
	spike = rotate(-90,v=RIGHT_VEC)(spike())
	spike = translate([0,11.9,0])(spike)
	return spike

def cutouts(ends = [1,1,1,1,1,1,1,1],length = 100) -> OpenSCADObject:
	extrusion_offset = 10
	extrusion_profile = extrude_and_mirror_profile(e_profile(),length+extrusion_offset,1)
	extrusion_profile = translate([0,-extrusion_offset,0])(rotate(-90, v=RIGHT_VEC)(extrusion_profile))

	cutouts = pyramid(15) + star_spike()
	cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( pyramid(15) + star_spike() )))  
	
	if ends[0]:
		cutouts += rotate(180,v=FORWARD_VEC)(slot())
	if ends[1]:
		cutouts += rotate(90,v=FORWARD_VEC)(slot())
	if ends[2]:
		cutouts += slot()
	if ends[3]:
		cutouts += rotate(270,v=FORWARD_VEC)(slot())
	if ends[4]:
		cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(180,v=FORWARD_VEC)(slot()) )))
	if ends[5]:
		cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(90,v=FORWARD_VEC)(slot()) )))
	if ends[6]:
		cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))((slot())))
	if ends[7]:
		cutouts += translate([0,length-9,0])(rotate(180,v=(1,0,0))(( rotate(270,v=FORWARD_VEC)(slot()) )))
	cutouts += extrusion_profile
	cutouts = rotate(90,v=UP_VEC)(cutouts)
	return cutouts

def shell_pos(first_pt = np.array([10,10,10]),second_pt = np.array([100,100,100])) -> OpenSCADObject:
	if type(first_pt) == list:
		first_pt = np.array(first_pt)
	if type(second_pt) == list:
		second_pt = np.array(second_pt)
	norm_v = second_pt - first_pt
	length = np.linalg.norm(norm_v)
	total = (e_thickness/2 + shell_thickness)*2
	cube_shell = (cube([total, total, length], center=True))
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

def cutout_pos(first_pt = np.array([10,10,10]),second_pt = np.array([100,100,100]),ends = [1,1,1,1,1,1,1,1]) -> OpenSCADObject:
	offset = 10
	if type(first_pt) == list:
		first_pt = np.array(first_pt)
	if type(second_pt) == list:
		second_pt = np.array(second_pt)
	norm_v = second_pt - first_pt
	length = np.linalg.norm(norm_v)
	cube_shell = (cutouts(ends=ends,length = length - offset))
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

def balance_on_corner_and_cutoff(a) -> OpenSCADObject:
	a = rotate(a = 45, v=(1,0,0))(a) 
	a = rotate(a = -35.26, v=(0,1,0))(a)
	a = bisect_floor(a)
	return a

if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

#	gusset_pts = [[0,0,0],[60,0,0]]

	# tt = shell_thickness + e_thickness/2 
	# shell = shell_pos([60,0,0],[-60,0,0])
	# shell += shell_pos([0,0,0],[0,60,0])
	# shell += shell_pos([0,0,60],[0,0,0])
	# cutout = cutout_pos([60,0,0],[-60,0,0],[0,1,1,0,0,0,0,0])
	# cutout += cutout_pos([0,60,0],[0,tt,0],[0,0,1,1,0,0,0,0])
	# cutout += cutout_pos([0,0,60],[0,0,tt],[0,0,1,1,0,0,0,0])
	# a = shell - cutout

	tt = shell_thickness + e_thickness/2 
	shell = shell_pos([60,0,0],[-60,0,0])
	shell += shell_pos([60,0,0],[-60,60,0])
	cutout = cutout_pos([60,0,0],[-60,0,0],[0,1,1,0,0,0,0,0])
	cutout += cutout_pos([0,60,0],[0,60,0],[0,0,1,1,0,0,0,0])
	a = shell - cutout

#	a = balance_on_corner_and_cutoff(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
