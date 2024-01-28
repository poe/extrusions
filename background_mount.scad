translate(v = [0, 0, 92]) {
	union() {
		difference() {
			cylinder($fn = 256, center = true, h = 188, r = 101.0);
			union() {
				cylinder($fn = 256, center = true, h = 190, r = 100.0);
				translate(v = [200, 0, 0]) {
					cube(center = true, size = [400, 400, 380]);
				}
			}
		}
		translate(v = [0, 0, -184]) {
			difference() {
				cylinder($fn = 256, center = true, h = 190, r = 110.0);
				union() {
					cylinder($fn = 256, center = true, h = 200, r = 80.0);
					translate(v = [200, 0, 0]) {
						cube(center = true, size = [400, 400, 380]);
					}
					translate(v = [0, 0, -100]) {
						cube(center = true, size = [400, 400, 380]);
					}
				}
			}
		}
		translate(v = [-114, 0, 56]) {
			difference() {
				rotate(a = 270, v = [0, 1, 0]) {

					difference() {
						union() {
							union();
							translate(v = [-40, 0, 0]) {
								rotate(a = [0, 90.0, 0.0]) {
									translate(v = [0, 0, 40.0]) {
										cube(center = true, size = [32.0000000000, 32.0000000000, 80.0]);
									}
								}
							}
							union();
						}
						union() {
							union();
							translate(v = [-40, 0, 0]) {
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
													translate(v = [0, 61.0, 0]) {
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
																polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 80.0], [-10.2, 2.8, 80.0], [-4.3999999999999995, 2.8, 80.0], [-4.3999999999999995, 0.0, 80.0], [0.0, 0.0, 80.0]]);
																mirror(v = [0, 1]) {
																	polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 80.0], [-10.2, 2.8, 80.0], [-4.3999999999999995, 2.8, 80.0], [-4.3999999999999995, 0.0, 80.0], [0.0, 0.0, 80.0]]);
																}
																mirror(v = [1, 1]) {
																	union() {
																		polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 80.0], [-10.2, 2.8, 80.0], [-4.3999999999999995, 2.8, 80.0], [-4.3999999999999995, 0.0, 80.0], [0.0, 0.0, 80.0]]);
																		mirror(v = [0, 1]) {
																			polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 80.0], [-10.2, 2.8, 80.0], [-4.3999999999999995, 2.8, 80.0], [-4.3999999999999995, 0.0, 80.0], [0.0, 0.0, 80.0]]);
																		}
																	}
																}
																mirror(v = [1, -1]) {
																	union() {
																		polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 80.0], [-10.2, 2.8, 80.0], [-4.3999999999999995, 2.8, 80.0], [-4.3999999999999995, 0.0, 80.0], [0.0, 0.0, 80.0]]);
																		mirror(v = [0, 1]) {
																			polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 80.0], [-10.2, 2.8, 80.0], [-4.3999999999999995, 2.8, 80.0], [-4.3999999999999995, 0.0, 80.0], [0.0, 0.0, 80.0]]);
																		}
																		mirror(v = [1, 1]) {
																			union() {
																				polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 80.0], [-10.2, 2.8, 80.0], [-4.3999999999999995, 2.8, 80.0], [-4.3999999999999995, 0.0, 80.0], [0.0, 0.0, 80.0]]);
																				mirror(v = [0, 1]) {
																					polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 80.0], [-10.2, 2.8, 80.0], [-4.3999999999999995, 2.8, 80.0], [-4.3999999999999995, 0.0, 80.0], [0.0, 0.0, 80.0]]);
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
														translate(v = [0, 61.0, 0]) {
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
														translate(v = [0, 61.0, 0]) {
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
														translate(v = [0, 61.0, 0]) {
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
														translate(v = [0, 61.0, 0]) {
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
					}}
				translate(v = [0, 0, -20]) {
					rotate(a = 45, v = [0, 45, 0]) {
						cube(center = true, size = [120, 40, 60]);
					}
				}
			}
		}
	}
}
