import time # for timing
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
from random import *
from numpy import *
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from nltk import CFG, PCFG, ProbabilisticProduction, Nonterminal
from nltk.parse.generate import generate
import random
import utilityFunctions as utilityFunctions

#inputs are taken from the user. Here I've just showing labels, as well as letting the user define
# what the main creation material for the structures is
inputs = (
	("Gillis Extract Data", "label"),
	("Creator: Gillis Hermans", "label"),
	)

# MAIN SECTION #
# Every agent must have a "perform" function, which has three parameters
# 1: the level (aka the minecraft world). 2: the selected box from mcedit. 3: User defined inputs from mcedit
def perform(level, box, options):
	prob = scanStructure(level,box,options)

def addBlock(nb,prob,blockid,dmg):
	for b in prob:
		if b[0] == blockid and b[3] == dmg:
			b[1] = b[1]+1.0
			b[2] = b[1]/nb
			return
	prob.append([blockid,1.0,1.0/nb,dmg])

def writeToFile(prob):
	file = open("C:/Users/Gilli/GDMC/stock-filters/thesis_filters/thesis_filters/g_data.txt","w")
	print(" ".join(str(x) for x in prob))
	for p in prob:
		file.write(str(p[0])+" "+str(p[3])+" "+str(p[2])+"\n")
	file.close()

def scanStructure(level,box,options):
	nb=0
	prob=[]

	for x in range(box.minx,box.maxx):
		for y in range(box.miny,box.maxy):
			for z in range(box.minz,box.maxz):
				blockid = level.blockAt(x,y,z)
				dmg = level.blockDataAt(x,y,z)
				if blockid != 0 and blockid != 2 and blockid != 3:
					nb = nb+1
					addBlock(nb,prob,blockid,dmg)
	writeToFile(prob)









