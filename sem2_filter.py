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
    ("Generate procedural model for example structure.", "label"),
    ("Creator: Gillis Hermans", "label"),
    ("Merge(0), split(1) or both(2):", 0),
    ("Rect(0), same plane(1) or 3D shapes(2):", 0),
    ("Cost function:", 0),
    ("Alpha:", 1.5),
    ("Number of production shapes:", 100),
    ("Split grammar:", False),
    ("Apply post split operation:", False),
    ("Overlap allowed:", True),
    ("Visualize overlap:", False),
    ("Rotate the first produced shape:", False),
    ("Enclosure:", False)
)


def perform(level, box, options):

    #default = io.read_shapes(1)
    #for s in default:
    #    io.build_shape(s, level, box, options["Visualize overlap:"], 1)
    #enclosed = encl.enclosure_update_3d(default)
    #for s in enclosed:
    #    io.build_shape(s, level, box, options["Visualize overlap:"], 10)
    #return

    m = io.scan_structure(level, box)
    shapes = io.initial_shapes(m, options["Rect(0), same plane(1) or 3D shapes(2):"])
    if options["Cost function:"] == 2:
        shapes = shp.hill_climbing(shapes, options["Rect(0), same plane(1) or 3D shapes(2):"],
                                   options["Merge(0), split(1) or both(2):"], options["Cost function:"],
                                   float(options["Alpha:"]), m, shp.get_duplicate_shapes(shapes))
    else:
        shapes = shp.hill_climbing(shapes, options["Rect(0), same plane(1) or 3D shapes(2):"],
                                   options["Merge(0), split(1) or both(2):"], options["Cost function:"],
                                   float(options["Alpha:"]), m)
    print("Hill climbing done")
    if options["Overlap allowed:"]:
        shapes = shp.filter_final_shapes_overlap(shapes, m)
    else:
        shapes = shp.filter_final_shapes_no_overlap(shapes)
    print("overlap filter done")
    print("Hill climbing done")
    print(shapes)
    if options["Apply post split operation:"]:
        shapes = shp.post_plane_split(shapes, 'xz')
        shapes = shp.post_plane_split(shapes, 'xy')
        shapes = shp.post_plane_split(shapes, 'zy')
        #print("Post split results:")
        #print(shapes)
    i = 0
    for s in shapes:
        io.build_shape(s, level, box, options["Visualize overlap:"], 10 + i)
        i = i + 1
    #io.write_shapes(shapes)
    #default = io.read_shapes(0)
    #print(default)
    #print("SCORE")
    #print(shp.similarity_shape_sets(default,shapes))
    shapes = shp.normalize_relative(shapes)
    rel = shp.relation_learning(shp.copy_shapes(shapes))
    print("Relation learning done")
    print(rel)
    i = 0
    for r in rel:
        j = 0

        #if r[2].plane == 'xy':
        #    og_copy = shp.to_zy(r[2])
        #    s_copy = shp.to_xy(r[1])
        #else:
        #    og_copy = shp.to_xy(r[2])
        #    s_copy = shp.to_zy(r[1])
        #io.build_shape(og_copy, level, box, options["Visualize overlap:"], 10 + i -1, -15, True)
        #io.build_shape(s_copy, level, box, options["Visualize overlap:"], 10 + i - 1, -15, False)

        for f in r[0]:
            s = shp.edit_pos_relation(f, r[2], r[1])
            if r[2].eq_production(f):
                io.build_shape(f, level, box, options["Visualize overlap:"], 10+i,-15, True)
            else:
                io.build_shape(f, level, box, options["Visualize overlap:"], 10 + i, -15)
            io.build_shape(s, level, box, options["Visualize overlap:"], 10 + i,-15)
            i += 1
            j +=1
        i += 2

    for p in range(1):
        print("production")
        print(p)
        if options["Number of production shapes:"] != 0:
            if options["Split grammar:"]:
                final = splt.split_grammar(shp.copy_shapes(shapes), rel)

            else:
                final = shp.production_limit(shp.copy_shapes(shapes), rel, [25, 25, 25], options["Number of production shapes:"], options["Rotate the first produced shape:"])
            print("Production shapes done")
            i = 0
            if not options["Enclosure:"]:

                print("Building")
                for s in final:
                    io.build_shape(s, level, box, options["Visualize overlap:"], 1 + (p*2))
                    # build_shape(s, level, box,options["Visualize overlap:"],10+i)
                    i = i + 1

                #final = shp.fill_production(final, rel, 100)
                #print("Building")
                #for s in final:
                #    io.build_shape(s, level, box, options["Visualize overlap:"], 1 + ((p+5) * 2))
                #    # build_shape(s, level, box,options["Visualize overlap:"],10+i)
                #    i = i + 1


            else:
                enclosed = encl.enclosure_update_3d(final)
                print("enclosure done")
                for s in enclosed:
                    io.build_shape(s, level, box, options["Visualize overlap:"], 1)
                    # build_shape(s, level, box,options["Visualize overlap:"],10+i)
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
