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

# ============
# = GEOMETRY =
# ============

tube_length = 200
shell_thickness = 5
e_thickness = 20

def e_profile() -> List[Point3]:
	profile_pts = []

	tolerance = .15;
	inner_corner = e_thickness/2 + tolerance;
	outer_corner = inner_corner + shell_thickness
	nub_length = 6 - tolerance;
	rail_thickness = .5;
	gap_size = 3 - tolerance;

	# outer shell
	# profile_pts = [[inner_corner,inner_corner,0],[inner_corner,gap_size,0],
    #                  [inner_corner - nub_length, gap_size,0],[inner_corner - nub_length, 0,0],
    #                  [outer_corner,0,0],[outer_corner,outer_corner,0]]

	profile_pts = [[inner_corner,inner_corner,0],[inner_corner,gap_size,0],[inner_corner - nub_length, gap_size,0],
					[inner_corner - nub_length,0,0],[0,0,0]]

	return profile_pts

def extrude_and_mirror_profile() -> OpenSCADObject:
	path = [[0,0,0],[0,0,tube_length]]
	shape = e_profile()
	extruded = extrude_along_path( shape_pts=shape, path_pts=path)
	extruded += mirror(v=(0,1))(extruded)
	extruded += mirror(v=(1,1))(extruded)
	extruded += mirror(v=(1,-1))(extruded)
	return extruded

def make_three_e(extrusion_profile) -> OpenSCADObject:
	three_extrusions = translate([0,0,10+shell_thickness])(extrusion_profile)
	three_extrusions += translate([10+shell_thickness,0,0])(rotate(a=90, v=FORWARD_VEC)(extrusion_profile))
	three_extrusions += translate(([0,tube_length/2,0]))(rotate(a=90, v=RIGHT_VEC)(extrusion_profile))
	return three_extrusions

def make_shell() -> OpenSCADObject:
	total = (e_thickness/2 + shell_thickness)*2
	base_cube = cube([total, total, total], center=True)
	cube_shell = translate([total,0,0])(base_cube) + base_cube
	cube_shell += translate([0,total,0])(base_cube) + base_cube
	cube_shell += translate([0,0,total])(base_cube) + base_cube	
	return cube_shell

def bisect_floor(input) -> OpenSCADObject:
	size = 300
	floor = translate([0,0,-150])(cube([300,300,300],center = True))
	return input - floor
# ===============
# = ENTRY POINT =
# ===============
if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	extrusion_profile = extrude_and_mirror_profile()
	shell = make_shell()
	a = (shell - make_three_e(extrusion_profile()))
	a = rotate(a = -45, v=(0,1,0))(a)
	a = rotate(a = 35.26, v=(1,0,0))(a)
	a = bisect_floor(a)
	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
