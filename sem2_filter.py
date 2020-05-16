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
    ("---------Shape Inference---------", "label"),
    ("Operation: merge(0), split(1) or both(2):", 0),
    ("Specification: rectangular(0), planar(1) or 3D shapes(2):", 0),
    ("Cost function: basic(0), complex(1) or matching discount(2):", 0),
    ("Alpha:", 1.5),
    ("Overlap allowed:", True),
    ("Apply post split operation:", False),
    ("-----------Generation-----------", "label"),
    ("Number of rule derivations:", 100),
    ("Apply enclosure constraint:", False),
    ("Split grammar (experimental):", False),
    ("Visualize overlap (experimental):", False)
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
    shapes = io.initial_shapes(m, options["Specification: rectangular(0), planar(1) or 3D shapes(2):"])
    if options["Cost function: basic(0), complex(1) or matching discount(2):"] == 2:
        shapes = shp.hill_climbing(shapes, options["Specification: rectangular(0), planar(1) or 3D shapes(2):"],
                                   options["Operation: merge(0), split(1) or both(2):"], options["Cost function: basic(0), complex(1) or matching discount(2):"],
                                   float(options["Alpha:"]), m, shp.get_duplicate_shapes(shapes))
    else:
        shapes = shp.hill_climbing(shapes, options["Specification: rectangular(0), planar(1) or 3D shapes(2):"],
                                   options["Operation: merge(0), split(1) or both(2):"], options["Cost function: basic(0), complex(1) or matching discount(2):"],
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
        #io.build_shape(s, level, box, options["Visualize overlap (experimental):"], 10 + i)
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
        for f in r[0]:
            s = shp.edit_pos_relation(f, r[2], r[1])
            #if r[2].eq_production(f):
            #    io.build_shape(f, level, box, options["Visualize overlap (experimental):"], 10+i,-15, True)
            #else:
            #io.build_shape(f, level, box, options["Visualize overlap (experimental):"], 10 + i, -15)
            #io.build_shape(s, level, box, options["Visualize overlap (experimental):"], 10 + i,-15)
            i += 1
            j +=1
        i += 2

    for p in range(1):
        print("production")
        print(p)
        if options["Number of rule derivations:"] != 0:
            if options["Split grammar (experimental):"]:
                final = splt.split_grammar(shp.copy_shapes(shapes), rel)

            else:
                final = shp.production_limit(shp.copy_shapes(shapes), rel, [25, 25, 25], options["Number of rule derivations:"], False)
            print("Production shapes done")
            i = 0
            if not options["Apply enclosure constraint:"]:

                print("Building")
                for s in final:
                    io.build_shape(s, level, box, options["Visualize overlap (experimental):"], 4 + (p*2))
                    # build_shape(s, level, box,options["Visualize overlap (experimental):"],10+i)
                    i = i + 1


            else:

                #final = shp.fill_production(final, rel, 100)
                #print("Building")
                #for s in final:
                #  io.build_shape(s, level, box, options["Visualize overlap (experimental):"], 1 + ((p+5) * 2))
                   # build_shape(s, level, box,options["Visualize overlap (experimental):"],10+i)
                #  i = i + 1


                enclosed = encl.enclosure_update_3d(final)
                print("enclosure done")
                for s in enclosed:
                    io.build_shape(s, level, box, options["Visualize overlap (experimental):"], 1)
                    # build_shape(s, level, box,options["Visualize overlap (experimental):"],10+i)
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
