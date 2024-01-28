// Generated by SolidPython 1.1.3 on 2024-01-15 18:45:57


difference() {
	translate(v = [0, 0, 2]) {
		rotate(a = 15, v = [0, 1, 0]) {
			union() {
				difference() {
					translate(v = [0, 20.0000000000, 0]) {
						cube(center = true, size = [40, 80, 2]);
					}
					translate(v = [0, 50, 0]) {
						cylinder($fn = 32, center = true, h = 20, r = 3.2000000000);
					}
				}
				union() {
					translate(v = [-53, 0, -10]) {
						rotate(a = 90, v = [0, 1, 0]) {
							difference() {
								union() {
									union();
									translate(v = [-10, 0, 0]) {
										rotate(a = [0, 90.0, 0.0]) {
											translate(v = [0, 0, 10.0]) {
												cube(center = true, size = [32.0000000000, 32.0000000000, 20.0]);
											}
										}
									}
									union();
								}
								union() {
									union();
									translate(v = [-10, 0, 0]) {
										rotate(a = [0, 90.0, 0.0]) {
											translate(v = [0, 0, 10]) {
												rotate(a = -90, v = [0, -1, 0]) {
													rotate(a = 90, v = [0, 0, 1]) {
														union() {
															union();
															translate(v = [0, -10, 0]) {
																rotate(a = -90, v = [1, 0, 0]) {
																	polyhedron(convexity = 10, faces = [[0, 1, 4], [1, 5, 4], [1, 2, 5], [2, 6, 5], [2, 3, 6], [3, 7, 6], [3, 0, 7], [0, 4, 7], [3, 2, 1, 0], [4, 5, 6, 7]], points = [[-15.0000000000, 15.0000000000, 0.0000000000], [15.0000000000, 15.0000000000, 0.0000000000], [15.0000000000, -15.0000000000, 0.0000000000], [-15.0000000000, -15.0000000000, 0.0000000000], [0.0000000000, 0.0000000000, 15.0000000000], [0.0000000000, 0.0000000000, 15.0000000000], [0.0000000000, 0.0000000000, 15.0000000000], [0.0000000000, 0.0000000000, 15.0000000000]]);
																}
															}
															translate(v = [0, 1.0, 0]) {
																rotate(a = 180, v = [1, 0, 0]) {
																	translate(v = [0, -10, 0]) {
																		rotate(a = -90, v = [1, 0, 0]) {
																			polyhedron(convexity = 10, faces = [[0, 1, 4], [1, 5, 4], [1, 2, 5], [2, 6, 5], [2, 3, 6], [3, 7, 6], [3, 0, 7], [0, 4, 7], [3, 2, 1, 0], [4, 5, 6, 7]], points = [[-15.0000000000, 15.0000000000, 0.0000000000], [15.0000000000, 15.0000000000, 0.0000000000], [15.0000000000, -15.0000000000, 0.0000000000], [-15.0000000000, -15.0000000000, 0.0000000000], [0.0000000000, 0.0000000000, 15.0000000000], [0.0000000000, 0.0000000000, 15.0000000000], [0.0000000000, 0.0000000000, 15.0000000000], [0.0000000000, 0.0000000000, 15.0000000000]]);
																		}
																	}
																}
															}
															translate(v = [0, -10, 0]) {
																rotate(a = -90, v = [1, 0, 0]) {
																	union() {
																		polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 20.0], [-10.2, 2.8, 20.0], [-4.3999999999999995, 2.8, 20.0], [-4.3999999999999995, 0.0, 20.0], [0.0, 0.0, 20.0]]);
																		mirror(v = [0, 1]) {
																			polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 20.0], [-10.2, 2.8, 20.0], [-4.3999999999999995, 2.8, 20.0], [-4.3999999999999995, 0.0, 20.0], [0.0, 0.0, 20.0]]);
																		}
																		mirror(v = [1, 1]) {
																			union() {
																				polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 20.0], [-10.2, 2.8, 20.0], [-4.3999999999999995, 2.8, 20.0], [-4.3999999999999995, 0.0, 20.0], [0.0, 0.0, 20.0]]);
																				mirror(v = [0, 1]) {
																					polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 20.0], [-10.2, 2.8, 20.0], [-4.3999999999999995, 2.8, 20.0], [-4.3999999999999995, 0.0, 20.0], [0.0, 0.0, 20.0]]);
																				}
																			}
																		}
																		mirror(v = [1, -1]) {
																			union() {
																				polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 20.0], [-10.2, 2.8, 20.0], [-4.3999999999999995, 2.8, 20.0], [-4.3999999999999995, 0.0, 20.0], [0.0, 0.0, 20.0]]);
																				mirror(v = [0, 1]) {
																					polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 20.0], [-10.2, 2.8, 20.0], [-4.3999999999999995, 2.8, 20.0], [-4.3999999999999995, 0.0, 20.0], [0.0, 0.0, 20.0]]);
																				}
																				mirror(v = [1, 1]) {
																					union() {
																						polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 20.0], [-10.2, 2.8, 20.0], [-4.3999999999999995, 2.8, 20.0], [-4.3999999999999995, 0.0, 20.0], [0.0, 0.0, 20.0]]);
																						mirror(v = [0, 1]) {
																							polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 20.0], [-10.2, 2.8, 20.0], [-4.3999999999999995, 2.8, 20.0], [-4.3999999999999995, 0.0, 20.0], [0.0, 0.0, 20.0]]);
																						}
																					}
																				}
																			}
																		}
																	}
																}
															}
															union() {
																union();
																translate(v = [0, 1.0, 0]) {
																	rotate(a = 180, v = [1, 0, 0]) {
																		rotate(a = 180, v = [0, 1, 0]) {
																			union() {
																				translate(v = [0, 0, 14]) {
																					cylinder($fn = 32, h = 4, r = 3.8750000000);
																				}
																				translate(v = [-3.8750000000, -12, 15]) {
																					cube(size = [7.7500000000, 12, 4]);
																				}
																				union() {
																					cylinder($fn = 16, h = 19, r = 2.0000000000);
																					translate(v = [-2.0000000000, -12, 0]) {
																						cube(size = [4, 12, 19]);
																					}
																				}
																				rotate(a = -90, v = [0, 1, 0]) {
																					polyhedron(convexity = 10, faces = [[0, 1, 3], [1, 4, 3], [1, 2, 4], [2, 5, 4], [2, 0, 5], [0, 3, 5], [2, 1, 0], [3, 4, 5]], points = [[0.0000000000, -10.0000000000, 0.0000000000], [10.1000000000, -10.0000000000, 10.1000000000], [10.1000000000, -10.0000000000, -10.1000000000], [0.0000000000, 12.0000000000, 0.0000000000], [10.1000000000, 12.0000000000, 10.1000000000], [10.1000000000, 12.0000000000, -10.1000000000]]);
																				}
																			}
																		}
																	}
																}
																translate(v = [0, 1.0, 0]) {
																	rotate(a = 180, v = [1, 0, 0]) {
																		rotate(a = 90, v = [0, 1, 0]) {
																			union() {
																				translate(v = [0, 0, 14]) {
																					cylinder($fn = 32, h = 4, r = 3.8750000000);
																				}
																				translate(v = [-3.8750000000, -12, 15]) {
																					cube(size = [7.7500000000, 12, 4]);
																				}
																				union() {
																					cylinder($fn = 16, h = 19, r = 2.0000000000);
																					translate(v = [-2.0000000000, -12, 0]) {
																						cube(size = [4, 12, 19]);
																					}
																				}
																				rotate(a = -90, v = [0, 1, 0]) {
																					polyhedron(convexity = 10, faces = [[0, 1, 3], [1, 4, 3], [1, 2, 4], [2, 5, 4], [2, 0, 5], [0, 3, 5], [2, 1, 0], [3, 4, 5]], points = [[0.0000000000, -10.0000000000, 0.0000000000], [10.1000000000, -10.0000000000, 10.1000000000], [10.1000000000, -10.0000000000, -10.1000000000], [0.0000000000, 12.0000000000, 0.0000000000], [10.1000000000, 12.0000000000, 10.1000000000], [10.1000000000, 12.0000000000, -10.1000000000]]);
																				}
																			}
																		}
																	}
																}
																translate(v = [0, 1.0, 0]) {
																	rotate(a = 180, v = [1, 0, 0]) {
																		union() {
																			translate(v = [0, 0, 14]) {
																				cylinder($fn = 32, h = 4, r = 3.8750000000);
																			}
																			translate(v = [-3.8750000000, -12, 15]) {
																				cube(size = [7.7500000000, 12, 4]);
																			}
																			union() {
																				cylinder($fn = 16, h = 19, r = 2.0000000000);
																				translate(v = [-2.0000000000, -12, 0]) {
																					cube(size = [4, 12, 19]);
																				}
																			}
																			rotate(a = -90, v = [0, 1, 0]) {
																				polyhedron(convexity = 10, faces = [[0, 1, 3], [1, 4, 3], [1, 2, 4], [2, 5, 4], [2, 0, 5], [0, 3, 5], [2, 1, 0], [3, 4, 5]], points = [[0.0000000000, -10.0000000000, 0.0000000000], [10.1000000000, -10.0000000000, 10.1000000000], [10.1000000000, -10.0000000000, -10.1000000000], [0.0000000000, 12.0000000000, 0.0000000000], [10.1000000000, 12.0000000000, 10.1000000000], [10.1000000000, 12.0000000000, -10.1000000000]]);
																			}
																		}
																	}
																}
																translate(v = [0, 1.0, 0]) {
																	rotate(a = 180, v = [1, 0, 0]) {
																		rotate(a = 270, v = [0, 1, 0]) {
																			union() {
																				translate(v = [0, 0, 14]) {
																					cylinder($fn = 32, h = 4, r = 3.8750000000);
																				}
																				translate(v = [-3.8750000000, -12, 15]) {
																					cube(size = [7.7500000000, 12, 4]);
																				}
																				union() {
																					cylinder($fn = 16, h = 19, r = 2.0000000000);
																					translate(v = [-2.0000000000, -12, 0]) {
																						cube(size = [4, 12, 19]);
																					}
																				}
																				rotate(a = -90, v = [0, 1, 0]) {
																					polyhedron(convexity = 10, faces = [[0, 1, 3], [1, 4, 3], [1, 2, 4], [2, 5, 4], [2, 0, 5], [0, 3, 5], [2, 1, 0], [3, 4, 5]], points = [[0.0000000000, -10.0000000000, 0.0000000000], [10.1000000000, -10.0000000000, 10.1000000000], [10.1000000000, -10.0000000000, -10.1000000000], [0.0000000000, 12.0000000000, 0.0000000000], [10.1000000000, 12.0000000000, 10.1000000000], [10.1000000000, 12.0000000000, -10.1000000000]]);
																				}
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
					translate(v = [-28.0000000000, 0, 0]) {
						cube(center = true, size = [20, 40, 2]);
					}
				}
			}
		}
	}
	translate(v = [0, 0, -150]) {
		cube(center = true, size = [300, 300, 300]);
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
#! /usr/bin/env python3
import sys
from math import cos, radians, sin, pi, tau
from pathlib import Path

from solid import *
from solid.utils import *

from typing import Set, Sequence, List, Callable, Optional, Union, Iterable, Tuple

import numpy as np

import extrusion_fittings as ef

class CameraMount():
	def __init__(self,camera_size = 40,screw_dia = 6.4, mount_thick = 2):
		self.camera_size = camera_size
		self.screw_dia = screw_dia
		self.mount_thick = mount_thick

	def screws(self) -> OpenSCADObject:
		screw = cylinder(r=self.screw_dia/2, h=20, segments = 32, center=True)
		screw = translate([0,50,0])(screw)
		return screw

	def camera_mount(self) -> OpenSCADObject:
		mm = cube([self.camera_size,self.camera_size*2,self.mount_thick], center=True)
		mm = translate([0,self.camera_size/2,0])(mm)
		mm -= self.screws()
		return mm

	def offset_block(self) -> OpenSCADObject:
		ob = cube([20,self.camera_size,self.mount_thick],center=True)
		ob = translate([-self.camera_size/2-8,0,0])(ob)
		return ob

	def bisect_floor(self,input) -> OpenSCADObject:
		size = 300
		floor = translate([0,0,-150])(cube([300,300,300],center = True))
		return input - floor


if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	e = ef.Fittings(10)
	m = CameraMount()
	a = m.camera_mount()
	t = e.one_end_tube()
	t = rotate(a = 90,v = (0,1,0))(t)
	t = translate([-53,0,-10])(t)
	b = m.offset_block()
	a += t + b
	a = rotate(a = 15, v = (0,1,0))(a)
	a = translate([0,0,2])(a)
	a = m.bisect_floor(a)

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
 
 
************************************************/
