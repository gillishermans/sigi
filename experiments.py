import sys
import os

def overlap_experiment(exp):
    for e in exp:
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file_to_open = __location__ + "\evaluation\experiment%s.txt" % e
        with open(file_to_open) as f:

            nbshapes = []
            ov_nbshapes = []

            mean_size = []
            ov_mean_size = []

            median_size = []
            ov_median_size = []

            largest = []
            ov_largest = []

            smallest = []
            ov_smallest = []

            mean_complex = []
            ov_mean_complex = []

            median_complex = []
            ov_median_complex = []

            max_complex = []
            ov_max_complex = []

            min_complex = []
            ov_min_complex = []

            identical = []
            ov_identical = []

            time_spent = []
            ov_time_spent = []

            boundary = 162
            i = 0
            ov = False
            skip = False
            for line in f:
                split = line.split(": ")
                if split[0] == "Overlap allowed":
                    if split[1] == 'True\n':
                        ov = True
                        continue
                    else:
                        ov = False
                        continue
                if split[0] == "Number of shapes":
                    if ov:
                        ov_nbshapes.append(int(split[1]))
                    else:
                        nbshapes.append(int(split[1]))
                if split[0] == "Largest shape":
                    if int(split[1]) == 1:
                        skip = True
                    else:
                        skip = False
                    if ov:
                        ov_largest.append(int(split[1]))
                    else:
                        largest.append(int(split[1]))
                if split[0] == "Number of 'redundant' identical shapes":
                    #if skip:
                        #continue
                    if ov:
                        ov_identical.append(int(split[1]))
                    else:
                        identical.append(int(split[1]))

            print("overlap identical average")
            print(sum(ov_identical)/len(ov_identical))
            print("non overlap identical average")
            print(sum(identical) / len(identical))
            print(ov_identical)
            print(identical)
            print("largest ov")
            print(sum(ov_largest) / len(ov_largest))
            print("largest")
            print(sum(largest) / len(largest) + 1)
            ov_copy = ov_identical.copy()
            copy = identical.copy()
            i = 0
            for n in ov_nbshapes:
                ov_copy[i] = ov_copy[i]/n
                i += 1
            i = 0
            for n in nbshapes:
                copy[i] = copy[i] / n
                i += 1
            print("ov identical per")
            print(sum(ov_copy)/len(ov_copy))
            print("identical per")
            print(sum(copy)/len(copy))

def main():
    overlap_experiment([0,1])


if __name__ == "__main__":
    main()

