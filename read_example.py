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
    ("Read an example into disk", "label"),
    ("Creator: Gillis Hermans", "label")
)


# Perform the filter: scan the structure, extract the shapes and shape relations and produce a new structure.
def perform(level, box, options):
    m = scan_structure(level, box, options)


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
    write_array(m)
    return ma

# Writes a 3-dimensional array to a text file.
def write_array(array):
    # Find path
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    i = 0
    while os.path.exists(__location__ + "\examples\example%s.txt" % i):
        i += 1
    file_to_open = __location__ + "\examples\example%s.txt" % i
    # Save the array in slices so it is readable
    with open(file_to_open, 'w') as f:
        #f.write("#" + str(array.shape[0]) + ',' + str(array.shape[1]) + ',' + str(array.shape[2]) + '\n')
        for slice in array:
            np.savetxt(f, slice, fmt='%-7.2f')
            f.write('# slice\n')
    return i


