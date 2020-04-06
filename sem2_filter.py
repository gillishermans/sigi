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

inputs = (
    ("Shape grammar induction and production", "label"),
    ("Creator: Gillis Hermans", "label"),
    ("Merge or split:", 0),
    ("Cost function:", 0),
    ("Alpha:", 150),
    ("Split grammar:", 0),
    ("Apply post split operation:", 0),
    ("Overlap allowed:", 1),
    ("Visualize overlap:", 0),
    ("Add rotated shapes:", 1)
)


# Perform the filter: scan the structure, extract the shapes and shape relations and produce a new structure.
def perform(level, box, options):

    #default = read_shapes(1)
    #for s in default:
    #    build_shape(s, level, box, options, 1)
    #enclosed = encl.enclosure_update_3d(default)
    #for s in enclosed:
    #    build_shape(s, level, box, options, 10)
    #return

    m = scan_structure(level, box, options)
    shapes = initial_shapes(m)
    shapes = shp.hill_climbing(shapes, options["Merge or split:"], options["Cost function:"], float(options["Alpha:"])/100.0, m)
    if options["Overlap allowed:"] != 0:
        shapes = shp.filter_final_shapes_overlap(shapes, m)
    else:
        shapes = shp.filter_final_shapes_no_overlap(shapes)
    i = 0
    for s in shapes:
        build_shape(s, level, box, options, 5 + i)
        i = i + 1
    #print("Hill climbing results:")
    #print(shapes)
    if options["Apply post split operation:"] != 0:
        shapes = shp.post_plane_split(shapes, 'xz')
        shapes = shp.post_plane_split(shapes, 'xy')
        shapes = shp.post_plane_split(shapes, 'zy')
        for s in shapes:
            build_shape(s, level, box, options, 25 + i)
            i = i + 1
        #print("Post split results:")
        #print(shapes)
    #write_shapes(shapes)
    #default = read_shapes(0)
    #print(default)
    #print("SCORE")
    #print(shp.similarity_shape_sets(default,shapes))
    if options["Add rotated shapes:"] == 1:
        new_shapes = []
        for s in shapes:
            if s.plane == 'xy':
                ns = s.copy()
                ns = shp.to_zy(ns)
                new_shapes.append(ns)
            if s.plane == 'zy':
                ns = s.copy()
                ns = shp.to_xy(ns)
                new_shapes.append(ns)
            else:
                continue
        shapes.extend(new_shapes)
        #print("Rotated shapes results:")
        #print(shapes)
    rel = shp.relation_learning(shp.copy_shapes(shapes))
    #print("Relation learning results:")
    #print(rel)

    if options["Split grammar:"] == 0:
        final = shp.production_limit(shp.copy_shapes(shapes), rel, [25, 25, 25], 500)
        print("Production shapes")
    else:
        final = splt.split_grammar(shp.copy_shapes(shapes), rel)
    i = 0
    print("Building")
    for s in final:
        build_shape(s, level, box, options, 1)
        # build_shape(s, level, box,options,10+i)
        i = i + 1

    return

    enclosed = encl.enclosure_update_3d(final)
    for s in enclosed:
        build_shape(s, level, box, options, 10)
        # build_shape(s, level, box,options,10+i)
        i = i + 1


# Scan the box for a structure and the probabilities of the blocks used in the structure.
def scan_structure(level, box, options):
    nb = 0
    prob = []
    m = np.zeros((box.maxx - box.minx, box.maxy - box.miny, box.maxz - box.minz))
    ma = [[[Block(level.blockAt(x, y, z), level.blockDataAt(x, y, z), x - box.minx, y - box.miny, z - box.minz) for z in
            range(box.minz, box.maxz)] for y in range(box.miny, box.maxy)] for x in range(box.minx, box.maxx)]

    for x in range(box.minx, box.maxx):
        for y in range(box.miny, box.maxy):
            for z in range(box.minz, box.maxz):
                blockid = level.blockAt(x, y, z)
                dmg = level.blockDataAt(x, y, z)
                m[x - box.minx][y - box.miny][z - box.minz] = Block(blockid, dmg, x, y, z)
                if blockid != 0 and blockid != 2 and blockid != 3:
                    nb = nb + 1
                    shp.add_block(nb, prob, blockid, dmg)
    # write_array(m)
    # write_to_file(prob)
    return ma


# Writes a shape set to a text file.
def write_shapes(shapes):
    # Find path
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    i = 0
    while os.path.exists(__location__ + "\data\shapes%s.txt" % i):
        i += 1
    file_to_open = __location__ + "\data\shapes%s.txt" % i

    # Save the array in slices so it is readable
    with open(file_to_open, 'w') as f:
        #f.write("#" + str(array.shape[0]) + ',' + str(array.shape[1]) + ',' + str(array.shape[2]) + '\n')
        for s in shapes:
            print(s)
            f.write(s.write_str())
            f.write('\n')
    return i

def read_shapes(i):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    shapes = []

    # parse the shape of the array
    with open(__location__ + "\data\shapes%s.txt" % i) as f:
        lines = list(f)
        #l = f.readline()
        for l in lines:
            a = l.split(' ')

            # Build a shape for every line
            # Remove the last element (\n)
            a.pop(len(a)-1)
            # Remove the first element (the plane)
            plane = a.pop(0)
            blocks = []
            for i in range (0,int(len(a)/5)):
                blocks.append(Block(int(a[i*5]),int(a[i*5+1]),int(a[i*5+2]),int(a[i*5+3]),int(a[i*5+4])))
            shapes.append(shp.shape_from_blocks(blocks,plane))

    return shapes


# Reads a 3d array in from a text file.
def read_array(i):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    # parse the shape of the array
    with open(__location__ + "\data\example%s.txt" % i) as f:
        l = f.readline()
        print(l)
        a = l.split(',')
        a[0] = int(a[0][1:])
        a[1] = int(a[1])
        a[2] = int(a[2])
        print(a)

    # load the array and reshape to 3d
    na = np.loadtxt(__location__ + "\data\example%s.txt" % i)
    na = na.reshape((a[0], a[1], a[2]))

    m = [[[Block(int(na[x, y, z]), round(100 * (na[x, y, z] - int(na[x, y, z]))), x, y, z) for z in
           range(0, len(na[0][0]))] for y in range(0, len(na[0]))] for x in range(0, len(na))]
    return m


# Writes the probabilities to a text file.
def write_to_file(prob):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = os.path.join(__location__, 'g_data.txt')
    file = open(file_to_open, "w")
    for p in prob:
        file.write(str(p[0]) + " " + str(p[3]) + " " + str(p[2]) + "\n")
    file.close()


# Writes a 3-dimensional array to a text file.
def write_array(array):
    # Find path
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    i = 0
    while os.path.exists(__location__ + "\data\example%s.txt" % i):
        i += 1
    file_to_open = __location__ + "\data\example%s.txt" % i
    # Save the array in slices so it is readable
    with open(file_to_open, 'w') as f:
        #f.write("#" + str(array.shape[0]) + ',' + str(array.shape[1]) + ',' + str(array.shape[2]) + '\n')
        for slice in array:
            np.savetxt(f, slice, fmt='%-7.2f')
            f.write('# slice\n')
    return i


# Start with every block a shape of length 1 in every plane.
def initial_shapes(m):
    shapes = []
    for row in m:
        for col in row:
            for b in col:
                # If block is not air.
                if b.id != 0:
                    s = Shape(b, 'xy')
                    shapes.append(s)
                    s = Shape(b, 'xz')
                    shapes.append(s)
                    s = Shape(b, 'zy')
                    shapes.append(s)
    return shapes


# Build a shape. Place it in the world at it's position.
def build_shape(s, level, box, options, i=0):
    # print("BUILD")
    # print(s)
    y = box.miny
    for b in s:
        if options["Visualize overlap:"] == 1 and level.blockAt(box.minx + b.x, y + b.y,
                                                                box.minz + b.z + 10 + (i * 6)) != 0:
            utilityFunctions.setBlock(level, (35, b.dmg), box.minx + b.x, y + b.y, box.minz + b.z + 10 + (i * 6))
        else:
            utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + b.x, y + b.y, box.minz + b.z + 10 + (i * 6))


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
