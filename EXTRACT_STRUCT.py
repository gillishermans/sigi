import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
import numpy as np
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from nltk import CFG, PCFG, ProbabilisticProduction, Nonterminal
from nltk.parse.generate import generate
import random
import utilityFunctions as utilityFunctions
import sys

class Block:
    def __init__(self, blockid, dmg, x, y, z):
        self.id = blockid
        self.dmg = dmg
        self.x = x
        self.y = y
        self.z = z
        self.used = False

    def __float__(self):
        return float(self.id + float(self.dmg)/100)
    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(float(self.id + float(self.dmg) / 100))
        #return '('+str(self.id)+', '+str(self.dmg)+') at ('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'

    def to_used(self):
        self.used = True

inputs = (
	("Extract Data", "label"),
	("Creator: Gillis Hermans", "label"),
	)

def perform(level, box, options):
    print("EXTRACT")
    m = scan_structure(level,box,options)
    print(m)
    print("FIT")
    shapes = fit_shape(m)
    for s in shapes:
        build_shape(s,level,box)
    #build_shape(shapes[0],level,box)

#help function to count probabilities of blocks used
def add_block(nb,prob,blockid,dmg):
    for b in prob:
        if b[0] == blockid and b[3] == dmg:
            b[1] = b[1]+1.0
            b[2] = b[1]/nb
            return
    prob.append([blockid,1.0,1.0/nb,dmg])

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
                    add_block(nb,prob,blockid,dmg)
    write_array(m)
    write_to_file(prob)
    return ma

#writes the found probabilities to a text file
def write_to_file(prob):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = os.path.join(__location__, 'g_data.txt')
    file = open(file_to_open,"w")
    for p in prob:
        #print(str(p[0]) + " " + str(p[3]) + " " + str(p[2]) + "\n")
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
        f.write("#"+str(array.shape[0])+','+str(array.shape[1])+','+str(array.shape[2])+'\n')#f.write('#{0}\n'.format(array.shape))
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
    new_array = np.loadtxt(__location__ + "\data\data%s.txt" % i)
    new_array = new_array.reshape((a[0], a[1], a[2]))
    return new_array

#SHAPE FITTER

#fit shapes to the structure
def fit_shape(m):
    shapes = []
    #go through every block
    for row in m:
        for col in row:
            for b in col:
                #print(str(b))
                #if block is not air
                if b.id != 0 and not b.used:
                    #start shape matching procedure
                    s,ma = match_rect(b,m)
                    shapes.append(s)
                    print('SHAPE')
                    print(s)
                    #print('REDUCED M')
                    #print(ma)
    print(shapes)
    return shapes

#build a matching rectangle starting from the given block
def match_rect(b,m):
    #first corner to last corner spanning a rectangle: only contains 2 blocks
    shape = [b]
    b.to_used()
    #x and y -> z same
    p = check_pos(m,b.x+1,b.y,b.z)
    if p.id != 0:
        m[b.x + 1][b.y][b.z].to_used()
        s, m = match_rect(p,m)
        shape.extend(s)

    p = check_pos(m,b.x-1,b.y,b.z)
    if p.id != 0:
        m[b.x - 1][b.y][b.z].to_used()
        s, m = match_rect(p,m)
        shape.extend(s)

    p = check_pos(m,b.x,b.y+1,b.z)
    if p.id != 0:
        m[b.x][b.y + 1][b.z].to_used()
        s, m = match_rect(p,m)
        shape.extend(s)

    p = check_pos(m,b.x,b.y-1,b.z)
    if p.id != 0:
        m[b.x][b.y - 1][b.z].to_used()
        s, m = match_rect(p,m)
        shape.extend(s)

    return shape, m

def check_pos(m,x,y,z):
    #check if inside matrix bounds
    #print(str(len(m)) + ' x: ' + str(x))
    #print(str(len(m[0])) + ' y: ' + str(y))
    #print(str(len(m[0][0])) + ' z: ' + str(z))
    if len(m) > x > -1  and len(m[0]) > y > -1 and len(m[0][0]) > z > -1:
        if(m[x][y][z].used):
            return Block(0, 0, x, y, z)
        else:
            return m[x][y][z]
    #otherwise return air
    else:
        return Block(0,0,x,y,z)

#SHAPE BUILDER

def build_shape(s,level,box):
    print("BUILD")
    print(s)
    #for y in xrange(box.maxy, box.miny - 1, -1):
    y = box.miny
    temp = level.blockAt(box.minx, y, box.maxz)
        #if temp != 0:
    for b in s:
        print("Block loc (" + str(b.x) + ', ' + str(b.y) + ', ' +str(b.z) + ')' )
        print("Place loc (" + str(box.minx + (b.x - box.minx)) + ', ' + str(y + (b.y - y)) + ', ' +str(box.minz + (b.z - box.minz)) + ')' )
        utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + b.x, y + b.y, box.minz + b.z)



