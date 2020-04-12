from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
import math as math
from random import *
import numpy as np
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import utilityFunctions as utilityFunctions
import sys
from sem2_shape import Block, Shape
import sem2_shape as shp
import split_grammar as splt
import enclosure as encl
import in_out as io

inputs = (
    ("Shape grammar induction and production", "label"),
    ("Creator: Gillis Hermans", "label"),
    ("Merge(0), split(1) or both(2):", 0),
    ("Rect(0), same plane(1) or 3D shapes(2):", 0),
    ("Cost function:", 0),
    ("Alpha:", 150),
    ("Split grammar:", False),
    ("Apply post split operation:", False),
    ("Overlap allowed:", True),
    ("Visualize overlap:", False),
    ("Rotate the first produced shape:", False)
)


# Perform the filter: scan the structure, extract the shapes and shape relations and produce a new structure.
def perform(level, box, options):

    #default = io.read_shapes(1)
    #for s in default:
    #    io.build_shape(s, level, box, options, 1)
    #enclosed = encl.enclosure_update_3d(default)
    #for s in enclosed:
    #    io.build_shape(s, level, box, options, 10)
    #return

    m = io.scan_structure(level, box, options)
    shapes = io.initial_shapes(m)
    shapes = shp.hill_climbing(shapes, options["Rect(0), same plane(1) or 3D shapes(2):"], options["Merge(0), split(1) or both(2):"], options["Cost function:"], float(options["Alpha:"])/100.0, m)
    if options["Overlap allowed:"]:
        shapes = shp.filter_final_shapes_overlap(shapes, m)
    else:
        shapes = shp.filter_final_shapes_no_overlap(shapes)
    i = 0
    for s in shapes:
        io.build_shape(s, level, box, options, 10 + i)
        i = i + 1
    print("Hill climbing done")
    print(shapes)
    if options["Apply post split operation:"]:
        shapes = shp.post_plane_split(shapes, 'xz')
        shapes = shp.post_plane_split(shapes, 'xy')
        shapes = shp.post_plane_split(shapes, 'zy')
        for s in shapes:
            io.build_shape(s, level, box, options, 25 + i)
            i = i + 1
        #print("Post split results:")
        #print(shapes)
    #io.write_shapes(shapes)
    #default = io.read_shapes(0)
    #print(default)
    #print("SCORE")
    #print(shp.similarity_shape_sets(default,shapes))
    rel = shp.relation_learning(shp.copy_shapes(shapes))
    print("Relation learning done")
    print(rel)

    if options["Split grammar:"]:
        final = splt.split_grammar(shp.copy_shapes(shapes), rel)

    else:
        final = shp.production_limit(shp.copy_shapes(shapes), rel, [25, 25, 25], 200, options["Rotate the first produced shape:"])
    print("Production shapes done")
    i = 0
    print("Building")
    for s in final:
        io.build_shape(s, level, box, options, 1)
        # build_shape(s, level, box,options,10+i)
        i = i + 1

    return

    enclosed = encl.enclosure_update_3d(final)
    print("enclosure done")
    for s in enclosed:
        io.build_shape(s, level, box, options, 20)
        # build_shape(s, level, box,options,10+i)
        i = i + 1

def main():
    ms = read_array(0)
    print(ms)
    shapes = initial_shapes(ms)
    print(shapes)
    shapes = shp.hill_climbing(shapes)
    print(shapes)
    for s in shapes:
        build_shape(s, level, box, options)


if __name__ == "__main__":
    main()
