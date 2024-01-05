// Generated by SolidPython 1.1.3 on 2024-01-05 11:42:16


difference() {
	rotate(a = 90, v = [1, 0, 0]) {
		rotate(a = 45, v = [0, 0, 1]) {
			difference() {
				union() {
					union();
					translate(v = [-16, 0, 15]) {
						rotate(a = [0, 90.0, 0.0]) {
							translate(v = [0, 0, 38.0]) {
								cube(center = true, size = [32.0000000000, 32.0000000000, 76.0]);
							}
						}
					}
					translate(v = [0, -16, -15]) {
						rotate(a = [0, 90.0, 90.0]) {
							translate(v = [0, 0, 38.0]) {
								cube(center = true, size = [32.0000000000, 32.0000000000, 76.0]);
							}
						}
					}
					union() {
						union();
						hull() {
							union() {
								translate(v = [-16, 0, 15]) {
									rotate(a = [0, 90.0, 0.0]) {
										translate(v = [0, 0, 38.0]) {
											cube(center = true, size = [10, 10, 76.0]);
										}
									}
								}
								translate(v = [0, -16, -15]) {
									rotate(a = [0, 90.0, 90.0]) {
										translate(v = [0, 0, 38.0]) {
											cube(center = true, size = [10, 10, 76.0]);
										}
									}
								}
							}
						}
					}
				}
				union() {
					union();
					translate(v = [-16, 0, 15]) {
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
											translate(v = [0, 57.0, 0]) {
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
														polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
														mirror(v = [0, 1]) {
															polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
														}
														mirror(v = [1, 1]) {
															union() {
																polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																mirror(v = [0, 1]) {
																	polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																}
															}
														}
														mirror(v = [1, -1]) {
															union() {
																polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																mirror(v = [0, 1]) {
																	polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																}
																mirror(v = [1, 1]) {
																	union() {
																		polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																		mirror(v = [0, 1]) {
																			polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
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
												translate(v = [0, 57.0, 0]) {
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
												translate(v = [0, 57.0, 0]) {
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
												translate(v = [0, 57.0, 0]) {
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
												translate(v = [0, 57.0, 0]) {
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
					translate(v = [0, -16, -15]) {
						rotate(a = [0, 90.0, 90.0]) {
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
											translate(v = [0, 57.0, 0]) {
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
														polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
														mirror(v = [0, 1]) {
															polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
														}
														mirror(v = [1, 1]) {
															union() {
																polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																mirror(v = [0, 1]) {
																	polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																}
															}
														}
														mirror(v = [1, -1]) {
															union() {
																polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																mirror(v = [0, 1]) {
																	polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																}
																mirror(v = [1, 1]) {
																	union() {
																		polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
																		mirror(v = [0, 1]) {
																			polyhedron(convexity = 10, faces = [[0, 1, 5], [1, 6, 5], [1, 2, 6], [2, 7, 6], [2, 3, 7], [3, 8, 7], [3, 4, 8], [4, 9, 8], [4, 0, 9], [0, 5, 9], [4, 3, 2, 1, 0], [5, 6, 7, 8, 9]], points = [[-10.2, 10.2, 0.0], [-10.2, 2.8, 0.0], [-4.3999999999999995, 2.8, 0.0], [-4.3999999999999995, 0.0, 0.0], [0.0, 0.0, 0.0], [-10.2, 10.2, 76.0], [-10.2, 2.8, 76.0], [-4.3999999999999995, 2.8, 76.0], [-4.3999999999999995, 0.0, 76.0], [0.0, 0.0, 76.0]]);
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
												translate(v = [0, 57.0, 0]) {
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
												translate(v = [0, 57.0, 0]) {
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
												translate(v = [0, 57.0, 0]) {
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
												translate(v = [0, 57.0, 0]) {
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
	translate(v = [0, 0, -150]) {
		cube(center = true, size = [300, 300, 300]);
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
#! /usr/bin/env python3
# from solid.solidpython import *
from solid.solidpython import Path, scad_render_to_file
import sys

import extrusion_fittings as ef

if __name__ == "__main__":
	out_dir = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent

	a = ef.offset_cross()

	file_out = scad_render_to_file(a,  out_dir=out_dir, include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")
 
 
************************************************/
