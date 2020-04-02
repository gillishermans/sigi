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
import timeit

inputs = (
    ("Shape grammar induction and production", "label"),
    ("Creator: Gillis Hermans", "label"),
    ("Cost function:", 0),
    ("Alpha:", 150),
    ("Split grammar:", 0),
    ("Apply post split operation:", 0),
    ("Overlap allowed:", 1),
    ("Visualize overlap:", 0),
    ("Add rotated shapes:", 1)
)


def evaluate_alpha(level,box,options):
    m = scan_structure(level, box, options)
    initial = initial_shapes(m)
    av = [0.0,0.25,0.5,0.75,1.0,1.1,1.25,1.5,1.75,2,5,10]
    i = 0
    for alpha in av:
        tic = timeit.default_timer()
        shapes = shp.hill_climbing(initial, options["Cost function:"], alpha)
        if options["Overlap allowed:"] != 0:
            shapes = shp.filter_final_shapes_overlap(shapes, m)
        else:
            shapes = shp.filter_final_shapes_no_overlap(shapes)
        toc = timeit.default_timer()
        print("Experiment", i)
        print("Alpha", alpha)
        print("Number of shapes",len(shapes))
        avg = 0
        smallest = 99999
        largest = 0
        avg_c = 0
        most = 0
        least = 99999
        for s in shapes:
            avg += len(s)
            if smallest > len(s): smallest = len(s)
            if largest < len(s): largest = len(s)
            blocktypes = set([(x.id + x.dmg/100) for x in s])
            avg_c += len(blocktypes)
            if least > len(blocktypes): least = len(blocktypes)
            if most < len(blocktypes): most = len(blocktypes)
        avg = float(avg) / float(len(shapes))
        avg_c = float(avg_c) / float(len(shapes))
        print("Average shape size", avg)
        print("Largest shape", largest)
        print("Smallest shape", smallest)
        print("Average complexity", avg_c)
        print("Max complexity", least)
        print("Min complexity", most)
        print("Number of identical shapes")
        print("Time spent",(toc - tic))
        #print("Cost",shp.shapes_cost(shapes, options["Cost function:"], alpha))
        print("\n")
        i += 1
    i = 0
    for s in shapes:
        build_shape(s, level, box, options, 1 + i)
        i = i + 1

# Perform the filter: scan the structure, extract the shapes and shape relations and produce a new structure.
def perform(level, box, options):
    evaluate_alpha(level,box,options)


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
    while os.path.exists(__location__ + "\data\data%s.txt" % i):
        i += 1
    file_to_open = __location__ + "\data\data%s.txt" % i

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
    with open(__location__ + "\data\data%s.txt" % i) as f:
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
    with open(__location__ + "\data\data%s.txt" % i) as f:
        l = f.readline()
        print(l)
        a = l.split(',')
        a[0] = int(a[0][1:])
        a[1] = int(a[1])
        a[2] = int(a[2])
        print(a)

    # load the array and reshape to 3d
    na = np.loadtxt(__location__ + "\data\data%s.txt" % i)
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
    while os.path.exists(__location__ + "\data\data%s.txt" % i):
        i += 1
    file_to_open = __location__ + "\data\data%s.txt" % i
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