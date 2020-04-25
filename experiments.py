import sys
import os
import numpy as np

def overlap_experiment(exp,sep):
    if sep:
        for e in exp:
            print("EXAMPLE", e)
            __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__)))
            file_to_open = __location__ + "\evaluation\experiment%s.txt" % e
            with open(file_to_open) as f:

                nbshapes = []
                nbshapes_1 = []

                mean_size = []
                mean_size_1 = []

                median_size = []
                median_size_1 = []

                largest = []
                largest_1 = []

                smallest = []
                smallest_1 = []

                mean_complex = []
                mean_complex_1 = []

                median_complex = []
                median_complex_1 = []

                max_complex = []
                max_complex_1 = []

                min_complex = []
                min_complex_1 = []

                identical = []
                identical_1 = []

                time_spent = []
                time_spent_1 = []

                parse_file_2(e,"Overlap allowed",nbshapes, mean_size, median_size, largest, smallest,
                           mean_complex,median_complex, max_complex, min_complex, identical, time_spent,
                           nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                           median_complex_1,max_complex_1, min_complex_1, identical_1, time_spent_1)

                print("WITHOUT OVERLAP")
                print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                                max_complex, min_complex, identical, time_spent)

                print("WITH OVERLAP")
                print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                                median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)
    else:
        nbshapes = []
        nbshapes_1 = []

        mean_size = []
        mean_size_1 = []

        median_size = []
        median_size_1 = []

        largest = []
        largest_1 = []

        smallest = []
        smallest_1 = []

        mean_complex = []
        mean_complex_1 = []

        median_complex = []
        median_complex_1 = []

        max_complex = []
        max_complex_1 = []

        min_complex = []
        min_complex_1 = []

        identical = []
        identical_1 = []

        time_spent = []
        time_spent_1 = []

        for e in exp:
            parse_file_2(e, "Overlap allowed", nbshapes, mean_size, median_size, largest, smallest,
                         mean_complex, median_complex, max_complex, min_complex, identical, time_spent,
                         nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                         median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

        print("WITHOUT OVERLAP")
        print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                            max_complex, min_complex, identical, time_spent)

        print("WITH OVERLAP")
        print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                            median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)


def post_split_experiment(exp,sep):
    if sep:
        for e in exp:
            print("EXAMPLE", e)
            __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__)))
            file_to_open = __location__ + "\evaluation\experiment%s.txt" % e
            with open(file_to_open) as f:

                nbshapes = []
                nbshapes_1 = []

                mean_size = []
                mean_size_1 = []

                median_size = []
                median_size_1 = []

                largest = []
                largest_1 = []

                smallest = []
                smallest_1 = []

                mean_complex = []
                mean_complex_1 = []

                median_complex = []
                median_complex_1 = []

                max_complex = []
                max_complex_1 = []

                min_complex = []
                min_complex_1 = []

                identical = []
                identical_1 = []

                time_spent = []
                time_spent_1 = []

                parse_file_2(e,"Post split",nbshapes, mean_size, median_size, largest, smallest,
                           mean_complex,median_complex, max_complex, min_complex, identical, time_spent,
                           nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                           median_complex_1,max_complex_1, min_complex_1, identical_1, time_spent_1)

                print("WITHOUT POST SPLIT")
                print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                                max_complex, min_complex, identical, time_spent)

                print("WITH POST SPLIT")
                print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                                median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)
    else:
        nbshapes = []
        nbshapes_1 = []

        mean_size = []
        mean_size_1 = []

        median_size = []
        median_size_1 = []

        largest = []
        largest_1 = []

        smallest = []
        smallest_1 = []

        mean_complex = []
        mean_complex_1 = []

        median_complex = []
        median_complex_1 = []

        max_complex = []
        max_complex_1 = []

        min_complex = []
        min_complex_1 = []

        identical = []
        identical_1 = []

        time_spent = []
        time_spent_1 = []

        for e in exp:
            parse_file_2(e, "Post split", nbshapes, mean_size, median_size, largest, smallest,
                         mean_complex, median_complex, max_complex, min_complex, identical, time_spent,
                         nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                         median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

        print("WITHOUT POST SPLIT")
        print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                            max_complex, min_complex, identical, time_spent)

        print("WITH POST SPLIT")
        print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                            median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)


def representation_experiment(exp,sep):
    if sep:
        for e in exp:
            print("EXAMPLE", e)

            nbshapes = []
            nbshapes_1 = []
            nbshapes_2 = []

            mean_size = []
            mean_size_1 = []
            mean_size_2 = []

            median_size = []
            median_size_1 = []
            median_size_2 = []

            largest = []
            largest_1 = []
            largest_2 = []

            smallest = []
            smallest_1 = []
            smallest_2 = []

            mean_complex = []
            mean_complex_1 = []
            mean_complex_2 = []

            median_complex = []
            median_complex_1 = []
            median_complex_2 = []

            max_complex = []
            max_complex_1 = []
            max_complex_2 = []

            min_complex = []
            min_complex_1 = []
            min_complex_2 = []

            identical = []
            identical_1 = []
            identical_2 = []

            time_spent = []
            time_spent_1 = []
            time_spent_2 = []

            parse_file(e, "Rect(0), same plane(1) or 3D shapes(2)", nbshapes, mean_size, median_size, largest, smallest,
                       mean_complex,
                       median_complex, max_complex, min_complex, identical, time_spent,
                       nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                       median_complex_1,
                       max_complex_1, min_complex_1, identical_1, time_spent_1,
                       nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                       median_complex_2,
                       max_complex_2, min_complex_2, identical_2, time_spent_2)

            print("RECTANGLE REP AVERAGES")
            print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                                max_complex, min_complex, identical, time_spent)

            print("PLANAR REP AVERAGES")
            print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                                median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

            print("3D REP AVERAGES")
            print_basic_results(nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                                median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2)
    else:
        nbshapes = []
        nbshapes_1 = []
        nbshapes_2 = []

        mean_size = []
        mean_size_1 = []
        mean_size_2 = []

        median_size = []
        median_size_1 = []
        median_size_2 = []

        largest = []
        largest_1 = []
        largest_2 = []

        smallest = []
        smallest_1 = []
        smallest_2 = []

        mean_complex = []
        mean_complex_1 = []
        mean_complex_2 = []

        median_complex = []
        median_complex_1 = []
        median_complex_2 = []

        max_complex = []
        max_complex_1 = []
        max_complex_2 = []

        min_complex = []
        min_complex_1 = []
        min_complex_2 = []

        identical = []
        identical_1 = []
        identical_2 = []

        time_spent = []
        time_spent_1 = []
        time_spent_2 = []

        for e in exp:
            parse_file(e, "Rect(0), same plane(1) or 3D shapes(2)", nbshapes, mean_size, median_size, largest, smallest,
                       mean_complex,
                       median_complex, max_complex, min_complex, identical, time_spent,
                       nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1, median_complex_1,
                       max_complex_1, min_complex_1, identical_1, time_spent_1,
                       nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2, median_complex_2,
                       max_complex_2, min_complex_2, identical_2, time_spent_2)

        print("RECTANGLE REP AVERAGES")
        print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                            max_complex, min_complex, identical, time_spent)

        print("PLANAR REP AVERAGES")
        print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                            median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

        print("3D REP AVERAGES")
        print_basic_results(nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                            median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2)


def cost_experiment(exp,sep):
    if sep:
        for e in exp:
            print("EXAMPLE", e)

            nbshapes = []
            nbshapes_1 = []
            nbshapes_2 = []

            mean_size = []
            mean_size_1 = []
            mean_size_2 = []

            median_size = []
            median_size_1 = []
            median_size_2 = []

            largest = []
            largest_1 = []
            largest_2 = []

            smallest = []
            smallest_1 = []
            smallest_2 = []

            mean_complex = []
            mean_complex_1 = []
            mean_complex_2 = []

            median_complex = []
            median_complex_1 = []
            median_complex_2 = []

            max_complex = []
            max_complex_1 = []
            max_complex_2 = []

            min_complex = []
            min_complex_1 = []
            min_complex_2 = []

            identical = []
            identical_1 = []
            identical_2 = []

            time_spent = []
            time_spent_1 = []
            time_spent_2 = []

            parse_file(e, "Cost function", nbshapes, mean_size, median_size, largest, smallest,
                        mean_complex,
                        median_complex, max_complex, min_complex, identical, time_spent,
                        nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                        median_complex_1,
                        max_complex_1, min_complex_1, identical_1, time_spent_1,
                        nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                        median_complex_2,
                        max_complex_2, min_complex_2, identical_2, time_spent_2)

            print("COST 0 (BASIC COST) AVERAGES")
            print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                                    max_complex, min_complex, identical, time_spent)

            print("COST 1 (GROWS MORE FOR MORE TYPES) AVERAGES")
            print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                                    median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

            print("COST 2 (IDENTICAL DISCOUNT) AVERAGES")
            print_basic_results(nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                                    median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2)
    else:
        nbshapes = []
        nbshapes_1 = []
        nbshapes_2 = []

        mean_size = []
        mean_size_1 = []
        mean_size_2 = []

        median_size = []
        median_size_1 = []
        median_size_2 = []

        largest = []
        largest_1 = []
        largest_2 = []

        smallest = []
        smallest_1 = []
        smallest_2 = []

        mean_complex = []
        mean_complex_1 = []
        mean_complex_2 = []

        median_complex = []
        median_complex_1 = []
        median_complex_2 = []

        max_complex = []
        max_complex_1 = []
        max_complex_2 = []

        min_complex = []
        min_complex_1 = []
        min_complex_2 = []

        identical = []
        identical_1 = []
        identical_2 = []

        time_spent = []
        time_spent_1 = []
        time_spent_2 = []

        for e in exp:
            parse_file(e, "Cost function", nbshapes, mean_size, median_size, largest, smallest, mean_complex,
                       median_complex, max_complex, min_complex, identical, time_spent,
                       nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1, median_complex_1,
                       max_complex_1, min_complex_1, identical_1, time_spent_1,
                       nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2, median_complex_2,
                       max_complex_2, min_complex_2, identical_2, time_spent_2)

        print("COST 0 (BASIC COST) AVERAGES")
        print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                            max_complex, min_complex, identical, time_spent)

        print("COST 1 (GROWS MORE FOR MORE TYPES) AVERAGES")
        print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                            median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

        print("COST 2 (IDENTICAL DISCOUNT) AVERAGES")
        print_basic_results(nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                            median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2)


def operation_experiment(exp,sep):
    if sep:
        for e in exp:
            print("EXAMPLE", e)

            nbshapes = []
            nbshapes_1 = []
            nbshapes_2 = []

            mean_size = []
            mean_size_1 = []
            mean_size_2 = []

            median_size = []
            median_size_1 = []
            median_size_2 = []

            largest = []
            largest_1 = []
            largest_2 = []

            smallest = []
            smallest_1 = []
            smallest_2 = []

            mean_complex = []
            mean_complex_1 = []
            mean_complex_2 = []

            median_complex = []
            median_complex_1 = []
            median_complex_2 = []

            max_complex = []
            max_complex_1 = []
            max_complex_2 = []

            min_complex = []
            min_complex_1 = []
            min_complex_2 = []

            identical = []
            identical_1 = []
            identical_2 = []

            time_spent = []
            time_spent_1 = []
            time_spent_2 = []

            parse_file(e, "Merge(0), split(1) or both(2)", nbshapes, mean_size, median_size, largest, smallest,
                        mean_complex,
                        median_complex, max_complex, min_complex, identical, time_spent,
                        nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                        median_complex_1,
                        max_complex_1, min_complex_1, identical_1, time_spent_1,
                        nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                        median_complex_2,
                        max_complex_2, min_complex_2, identical_2, time_spent_2)

            print("OPERATION 0 (MERGE) AVERAGES")
            print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                                    max_complex, min_complex, identical, time_spent)

            print("OPERATION 1 (SPLIT) AVERAGES")
            print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                                    median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

            print("OPERATION 2 (BOTH) AVERAGES")
            print_basic_results(nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                                    median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2)
    else:
        nbshapes = []
        nbshapes_1 = []
        nbshapes_2 = []

        mean_size = []
        mean_size_1 = []
        mean_size_2 = []

        median_size = []
        median_size_1 = []
        median_size_2 = []

        largest = []
        largest_1 = []
        largest_2 = []

        smallest = []
        smallest_1 = []
        smallest_2 = []

        mean_complex = []
        mean_complex_1 = []
        mean_complex_2 = []

        median_complex = []
        median_complex_1 = []
        median_complex_2 = []

        max_complex = []
        max_complex_1 = []
        max_complex_2 = []

        min_complex = []
        min_complex_1 = []
        min_complex_2 = []

        identical = []
        identical_1 = []
        identical_2 = []

        time_spent = []
        time_spent_1 = []
        time_spent_2 = []

        for e in exp:
            parse_file(e, "Merge(0), split(1) or both(2)", nbshapes, mean_size, median_size, largest, smallest, mean_complex,
                       median_complex, max_complex, min_complex, identical, time_spent,
                       nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1, median_complex_1,
                       max_complex_1, min_complex_1, identical_1, time_spent_1,
                       nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2, median_complex_2,
                       max_complex_2, min_complex_2, identical_2, time_spent_2)

        print("OPERATION 0 (MERGE) AVERAGES")
        print_basic_results(nbshapes, mean_size, median_size,largest, smallest,mean_complex,median_complex,max_complex, min_complex,identical, time_spent)

        print("OPERATION 1 (SPLIT) AVERAGES")
        print_basic_results(nbshapes_1, mean_size_1, median_size_1,largest_1, smallest_1,mean_complex_1,median_complex_1,max_complex_1, min_complex_1,identical_1, time_spent_1)

        print("OPERATION 2 (BOTH) AVERAGES")
        print_basic_results(nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                            median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2)

def print_basic_results(nbshapes, mean_size, median_size,largest, smallest,mean_complex,median_complex,max_complex, min_complex,identical, time_spent):
    print("Avg nb shapes ", average(nbshapes))
    print("Median nb shapes ", median(nbshapes))
    print("Avg mean shape size ", average(mean_size))
    print("Median mean shape size ", median(mean_size))
    print("Avg median shape size ", average(median_size))
    print("Median median shape size ", median(median_size))
    print("Avg largest shape ", average(largest))
    print("Median largest shape ", median(largest))
    print("Avg smallest shape", average(smallest))
    print("Median smallest shape", median(smallest))
    print("Avg mean complexity ", average(mean_complex))
    print("Median mean complexity ", median(mean_complex))
    print("Avg median complexity ", average(median_complex))
    print("Median complexity ", median(median_complex))
    print("Avg max complexity ", average(max_complex))
    print("Median max complexity ", median(max_complex))
    print("Avg min complexity ", average(min_complex))
    print("Median min complexity ", median(min_complex))
    print("Avg identical shapes ", average(identical))
    print("Median identical shapes ", median(identical))
    i = 0
    copy = identical.copy()
    for n in nbshapes:
        copy[i] = copy[i] / n
        i += 1
    print("Avg identical percentage ", average(copy))
    print("Median identical percentage ", median(copy))
    print("Time spent ", average(time_spent))
    print("\n")

def parse_file(e,experiment_on,nbshapes, mean_size, median_size,largest, smallest,mean_complex,median_complex,max_complex, min_complex,identical, time_spent,
               nbshapes_1, mean_size_1, median_size_1,largest_1, smallest_1,mean_complex_1,median_complex_1,max_complex_1, min_complex_1,identical_1, time_spent_1,
               nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = __location__ + "\evaluation\experiment%s.txt" % e
    with open(file_to_open) as f:
        rep = 0
        for line in f:
            split = line.split(": ")
            if split[0] == experiment_on:
                if int(split[1]) == 0:
                    rep = 0
                    continue
                elif int(split[1]) == 1:
                    rep = 1
                    continue
                else:
                    rep = 2
                    continue
            if split[0] == "Number of shapes":
                if rep == 0:
                    nbshapes.append(int(split[1]))
                elif rep == 1:
                    nbshapes_1.append(int(split[1]))
                else:
                    nbshapes_2.append(int(split[1]))
            if split[0] == "Mean shape size":
                if rep == 0:
                    mean_size.append(float(split[1]))
                elif rep == 1:
                    mean_size_1.append(float(split[1]))
                else:
                    mean_size_2.append(float(split[1]))
            if split[0] == "Median shape size":
                if rep == 0:
                    median_size.append(float(split[1]))
                elif rep == 1:
                    median_size_1.append(float(split[1]))
                else:
                    median_size_2.append(float(split[1]))
            if split[0] == "Largest shape":
                if rep == 0:
                    largest.append(int(split[1]))
                elif rep == 1:
                    largest_1.append(int(split[1]))
                else:
                    largest_2.append(int(split[1]))
            if split[0] == "Smallest shape":
                if rep == 0:
                    smallest.append(int(split[1]))
                elif rep == 1:
                    smallest_1.append(int(split[1]))
                else:
                    smallest_2.append(int(split[1]))
            if split[0] == "Mean complexity":
                if rep == 0:
                    mean_complex.append(float(split[1]))
                elif rep == 1:
                    mean_complex_1.append(float(split[1]))
                else:
                    mean_complex_2.append(float(split[1]))
            if split[0] == "Median complexity":
                if rep == 0:
                    median_complex.append(float(split[1]))
                elif rep == 1:
                    median_complex_1.append(float(split[1]))
                else:
                    median_complex_2.append(float(split[1]))
            if split[0] == "Max complexity":
                if rep == 0:
                    max_complex.append(int(split[1]))
                elif rep == 1:
                    max_complex_1.append(int(split[1]))
                else:
                    max_complex_2.append(int(split[1]))
            if split[0] == "Min complexity":
                if rep == 0:
                    min_complex.append(int(split[1]))
                elif rep == 1:
                    min_complex_1.append(int(split[1]))
                else:
                    min_complex_2.append(int(split[1]))
            if split[0] == "Number of 'redundant' identical shapes":
                if rep == 0:
                    identical.append(int(split[1]))
                elif rep == 1:
                    identical_1.append(int(split[1]))
                else:
                    identical_2.append(int(split[1]))
            if split[0] == "Time spent":
                if rep == 0:
                    time_spent.append(float(split[1]))
                elif rep == 1:
                    time_spent_1.append(float(split[1]))
                else:
                    time_spent_2.append(float(split[1]))


def parse_file_2(e, experiment_on,nbshapes, mean_size, median_size,largest, smallest,mean_complex,median_complex,max_complex, min_complex,identical, time_spent,
               nbshapes_1, mean_size_1, median_size_1,largest_1, smallest_1,mean_complex_1,median_complex_1,max_complex_1, min_complex_1,identical_1, time_spent_1):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = __location__ + "\evaluation\experiment%s.txt" % e
    with open(file_to_open) as f:
        rep = False
        for line in f:
            split = line.split(": ")
            if split[0] == experiment_on:
                if split[1] == 'False\n':
                    rep = False
                    continue
                else:
                    rep = True
                    continue
            if split[0] == "Number of shapes":
                if not rep:
                    nbshapes.append(int(split[1]))
                else:
                    nbshapes_1.append(int(split[1]))
            if split[0] == "Mean shape size":
                if not rep:
                    mean_size.append(float(split[1]))
                else:
                    mean_size_1.append(float(split[1]))
            if split[0] == "Median shape size":
                if not rep:
                    median_size.append(float(split[1]))
                else:
                    median_size_1.append(float(split[1]))
            if split[0] == "Largest shape":
                if not rep:
                    largest.append(int(split[1]))
                else:
                    largest_1.append(int(split[1]))
            if split[0] == "Smallest shape":
                if not rep:
                    smallest.append(int(split[1]))
                else:
                    smallest_1.append(int(split[1]))
            if split[0] == "Mean complexity":
                if not rep:
                    mean_complex.append(float(split[1]))
                else:
                    mean_complex_1.append(float(split[1]))
            if split[0] == "Median complexity":
                if not rep:
                    median_complex.append(float(split[1]))
                else:
                    median_complex_1.append(float(split[1]))
            if split[0] == "Max complexity":
                if not rep:
                    max_complex.append(int(split[1]))
                else:
                    max_complex_1.append(int(split[1]))
            if split[0] == "Min complexity":
                if not rep:
                    min_complex.append(int(split[1]))
                else:
                    min_complex_1.append(int(split[1]))
            if split[0] == "Number of 'redundant' identical shapes":
                if not rep:
                    identical.append(int(split[1]))
                else:
                    identical_1.append(int(split[1]))
            if split[0] == "Time spent":
                if not rep:
                    time_spent.append(float(split[1]))
                else:
                    time_spent_1.append(float(split[1]))

def average(lst):
    return sum(lst)/len(lst)

def median(lst):
    return np.median(lst)

def main():
    #overlap_experiment([0,1,2],True)
    post_split_experiment([0,1,2],True)
    #representation_experiment([0,1,2],False)
    #cost_experiment([0,1,2], True)
    #operation_experiment([0,1,2],True)

if __name__ == "__main__":
    main()

