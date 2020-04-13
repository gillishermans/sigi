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

# Scan the box for a structure and the probabilities of the blocks used in the structure.
def scan_structure(level, box):
    nb = 0
    prob = []
    m = np.zeros((box.maxx - box.minx, box.maxy - box.miny, box.maxz - box.minz))
    ma = [[[Block(level.blockAt(x, y, z), level.blockDataAt(x, y, z), x - box.minx, y - box.miny, z - box.minz) for z in
            range(box.minz, box.maxz)] for y in range(box.miny, box.maxy)] for x in range(box.minx, box.maxx)]

    for x in range(box.minx, box.maxx):
        for y in range(box.miny, box.maxy):
            for z in range(box.minz, box.maxz):
                block_id = level.blockAt(x, y, z)
                dmg = level.blockDataAt(x, y, z)
                m[x - box.minx][y - box.miny][z - box.minz] = Block(block_id, dmg, x, y, z)
                if block_id != 0 and block_id != 2 and block_id != 3:
                    nb = nb + 1
                    shp.add_block(nb, prob, block_id, dmg)
    return ma

# Writes the probabilities to a text file.
def write_to_file(prob):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = os.path.join(__location__, 'g_data.txt')
    file = open(file_to_open, "w")
    for p in prob:
        file.write(str(p[0]) + " " + str(p[3]) + " " + str(p[2]) + "\n")
    file.close()

# Reads a 3d array from a text file.
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
        for slc in array:
            np.savetxt(f, slc, fmt='%-7.2f')
            f.write('# slice\n')
    return i

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


# Reads a shape set from a text file.
def read_shapes(i):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    shapes = []

    # parse the shape of the array
    with open(__location__ + "\data\data%s.txt" % i) as f:
        lines = list(f)
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