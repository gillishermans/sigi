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

inputs = (
	("Thesis filter", "label"),
	("Creator: Gillis Hermans", "label"),
	)

def perform(level, box, options):
    m = scan_structure(level,box,options)
    print(m)
    shapes = initial_shapes(m)
    print("SHAPES")
    print(shapes)
    #ms = read_array(0)
    #print(ms)
    #shapes = initial_shapes(ms)
    #print(shapes)
    shapes = shp.hill_climbing(shapes)
    shapes = shp.filter_final_shapes_total(shapes,m)
    i=0
    #for s in shapes:
        #build_shape(s,level,box,i)
        #print(s.plane)
        #for s2 in shapes:
        #    print(shp.is_duplicate_shape(s,s2))
        #build_shape(shp.to_zy(s),level,box,i+1)
        #i = i+2
    rel = shp.relation_learning(shp.copy_shapes(shapes))
    print("REL")
    for r in rel:
        print(r)
    i=0
    final = shp.production(shp.copy_shapes(shapes),rel,50)
    for s in final:
        build_shape(s, level, box,0)
        build_shape(s, level, box,5+i)
        i=i+1
    i = 0
    #final = shp.production(shp.copy_shapes(shapes), rel, 15)
    #for s in final:
    #    build_shape(s, level, box, 20)
    #    build_shape(s, level, box,25+i)
    #    i = i + 1
    #i = 0
    #final = shp.production(shp.copy_shapes(shapes), rel, 25)
    #for s in final:
    #    build_shape(s, level, box,40)
    #    build_shape(s, level, box,45+i)
    #    i = i + 1

#scan the box for a structure and the probabilities of the blocks used in the structure
def scan_structure(level,box,options):
    nb=0
    prob=[]
    m = np.zeros((box.maxx-box.minx,box.maxy-box.miny,box.maxz-box.minz))
    ma = [[[Block(level.blockAt(x,y,z),level.blockDataAt(x,y,z),x-box.minx,y-box.miny,z-box.minz) for z in range(box.minz,box.maxz)] for y in range(box.miny,box.maxy)] for x in range(box.minx,box.maxx)]

    for x in range(box.minx,box.maxx):
        for y in range(box.miny,box.maxy):
            for z in range(box.minz,box.maxz):
                blockid = level.blockAt(x,y,z)
                dmg = level.blockDataAt(x,y,z)
                m[x-box.minx][y-box.miny][z-box.minz] = Block(blockid,dmg,x,y,z)
                if blockid != 0 and blockid != 2 and blockid != 3:
                    nb = nb+1
                    shp.add_block(nb,prob,blockid,dmg)
    write_array(m)
    write_to_file(prob)
    return ma

#writes the probabilities to a text file
def write_to_file(prob):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = os.path.join(__location__, 'g_data.txt')
    file = open(file_to_open,"w")
    for p in prob:
        file.write(str(p[0])+" "+str(p[3])+" "+str(p[2])+"\n")
    file.close()

#writes a 3d array to a text file
def write_array(array):
    #Find path
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    i = 0
    while os.path.exists(__location__ + "\data\data%s.txt" % i):
        i += 1
    file_to_open = __location__ + "\data\data%s.txt" % i
    #Save the array in slices so it is readable
    with open(file_to_open, 'w') as f:
        f.write("#"+str(array.shape[0])+','+str(array.shape[1])+','+str(array.shape[2])+'\n')
        for slice in array:
            np.savetxt(f, slice, fmt='%-7.2f')
            f.write('# slice\n')
    return i

#Reads a 3d array in from a text file
def read_array(i):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    #parse the shape of the array
    with open(__location__ + "\data\data%s.txt" % i) as f:
        l = f.readline()
        print(l)
        a = l.split(',')
        a[0] = int(a[0][1:])
        a[1] = int(a[1])
        a[2] = int(a[2])
        print(a)

    #load the array and reshape to 3d
    na = np.loadtxt(__location__ + "\data\data%s.txt" % i)
    na = na.reshape((a[0], a[1], a[2]))

    m = [[[Block(int(na[x,y,z]),round(100*(na[x,y,z] - int(na[x,y,z]))),x,y,z) for z in range(0,len(na[0][0]))] for y in range(0,len(na[0]))] for x in range(0,len(na))]
    return m

#SHAPE FITTER

#start with every block a shape of length 1
def initial_shapes(m):
    shapes = []
    for row in m:
        for col in row:
            for b in col:
                #if block is not air
                if b.id != 0:
                    #start shape matching procedure
                    s = Shape(b,'xy')
                    shapes.append(s)
                    s = Shape(b, 'xz')
                    shapes.append(s)
                    s = Shape(b, 'zy')
                    shapes.append(s)
    return shapes

#SHAPE BUILDER

def build_shape(s,level,box,i=0):
    print("BUILD")
    print(s)
    y = box.miny
    for b in s:
        #print("BUILD")
        #print(b)
        #print(b.id)
        #print(b.dmg)
        #utilityFunctions.setBlock(level, (b.id, b.dmg), box.maxx + b.rx, box.maxy + b.ry, box.minz + b.rz + 10 + (i * 6))
        utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + b.x, y + b.y, box.minz + b.z + 10 + (i*6))

def main():
    ms = read_array(0)
    print(ms)
    shapes = initial_shapes(ms)
    print(shapes)
    shapes = shp.hill_climbing(shapes)
    print(shapes)
    for s in shapes:
        build_shape(s,level,box)

if __name__ == "__main__":
    main()