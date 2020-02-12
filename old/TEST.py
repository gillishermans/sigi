# This filter procedurally generates 4 structures within the selection box within defined limits
# This filter: mcgreentn@gmail.com (mikecgreen.com)

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
    r = random.uniform(0, 1);
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
    B -> 'wall' [0.6]|'window' [0.2]|'door' [0.2]
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
					newValue = 0
					utilityFunctions.setBlock(level, (chooseBlock(frags[i]), newValue), box.minx + i, y+1, box.maxz)
					utilityFunctions.setBlock(level, (chooseBlock(frags[i]), newValue), box.minx + i, y+2, box.maxz)
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
					newValue = 0
					utilityFunctions.setBlock(level, (chooseBlock(frags1[i]), newValue), box.minx + len(frags)-1, y+1, box.maxz + i)
					utilityFunctions.setBlock(level, (chooseBlock(frags1[i]), newValue), box.minx + len(frags)-1, y+2, box.maxz + i)
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
					newValue = 0
					utilityFunctions.setBlock(level, (chooseBlock(frags2[i]), newValue), box.minx + i, y+1, box.maxz + len(frags1)-1)
					utilityFunctions.setBlock(level, (chooseBlock(frags2[i]), newValue), box.minx + i, y+2, box.maxz + len(frags1)-1)
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
					newValue = 0
					utilityFunctions.setBlock(level, (chooseBlock(frags3[i]), newValue), box.minx, y+1, box.maxz + i)
					utilityFunctions.setBlock(level, (chooseBlock(frags3[i]), newValue), box.minx, y+2, box.maxz + i)
					break;  					

def chooseBlock(str):
	if str == 'corner': return 17
	if str == 'wall': return 5
	if str == 'window': return 20
	if str == 'door': return 64






