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

	def __float__(self):
		return float(self.id + float(self.dmg) / 100)
	def __repr__(self):
		return str(self)

	def __str__(self):
		return '('+str(self.id)+', '+str(self.dmg)+') at ('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'

inputs = (
	("Extract Data", "label"),
	("Creator: Gillis Hermans", "label"),
	)

def perform(level, box, options):
	print("EXTRACT")
	m = scanStructure(level,box,options)
	print(m)
	print(get_adjacent_cells(level,m,0,0,0))
	#print(get_adjacent_cells(m, 2, 2, 0))

def addBlock(nb,prob,blockid,dmg):
	for b in prob:
		if b[0] == blockid and b[3] == dmg:
			b[1] = b[1]+1.0
			b[2] = b[1]/nb
			return
	prob.append([blockid,1.0,1.0/nb,dmg])

def writeToFile(prob):
	__location__ = os.path.realpath(
		os.path.join(os.getcwd(), os.path.dirname(__file__)))
	file_to_open = os.path.join(__location__, 'g_data.txt')
	file = open(file_to_open,"w")
	for p in prob:
		print(str(p[0]) + " " + str(p[3]) + " " + str(p[2]) + "\n")
		file.write(str(p[0])+" "+str(p[3])+" "+str(p[2])+"\n")
	file.close()

def scanStructure(level,box,options):
	nb=0
	prob=[]
	m = np.zeros((box.maxx-box.minx,box.maxy-box.miny,box.maxz-box.minz))
	print(m.size)

	for x in range(box.minx,box.maxx):
		for y in range(box.miny,box.maxy):
			for z in range(box.minz,box.maxz):
				blockid = level.blockAt(x,y,z)
				dmg = level.blockDataAt(x,y,z)
				m[x-box.minx][y-box.miny][z-box.minz] = Block(blockid,dmg,x,y,z)
				if blockid != 0 and blockid != 2 and blockid != 3:
					nb = nb+1
					addBlock(nb,prob,blockid,dmg)
	writeToFile(prob)
	return m


def scanForWalls(level,box,options,m):
	#a = np.zeros(m.size,m.size)
	w = []
	for x in range(box.minx,box.maxx):
		for y in range(box.miny,box.maxy):
			for z in range(box.minz,box.maxz):
				b = Block(level.blockAt(x,y,z),level.blockDataAt(x,y,z),x,y,z)
				if b.id == 0:
					break
				if w.__len__() == 0:
					w.append(b)
				#if w[-1]

def adjacent(a,b):
	#if a.x == b.x and a.y == b.y and a.z ==
	print('lel')

def get_adjacent_cells(level,m,x_coord, y_coord, z_coord):
	res = []
	result = {}
	print("og")
	print(m[x_coord][y_coord][z_coord])
	for x, y, z in [(x_coord + i, y_coord + j,z_coord + k) for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1,0,1)]:
		#in the matrix
		if x>-1 and x<len(m) and y>-1 and y<len(m[0]) and z>-1 and z<len(m[0][0]):
			#direct neighbours?
			if x+y+z == 1:
				result[(x, y, z)] = m[x][y][z]
				res.append(Block(m[x][y][z],level.blockDataAt(x,y,z),x,y,z))
	return result

def direction_scan(m):
	wall = []





