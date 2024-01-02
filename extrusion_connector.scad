module copy_mirror(vec){
    children();
    mirror(vec)
    children();
}

tolerance = .1;
outer_corner = 14;
inner_corner = 10 + tolerance;
nub_length = 6 - tolerance;
rail_thickness = .5;
gap_size = 3 - tolerance;
tube_length = 50;

silhouette_points = [[inner_corner,inner_corner],[inner_corner,gap_size],
                    [inner_corner - nub_length, gap_size],[inner_corner - nub_length, 0],
                    [outer_corner,0],[outer_corner,outer_corner]];
                linear_extrude(height = tube_length, center = true, convexity = 0, twist = 0){
                    copy_mirror([-1,1,0])
                        copy_mirror([1,1,0])
                            copy_mirror([1,0,0])
                                polygon(silhouette_points,10);
                }
render();