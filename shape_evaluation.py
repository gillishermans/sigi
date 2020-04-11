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
import timeit

inputs = (
    ("Shape grammar induction and production", "label"),
    ("Creator: Gillis Hermans", "label")
)


def evaluate_alpha(level,box,options):
    m = scan_structure(level, box, options)
    initial = initial_shapes(m)
    av = [0.5,1.0,1.5]#[0.0,0.25,0.5,0.75,1.0,1.1,1.25,1.5,1.75,2,5,10]

    example = 1
    file_nb = 0
    for rect in [0]:
        for operation in [0,1,2]:
            for cost in [0,1]:
                for overlap in [True,False]:
                    write_experiment(file_nb, example, rect, operation, cost, overlap)
                    alpha_experiment(initial, av, rect, operation, cost, overlap, m, file_nb)
                    file_nb += 1


def alpha_experiment(initial, alpha_list, rect, operation, cost, overlap, m, file_nb):
    for alpha in alpha_list:
        tic = timeit.default_timer()
        shapes = shp.hill_climbing(initial, rect, operation, cost, alpha, m)
        if overlap:
            shapes = shp.filter_final_shapes_overlap(shapes, m)
        else:
            shapes = shp.filter_final_shapes_no_overlap(shapes)
        toc = timeit.default_timer()
        avg_size = 0
        min_size = 99999
        max_size = 0
        avg_complex = 0
        max_complex = 0
        min_complex = 99999
        sizes = []
        complexity = []
        for s in shapes:
            sizes.append(len(s))
            avg_size += len(s)
            if min_size > len(s): min_size = len(s)
            if max_size < len(s): max_size = len(s)
            blocktypes = set([(x.id + x.dmg/100) for x in s])
            complexity.append(len(blocktypes))
            avg_complex += len(blocktypes)
            if min_complex > len(blocktypes): min_complex = len(blocktypes)
            if max_complex < len(blocktypes): max_complex = len(blocktypes)
        mean_size = np.mean(sizes)#float(avg) / float(len(shapes))
        mean_complex = np.mean(complexity)#float(avg_c) / float(len(shapes))
        median_size = np.median(sizes)
        median_complex = np.median(complexity)

        duplicate_list = shp.get_duplicate_shapes(shapes)
        identical = 0
        for d in duplicate_list:
            identical += len(d) -1
        #print("Cost",shp.shapes_cost(shapes, options["Cost function:"], alpha))

        time_spent = (toc - tic)
        write_alpha_experiment(file_nb,alpha,len(shapes),mean_size,median_size,max_size,min_size,mean_complex,median_complex,max_complex,min_complex,identical,time_spent)

def write_experiment(file_nb, example, rect, operation, cost, overlap):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = __location__ + "\evaluation\experiment%s.txt" % file_nb
    file = open(file_to_open, "w")
    file.write("Example: " + str(example) +"\n")
    file.write("Rect(0), same plane(1) or 3D shapes(2): " + str(rect) +"\n")
    file.write("Merge(0), split(1) or both(2): " + str(operation) +"\n")
    file.write("Cost function: " + str(cost) +"\n")
    file.write("Overlap allowed: " + str(overlap) +"\n")
    file.write("\n")
    file.close()


def write_alpha_experiment(file_nb,alpha,nb_shapes,avg_size,mean_size,max_size,min_size,avg_complex,mean_complex,max_complex,min_complex,identical,time):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = __location__ + "\evaluation\experiment%s.txt" % file_nb
    file = open(file_to_open, "a")
    file.write("Alpha: " + str(alpha) +"\n")
    file.write("Number of shapes: " + str(nb_shapes) +"\n")
    file.write("Mean shape size: " + str(avg_size) +"\n")
    file.write("Median shape size: " + str(mean_size) +"\n")
    file.write("Largest shape: " + str(max_size) +"\n")
    file.write("Smallest shape: " + str(min_size) +"\n")
    file.write("Mean complexity: " + str(avg_complex) +"\n")
    file.write("Median complexity: " + str(mean_complex) +"\n")
    file.write("Max complexity: " + str(max_complex) +"\n")
    file.write("Min complexity: " + str(min_complex) +"\n")
    file.write("Number of 'redundant' identical shapes: " + str(identical) +"\n")
    file.write("Time spent: " + str(time) +"\n")
    file.write("\n")
    file.close()

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