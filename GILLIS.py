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

class Block:
	def __init__(self, blockid, dmg):
		self.id = blockid
		self.dmg = dmg

#blockid and dmg pairs

plank_set = [Block(5,0),Block(5,1),Block(5,2),Block(5,3),Block(5,4),Block(5,5)]
log_set = [Block(17,0),Block(17,1),Block(17,2),Block(17,3),Block(162,0),Block(162,1)]
stair_set = [Block(163,0),Block(164,0),Block(53,0),Block(67,0),Block(108,0),Block(109,0),Block(114,0),Block(128,0),
			 Block(134,0),Block(135,0),Block(136,0),Block(156,0),Block(180,0),Block(103,0)]
fence_set = [Block(85,0),Block(101,0),Block(113,0),Block(188,0),Block(189,0),Block(190,0),Block(191,0),Block(192,0)]
furniture_set = [Block(26,0),Block(30,0),Block(47,0),Block(54,0),Block(58,0),Block(61,0),Block(84,0),Block(92,0),
				 Block(116,0),Block(117,0),Block(118,0),Block(130,0),Block(145,0),Block(321,0),]
carpet_set = [Block(171,0),Block(171,1),Block(171,2),Block(171,3),Block(171,4),Block(171,5),Block(171,6),Block(171,7),Block(171,8),
				Block(171,9),Block(171,10),Block(171,11),Block(171,12),Block(171,13),Block(171,14),Block(171,15)]
light_set = [Block(50,0,)Block(123,0),Block(89,0)]
flower_set = [Block(37,0),Block(38,0),Block(38,1),Block(38,2),Block(38,3),Block(38,4),Block(38,5),Block(38,6),Block(38,7),Block(38,8)]
double_flower_set = [Block(175,0),Block(175,1),Block(175,2),Block(175,3),Block(175,4),Block(175,5)]
slab_set = [Block(44,0),Block(44,1),Block(44,2),Block(44,3),Block(44,4),Block(44,5),Block(44,6),Block(44,7),
			Block(126,0),Block(126,1),Block(126,2),Block(126,3),Block(126,4),Block(126,5),Block(182,0),Block(205,0)]
door_set = [Block(64,0),Block(71,0),Block(107,0),Block(183,0),Block(184,0),Block(185,0),Block(186,0),Block(187,0),
            Block(193,0),Block(194,0),Block(195,0),Block(196,0),Block(197,0)]
corner_set = []
wall_set = [Block(1,0),Block(1,1),Block(1,2),Block(1,3),Block(1,4),Block(1,5),Block(1,6),Block(4,0),Block(5,0),Block(5,1),Block(5,2),Block(5,3),Block(5,4),Block(5,5),Block(17,0),Block(17,1),
            Block(17,2),Block(17,3),Block(24,0),Block(24,1),Block(24,2),Block(35,0),Block(35,1),Block(35,2),Block(35,3),Block(35,4),Block(35,5),Block(35,6),Block(35,7),Block(35,8),
            Block(35,9),Block(35,10),Block(35,11),Block(35,12),Block(35,13),Block(35,14),Block(35,15),Block(41,0),Block(42,0),Block(45,0),Block(48,0),Block(49,0),Block(57,0),
            Block(80,0),Block(87,0),Block(98,0),Block(98,1),Block(98,2),Block(98,3),Block(99,0),Block(100,0),Block(112,0),Block(133,0),Block(152,0),Block(155,0),Block(155,1),
            Block(155,2),Block(159,0),Block(159,1),Block(159,2),Block(159,3),Block(159,4),Block(159,5),Block(159,6),Block(159,7),Block(159,8),Block(159,9),Block(159,10),
            Block(159,11),Block(159,12),Block(159,13),Block(159,14),Block(159,15),Block(162,0),Block(162,1),Block(168,0),Block(168,1),Block(168,2),Block(170,0),Block(172,0),
            Block(173,0),Block(179,0),Block(179,1),Block(179,2),Block(201,0),Block(202,0),Block(206,0),Block(214,0),Block(215,0),Block(216,0)]

window_set =  [Block(20,0),Block(79,0),Block(85,0),Block(95,0),Block(95,1),Block(95,2),Block(95,3),Block(95,4),Block(95,5),Block(95,6),Block(95,7),Block(95,8),Block(95,9),
              Block(95,10),Block(95,11),Block(95,12),Block(95,13),Block(95,14),Block(95,15),Block(101,0),Block(102,0),Block(113,0),Block(139,0),Block(139,1),
              Block(160,0),Block(160,1),Block(160,2),Block(160,3),Block(160,4),Block(160,5),Block(160,6),Block(160,7),Block(160,8),Block(160,9),Block(160,10),
              Block(160,11),Block(160,12),Block(160,13),Block(160,14),Block(160,15),Block(174,0),Block(188,0),Block(189,0),Block(190,0),Block(191,0),Block(192,0)]

cb = random.choice(wall_set)
wb = random.choice(wall_set)
wib = random.choice(window_set)
db = random.choice(door_set)

def rewrite_at(index, replacements, the_list):
	del the_list[index]
	the_list[index:index] = replacements

def generate_sentence(grammar):
	sentence_list = [grammar.start()]
	all_terminals = False
	while not all_terminals:
		all_terminals = True
		for position, symbol in enumerate(sentence_list):
			if symbol in grammar._lhs_index:
				all_terminals = False
				derivations = grammar._lhs_index[symbol]
				derivation = weighted_choice(derivations) # or weighted_choice(derivations) if you have a function for that
				rewrite_at(position, derivation.rhs(), sentence_list)
	return sentence_list

#Choose a derivation depending on the probabilities of the grammar
def weighted_choice(derivations):
	r = random.uniform(0, 1)
	t = 0
	for der in derivations:
		t = t + der.prob()
		if t > r:
			return der
			
def search(grammar,con):
	f = False
	while f==False:
		s = generate_sentence(grammar)
		if check_constraints(s,con) == True:
			return s
			
def check_constraints(s,con):
	for c in con:
		if c[0] == "l":
			if length_constraint(s,int(c[1:])) == False:
				return False
		elif c[0] == "d":
			if door_constraint(s,1) == False:
				return False
	return True

#Checks a sentence length constraint
def length_constraint(s,l):
	if len(s) == l:
		return True
	else:
		return False

#Checks a door constraint 	
def door_constraint(s,a):
	if s.count('door') < a+1:
		return True
	else:
		return False

grammar = PCFG.fromstring("""
    S -> C B A [1.0]
    A -> B A [0.9] | C [0.1]
    B -> 'wall' [0.6] | 'window' [0.2] | 'door' [0.2]
    C -> 'corner' [1.0]
""")

print('A Grammar:', grammar)
print('grammar.start()   =>', grammar.start())
print('grammar.productions() =>')
print(grammar.productions())

#inputs are taken from the user. Here I've just showing labels, as well as letting the user define
# what the main creation material for the structures is
inputs = (
	("Gillis Test", "label"),
	("Material", alphaMaterials.Cobblestone), # the material we want to use to build the mass of the structures
	("Creator: Gillis Hermans", "label"),
	)


# MAIN SECTION #
# Every agent must have a "perform" function, which has three parameters
# 1: the level (aka the minecraft world). 2: the selected box from mcedit. 3: User defined inputs from mcedit
def perform(level, box, options):
	buildWall(level,box,options)

#Build a wall
def buildWall(level, box, options):

	#Generate a wall sentence out of the grammar
	y = "d"
	con = [y]
	frags = search(grammar,con)#generate_sentence(grammar)
	print( ' '.join(frags) )

	#Build the wall (2 levels) on the ground
	for i in range(0,len(frags)):
		for y in xrange(box.maxy, box.miny-1, -1):
				# get this block
				tempBlock = level.blockAt(box.minx + i, y, box.maxz)
				if tempBlock != 0:
					b = chooseBlock(frags[i])
					utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + i, y+1, box.maxz)
					utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + i, y+2, box.maxz)
					break;
					
	#Generate a wall sentence out of the grammar
	y = "d"
	con = [y]
	frags1 = search(grammar,con)#generate_sentence(grammar)
	print( ' '.join(frags1) )
	
	#Build the second wall (2 levels) on the ground (leave out first corner)
	for i in range(1,len(frags1)):
		for y in xrange(box.maxy, box.miny-1, -1):
				# get this block
				tempBlock = level.blockAt(box.minx + len(frags)-1, y, box.maxz +i)
				if tempBlock != 0:
					b = chooseBlock(frags1[i])
					utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + len(frags)-1, y+1, box.maxz + i)
					utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + len(frags)-1, y+2, box.maxz + i)
					break;
					
	#Generate a wall sentence out of the grammar
	x = "l"+str(len(frags))
	y = "d"
	con = [x,y]
	frags2 = search(grammar,con)#generate_sentence(grammar)
	print( ' '.join(frags2) )
					
	#Build the second wall (2 levels) on the ground (leave out first corner)
	
	for i in range(1,len(frags2)-1): #range(0,min(len(frags2),len(frags))):
		for y in xrange(box.maxy, box.miny-1, -1):
				# get this block
				tempBlock = level.blockAt(box.minx + i, y, box.maxz + len(frags1)-1)
				if tempBlock != 0:
					b = chooseBlock(frags2[i])
					utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + i, y+1, box.maxz + len(frags1)-1)
					utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx + i, y+2, box.maxz + len(frags1)-1)
					break;

	#Generate a wall sentence out of the grammar
	x = "l"+str(len(frags1))
	y = "d"
	con = [x,y]
	con = [x]
	frags3 = search(grammar,con)#generate_sentence(grammar)
	print( ' '.join(frags3) )
					
	#Build the second wall (2 levels) on the ground (leave out first corner)
	
	for i in range(1,len(frags3)):
		for y in xrange(box.maxy, box.miny-1, -1):
				# get this block
				tempBlock = level.blockAt(box.minx, y, box.maxz +i)
				if tempBlock != 0:
					b = chooseBlock(frags3[i])
					utilityFunctions.setBlock(level, (b.id,b.dmg), box.minx, y+1, box.maxz + i)
					utilityFunctions.setBlock(level, (b.id, b.dmg), box.minx, y+2, box.maxz + i)
					break;                 

def chooseBlockProb(prob):
	r = random.uniform(0,1)
	for b in prob:
		if (b[1]/nb) > r:
			return b[0]

def chooseBlock(str):
	if str == 'corner':
		return cb
	if str == 'wall':
		return wb
	if str == 'window':
		return wib
	if str == 'door':
		return db


#Future blocks - Concrete - Block(251,0),Block(251,1),Block(251,2),Block(251,3),Block(251,4),Block(251,5),Block(251,6),Block(251,7),Block(251,8),Block(251,9),Block(251,10),Block(251,11),Block(251,12),Block(251,13),Block(251,14),Block(251,15)
#                Terra Cotta - Block(235,0),Block(236,0),Block(237,0),Block(238,0),Block(239,0),Block(240,0),Block(241,0),Block(242,0),Block(243,0),Block(244,0),Block(245,0),Block(246,0),Block(247,0),Block(248,0),Block(249,0),Block(250,0)



