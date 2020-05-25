import sys
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def overlap_experiment(exp,sep):
    if sep:
        for e in exp:
            print("EXAMPLE", e)
            __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__)))
            file_to_open = __location__ + "\evaluation\done\experiment%s.txt" % e
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

                #plot_identical_percentage(nbshapes, nbshapes_1, identical, identical_1)
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

        #plot_identical_percentage(nbshapes, nbshapes_1, identical, identical_1)

def post_split_sizes_experiment(exp,sep):
    if sep:
        for e in exp:
            print("EXAMPLE", e)
            __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__)))
            file_to_open = __location__ + "\evaluation\done\experiment%s.txt" % e
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

                parse_file_2(e, "Post split", nbshapes, mean_size, median_size, largest, smallest,
                             mean_complex, median_complex, max_complex, min_complex, identical, time_spent,
                             nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                             median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

                print("mean_size", mean_size)
                print("median_size", median_size)

                print("WITHOUT POST SPLIT")
                print_size_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                                    max_complex, min_complex, identical, time_spent)

                print("WITH POST SPLIT")
                print_size_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
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
        print_size_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                            max_complex, min_complex, identical, time_spent)

        print("WITH POST SPLIT")
        print_size_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                            median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

def post_split_experiment(exp,sep):
    if sep:
        for e in exp:
            print("EXAMPLE", e)
            __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__)))
            file_to_open = __location__ + "\evaluation\done\experiment%s.txt" % e
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

            new_identical = []
            new_identical_1 = []
            new_identical_2 = []
            new_nbshapes = []
            new_nbshapes_1 = []
            new_nbshapes_2 = []
            i = 0
            #print(largest_2)
            #print(mean_size_2)
            for l in mean_size_2:
                if l >= 1.5:
                    new_identical.append(identical[i])
                    new_identical_1.append(identical_1[i])
                    new_identical_2.append(identical_2[i])
                    new_nbshapes.append(nbshapes[i])
                    new_nbshapes_1.append(nbshapes_1[i])
                    new_nbshapes_2.append(nbshapes_2[i])
                i += 1


            print("COST 0 (BASIC COST) AVERAGES")
            print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                                    max_complex, min_complex, identical, time_spent)

            i = 0
            copy = new_identical.copy()
            for n in new_nbshapes:
                copy[i] = copy[i] / n
                i += 1
            print("Removed largest 1 Avg identical percentage ", average(copy))
            print("Removed largest 1 Median identical percentage ", median(copy))
            print("Removed largest 1 Avg number of shapes", average(new_nbshapes))
            print(len(new_nbshapes))

            print("COST 1 (GROWS MORE FOR MORE TYPES) AVERAGES")
            print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                                    median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

            i = 0
            copy = new_identical_1.copy()
            for n in new_nbshapes_1:
                copy[i] = copy[i] / n
                i += 1
            print("Removed largest 1 Avg identical percentage ", average(copy))
            print("Removed largest 1 Median identical percentage ", median(copy))
            print("Removed largest 1 Avg number of shapes", average(new_nbshapes_1))

            print("COST 2 (IDENTICAL DISCOUNT) AVERAGES")
            print_basic_results(nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,
                                    median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2)

            i = 0
            copy = new_identical_2.copy()
            for n in new_nbshapes_2:
                copy[i] = copy[i] / n
                i += 1
            print("Removed largest 1 Avg identical percentage ", average(copy))
            print("Removed largest 1 Median identical percentage ", median(copy))
            print("Removed largest 1 Avg number of shapes", average(new_nbshapes_2))
            print(len(new_nbshapes_2))
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

        #mean_complex / mean_size
        #copy = mean_size.copy()
        #i=0
        #for c in mean_complex:
        #    copy[i] = c / copy[i]
        #    i += 1
        #print(copy)
        #print("avg complex/size",average(copy))

        print("COST 1 (GROWS MORE FOR MORE TYPES) AVERAGES")
        print_basic_results(nbshapes_1, mean_size_1, median_size_1, largest_1, smallest_1, mean_complex_1,
                            median_complex_1, max_complex_1, min_complex_1, identical_1, time_spent_1)

        #copy = mean_size_1.copy()
        #i = 0
        #for c in mean_complex_1:
        #    copy[i] = c / copy[i]
        #    i += 1
        #print(copy)
        #print("avg complex/size",average(copy))

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

def alpha_experiment(exp,sep):
    av = [0.0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2,5,10,100]
    if sep:
        nb_shapes = []
        complexity = []
        for e in exp:
            print("EXAMPLE", e)
            for alpha in av:
                nb_shap, complex = single_alpha_experiment(e,alpha)
                nb_shapes.append(average(nb_shap))
                complexity.append(average(complex))
        return nb_shapes, complexity
    else:
        print("NOT SEPARATE")
        for alpha in av:
            multiple_alpha_experiment(exp,alpha)

def single_alpha_experiment(e,alpha):
    nbshapes = []

    mean_size = []

    median_size = []

    largest = []

    smallest = []

    mean_complex = []

    median_complex = []

    max_complex = []

    min_complex = []

    identical = []

    time_spent = []

    parse_file_3(e, "Alpha", alpha, nbshapes, mean_size, median_size, largest, smallest,
               mean_complex,
               median_complex, max_complex, min_complex, identical, time_spent)

    print("ALPHA", alpha)
    print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                        max_complex, min_complex, identical, time_spent)
    return nbshapes, mean_complex

def multiple_alpha_experiment(ex,alpha):
    nbshapes = []

    mean_size = []

    median_size = []

    largest = []

    smallest = []

    mean_complex = []

    median_complex = []

    max_complex = []

    min_complex = []

    identical = []

    time_spent = []

    for e in ex:
        parse_file_3(e, "Alpha", alpha, nbshapes, mean_size, median_size, largest, smallest,
                mean_complex,
                median_complex, max_complex, min_complex, identical, time_spent)

    print("ALPHA", alpha)
    print_basic_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                        max_complex, min_complex, identical, time_spent)
    return nbshapes, mean_complex

def parse_file(e,experiment_on,nbshapes, mean_size, median_size,largest, smallest,mean_complex,median_complex,max_complex, min_complex,identical, time_spent,
               nbshapes_1, mean_size_1, median_size_1,largest_1, smallest_1,mean_complex_1,median_complex_1,max_complex_1, min_complex_1,identical_1, time_spent_1,
               nbshapes_2, mean_size_2, median_size_2, largest_2, smallest_2, mean_complex_2,median_complex_2, max_complex_2, min_complex_2, identical_2, time_spent_2):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = __location__ + "\evaluation\done\experiment%s.txt" % e
    with open(file_to_open) as f:
        rep = 0
        skip = False
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
            #if split[0] == "Rect(0), same plane(1) or 3D shapes(2)":
            if split[0] == "Cost function":
            #if split[0] == "Merge(0), split(1) or both(2)":
                if int(split[1]) == 2:
                    skip = True
                else:
                    skip = False
            if skip:
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
    file_to_open = __location__ + "\evaluation\done\experiment%s.txt" % e
    skip = False
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
            #if split[0] == "Rect(0), same plane(1) or 3D shapes(2)":
            #if split[0] == "Cost function":
            if split[0] == "Merge(0), split(1) or both(2)":
                if int(split[1]) != 1:
                    skip = True
                else:
                    skip = False
            if skip:
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

def parse_file_3(e, experiment_on, alpha, nbshapes, mean_size, median_size,largest, smallest,mean_complex,median_complex,max_complex, min_complex,identical, time_spent):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_to_open = __location__ + "\evaluation\done\experiment%s.txt" % e
    with open(file_to_open) as f:
        rep = False
        for line in f:
            split = line.split(": ")
            if split[0] == experiment_on:
                if float(split[1]) == alpha:
                    rep = False
                    continue
                else:
                    rep = True
                    continue
            if split[0] == "Number of shapes":
                if not rep:
                    nbshapes.append(int(split[1]))
            if split[0] == "Mean shape size":
                if not rep:
                    mean_size.append(float(split[1]))
            if split[0] == "Median shape size":
                if not rep:
                    median_size.append(float(split[1]))
            if split[0] == "Largest shape":
                if not rep:
                    largest.append(int(split[1]))
            if split[0] == "Smallest shape":
                if not rep:
                    smallest.append(int(split[1]))
            if split[0] == "Mean complexity":
                if not rep:
                    mean_complex.append(float(split[1]))
            if split[0] == "Median complexity":
                if not rep:
                    median_complex.append(float(split[1]))
            if split[0] == "Max complexity":
                if not rep:
                    max_complex.append(int(split[1]))
            if split[0] == "Min complexity":
                if not rep:
                    min_complex.append(int(split[1]))
            if split[0] == "Number of 'redundant' identical shapes":
                if not rep:
                    identical.append(int(split[1]))
            if split[0] == "Time spent":
                if not rep:
                    time_spent.append(float(split[1]))

def print_size_results(nbshapes, mean_size, median_size, largest, smallest, mean_complex, median_complex,
                                    max_complex, min_complex, identical, time_spent):
    #med > 3
    nbshapes_a = []
    mean_size_a = []
    identical_a = []
    mean_complex_a = []

    #med > 10
    nbshapes_b = []
    mean_size_b = []
    identical_b = []
    mean_complex_b = []

    #med <= 10
    nbshapes_c = []
    mean_size_c = []
    identical_c = []
    mean_complex_c = []

    i = 0
    for ms in median_size:
        if ms < 3:
            nbshapes_a.append(nbshapes[i])
            mean_size_a.append(mean_size[i])
            identical_a.append(identical[i])
            mean_complex_a.append(mean_complex[i])
        elif ms < 10:
            nbshapes_b.append(nbshapes[i])
            mean_size_b.append(mean_size[i])
            identical_b.append(identical[i])
            mean_complex_b.append(mean_complex[i])
        else:
            nbshapes_c.append(nbshapes[i])
            mean_size_c.append(mean_size[i])
            identical_c.append(identical[i])
            mean_complex_c.append(mean_complex[i])
        i += 1

    print("MEDIAN SHAPE SIZE UNDER 3")
    print("Avg nb shapes ", average(nbshapes_a))
    print("Median nb shapes ", median(nbshapes_a))
    i = 0
    copy = identical_a.copy()
    for n in nbshapes_a:
        copy[i] = copy[i] / n
        i += 1
    print("Avg identical percentage ", average(copy))
    print("Avg mean shape size ", average(mean_size_a))
    copy = mean_size_a.copy()
    i = 0
    for c in mean_complex_a:
        copy[i] = c / copy[i]
        i += 1
    # print(copy)
    print("Avg complex/size", average(copy))
    print("\n")

    print("MEDIAN SHAPE SIZE UNDER 10")
    print("Avg nb shapes ", average(nbshapes_b))
    print("Median nb shapes ", median(nbshapes_b))
    i = 0
    copy = identical_b.copy()
    for n in nbshapes_b:
        copy[i] = copy[i] / n
        i += 1
    print("Avg identical percentage ", average(copy))
    print("Avg mean shape size ", average(mean_size_b))
    copy = mean_size_b.copy()
    i = 0
    for c in mean_complex_b:
        copy[i] = c / copy[i]
        i += 1
    # print(copy)
    print("Avg complex/size", average(copy))
    print("\n")

    print("MEDIAN SHAPE SIZE ABOVE 10")
    print("Avg nb shapes ", average(nbshapes_c))
    print("Median nb shapes ", median(nbshapes_c))
    i = 0
    copy = identical_c.copy()
    for n in nbshapes_c:
        copy[i] = copy[i] / n
        i += 1
    print("Avg identical percentage ", average(copy))
    print("Avg mean shape size ", average(mean_size_c))
    copy = mean_size_c.copy()
    i = 0
    for c in mean_complex_c:
        copy[i] = c / copy[i]
        i += 1
    # print(copy)
    print("Avg complex/size", average(copy))
    print("\n")

def print_basic_results(nbshapes, mean_size, median_size,largest, smallest,mean_complex,median_complex,max_complex, min_complex,identical, time_spent):
    print("Avg nb shapes ", average(nbshapes))
    #print("Median nb shapes ", median(nbshapes))
    #print("Avg mean shape size ", average(mean_size))
    #print("Median mean shape size ", median(mean_size))
    #print("Avg median shape size ", average(median_size))
    #print("Median median shape size ", median(median_size))
    #print("Avg largest shape ", average(largest))
    #print("Median largest shape ", median(largest))
    #print("Avg smallest shape", average(smallest))
    #print("Median smallest shape", median(smallest))
    #print("Median mean complexity ", median(mean_complex))
    #print("Avg median complexity ", average(median_complex))
    #print("Median complexity ", median(median_complex))
    #print("Avg max complexity ", average(max_complex))
    #print("Median max complexity ", median(max_complex))
    #print("Avg min complexity ", average(min_complex))
    #print("Median min complexity ", median(min_complex))
    # mean_complex / mean_size
    #print("Avg identical shapes ", average(identical))
    #print("Median identical shapes ", median(identical))
    i = 0
    copy = identical.copy()
    for n in nbshapes:
        copy[i] = copy[i] / n
        i += 1
    #print("Avg identical percentage ", average(copy))

    #print("Time spent ", average(time_spent))
    #print("Avg mean shape size ", average(mean_size))
    #print("Avg mean complexity ", average(mean_complex))
    copy = mean_size.copy()
    i = 0
    for c in mean_complex:
        copy[i] = c / copy[i]
        i += 1
    # print(copy)
    print("Avg complex/size", average(copy))
    print("Median nb shapes ", median(nbshapes))
    print("Median identical percentage ", median(copy))
    print("Avg median shape size ", median(mean_size))
    print("Median mean complexity ", median(mean_complex))
    print("\n")

def average(lst):
    return round(sum(lst)/len(lst),3)

def median(lst):
    return round(np.median(lst),3)

def plot_identical_percentage(nbshapes, nbshapes_1, identical, identical_1):
    fig, (ax,ax2) = plt.subplots(1,2)
    #ax.plot(nbshapes, identical)
    #ax.plot(nbshapes_1, identical_1)

    i = 0
    copy = identical.copy()
    for n in nbshapes:
        copy[i] = copy[i] / n
        i += 1
    i = 0
    copy_1 = identical_1.copy()
    for n in nbshapes_1:
        copy_1[i] = copy_1[i] / n
        i += 1
    expr = list(range(0, len(nbshapes)))

    ax.plot(expr, copy)
    ax2.plot(expr, copy_1)
    plt.show()

def plot_identical_percentage_2(percentage,percentage_1):
    fig, ax = plt.subplots()
    ex = list(range(0, len(percentage)))
    ax.plot(ex, percentage)
    ax.plot(ex, percentage_1)
    plt.show()

def plot_alpha_nbshapes():
    av = [0.0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2,5,10,100]
    ex = list(range(0, len(av)))
    nb_shapes, complexity = alpha_experiment([0], True)
    print(nb_shapes)
    print(complexity)
    fig, ax = plt.subplots()
    ax.plot(ex,nb_shapes)
    ax.plot(ex, complexity)
    #plt.xscale("log")
    plt.show()

def main():
    examples = [0,1,2,3,6,7,8]
    examples_all = [0,1,2,3,4,5,6,7,8,9]
    overlap_experiment(examples,False)
    #post_split_experiment(examples_all,True)
    #post_split_sizes_experiment(examples,False)
    #representation_experiment(examples_all,False)
    #cost_experiment(examples, False)
    #operation_experiment(examples,False)
    #alpha_experiment(examples,False)
    #plot_alpha_nbshapes()

    #percentage
    #plot_identical_percentage_2([0.34158406256221185,0.46610180549893243,0.3420555131516893,0.43137178879616134,0.480878670587517,0.4123137373849038,0.4738372588984549],
    #                            [0.44612042131382657,0.5041287921726759,0.4229240027823339,0.39121635755795703,0.5452200468129594,0.45726542505323403,0.48293493685945077])
    #mean shape size
    #plot_identical_percentage_2([22.372653536494955,40.36501562440603,45.22494410158257,62.29558287208004,63.80464859135371,100.94512774441753,86.15226209497432],
     #                           [23.196819462058883,38.38257334168784,43.15462622539223,59.28127929788493,62.24174418667774,96.26413691686363,83.47967189737884])

if __name__ == "__main__":
    main()

