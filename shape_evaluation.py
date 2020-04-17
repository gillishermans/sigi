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
    ("Evaluate procedural models.", "label"),
    ("Creator: Gillis Hermans", "label"),
    ("Example number: ", 0),
    ("Restart: ", True),
    ("Rect start: ", 0),
    ("Operation start: ", 0),
    ("Cost start: ", 0),
    ("Overlap start: ", True),
    ("Post split start: ", True)
)

def perform(level, box, options):
    evaluate_alpha(level,box,options)


#Evaluate different algorithms for a set of alpha values.
def evaluate_alpha(level,box,options):
    tic = timeit.default_timer()
    m = io.scan_structure(level, box)
    av = [0.0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2,5,10,100]

    file_nb = options["Example number: "]
    write_example(file_nb, options["Restart: "])

    e = 0
    for rect in [0,1,2]:
        if options["Rect start: "] < rect:
            print("skip rect")
            continue
        initial = io.initial_shapes(m, rect)
        for operation in [0,1,2]:
            if options["Operation start: "] < operation:
                print("skip op")
                continue
            for cost in [0,1,2]:
                if options["Cost start: "] < cost:
                    print("skip cost")
                    continue
                for overlap in [True,False]:
                    if options["Overlap start: "] == False and overlap == True:
                        print("skip overlap")
                        continue
                    for post_split in [False, True]:
                        if options["Post split start: "] == True and overlap == False:
                            print("skip post split")
                            continue
                        write_experiment(file_nb, rect, operation, cost, overlap, post_split)
                        alpha_experiment(initial, av, rect, operation, cost, overlap, post_split, m, file_nb)
                        e += 1
                        print("Progress: " + str(e/(108*len(av))))
    toc = timeit.default_timer()
    print("TIME")
    print(toc - tic)
    #file_nb += 1


#Perform an experiment for a certain algorithm and a number of alpha values.
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
        mean_size = np.mean(sizes)
        mean_complex = np.mean(complexity)
        median_size = np.median(sizes)
        median_complex = np.median(complexity)

        duplicate_list = shp.get_duplicate_shapes(shapes)
        identical = 0
        for d in duplicate_list:
            identical += len(d) -1

        time_spent = (toc - tic)
        write_alpha_experiment(file_nb,alpha,len(shapes),mean_size,median_size,max_size,min_size,mean_complex,median_complex,max_complex,min_complex,identical,time_spent)

def write_example(file_nb, restart):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = __location__ + "\evaluation\experiment%s.txt" % file_nb
    if restart:
        file = open(file_to_open, "w")
    else:
        file = open(file_to_open, "a")
    file.write("Example number: " + str(file_nb))
    file.write("\n")
    file.close()

#Write the initial specifications of an experiment to disk.
def write_experiment(file_nb, rect, operation, cost, overlap, post_split):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = __location__ + "\evaluation\experiment%s.txt" % file_nb
    file = open(file_to_open, "a")
    file.write("Rect(0), same plane(1) or 3D shapes(2): " + str(rect) +"\n")
    file.write("Merge(0), split(1) or both(2): " + str(operation) +"\n")
    file.write("Cost function: " + str(cost) +"\n")
    file.write("Overlap allowed: " + str(overlap) +"\n")
    file.write("Post split: " + str(post_split) +"\n")
    file.write("\n")
    file.close()


#Write the results of an experiment to disk.
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

