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
import in_out as io

inputs = (
    ("Shape grammar induction and production", "label"),
    ("Creator: Gillis Hermans", "label")
)

def perform(level, box, options):
    evaluate_alpha(level,box,options)


def evaluate_alpha(level,box,options):
    m = io.scan_structure(level, box, options)
    initial = io.initial_shapes(m)
    av = [0.5,1.0,1.5]#[0.0,0.25,0.5,0.75,1.0,1.1,1.25,1.5,1.75,2,5,10]

    example = 1
    file_nb = 0
    for rect in [0]:
        for operation in [0,1,2]:
            for cost in [0,1]:
                for overlap in [True,False]:
                    for post_split in [False, True]:
                        write_experiment(file_nb, example, rect, operation, cost, overlap)
                        alpha_experiment(initial, av, rect, operation, cost, overlap, post_split, m, file_nb)
                        file_nb += 1


def alpha_experiment(initial, alpha_list, rect, operation, cost, overlap, post_split, m, file_nb):
    for alpha in alpha_list:
        tic = timeit.default_timer()
        shapes = shp.hill_climbing(initial, rect, operation, cost, alpha, m)
        if overlap:
            shapes = shp.filter_final_shapes_overlap(shapes, m)
        else:
            shapes = shp.filter_final_shapes_no_overlap(shapes)
        if post_split:
            shapes = shp.post_plane_split(shapes, 'xz')
            shapes = shp.post_plane_split(shapes, 'xy')
            shapes = shp.post_plane_split(shapes, 'zy')
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

