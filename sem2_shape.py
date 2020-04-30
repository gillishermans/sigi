import numpy as np
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
import math as math
from itertools import combinations
import itertools
import random
import enclosure as encl


# Updates a list of probabilities for blocks.
def add_block(nb, prob, block_id, dmg):
    for b in prob:
        if b[0] == block_id and b[3] == dmg:
            b[1] = b[1] + 1.0
            b[2] = b[1] / nb
            return
    prob.append([block_id, 1.0, 1.0 / nb, dmg])

def add_block_type(nb,prob,block_id,dmg):
    for b in prob:
        if same_type(b[0],b[3],block_id,dmg):
            b[1] = b[1] + 1.0
            b[2] = b[1] / nb
            return
    prob.append([block_id, 1.0, 1.0 / nb, dmg])

def same_type(id1, d1, id2, d2):
    gen = [50, 53, 64, 65,66,67,68,69,71,77,78,96,107,
           108,109,114,128,134,135,136,143,156,163,164,
           167,170,183,184,185,186,187,193,194,195,196,
           197,198,202,203]
    if id1 != id2:
        return False
    elif d1 == d2:
        return True
    elif id1 == 17:
        jungle = [11, 15, 3, 7]
        spruce = [13, 1, 5, 9]
        birch = [10, 14, 2, 6]
        oak = [12, 0, 4, 8]
        if jungle.__contains__(d1) and jungle.__contains__(d2):
            return True
        if spruce.__contains__(d1) and spruce.__contains__(d2):
            return True
        if birch.__contains__(d1) and birch.__contains__(d2):
            return True
        if oak.__contains__(d1) and oak.__contains__(d2):
            return True
    elif id1 == 43:
        cobble = [11,3]
        wood = [10,2]
        stonebr = [13,5]
        brick = [12,4]
        quartz = [15,7]
        nether = [14,6]
        sandstone = [1,9]
        stone = [0,8]
        types = [cobble,wood,stonebr,brick,quartz,nether,sandstone,stone]
        for t in types:
            if t.__contains__(d1) and t.__contains__(d2):
                return True
    elif id1 == 44:
        cobble = [11,3]
        wood = [10,2]
        stonebr = [13,5]
        brick = [12,4]
        quartz = [15,7]
        nether = [14,6]
        sandstone = [1,9]
        stone = [0,8]
        types = [cobble,wood,stonebr,brick,quartz,nether,sandstone,stone]
        for t in types:
            if t.__contains__(d1) and t.__contains__(d2):
                return True
    elif id1 == 126:
        jungle = [11,3]
        birch = [10,2]
        dark = [13,5]
        acacia = [12,4]
        spruce = [1,9]
        oak = [0,8]
        types = [jungle,birch,dark,acacia,spruce,oak]
        for t in types:
            if t.__contains__(d1) and t.__contains__(d2):
                return True
    elif id1 == 155:
        pillar = [3,2,4]
        types = [pillar]
        for t in types:
            if t.__contains__(d1) and t.__contains__(d2):
                return True
    elif id1 == 162:
        dark = [13,1,5,9]
        acacia = [12,0,4,8]
        types = [dark,acacia]
        for t in types:
            if t.__contains__(d1) and t.__contains__(d2):
                return True
    elif gen.__contains__(id1):
        return True
    else:
        return False


# A single block class.
class Block:
    def __init__(self, block_id, dmg, x, y, z):
        self.id = block_id
        self.dmg = dmg
        self.x = x
        self.y = y
        self.z = z
        self.rx = x
        self.ry = y
        self.rz = z

    def compare_eq(self, other):
        if self.id == other.id and self.dmg == other.dmg and self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __float__(self):
        return float(self.id + float(self.dmg) / 100)

    def __repr__(self):
        return str(self)

    def __str__(self):
        #return str(float(self.id + float(self.dmg) / 100)) + " pos (" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"+ " rel pos (" + str(self.rx) + "," + str(self.ry) + "," + str(self.rz) + ")"
        #return str(float(self.id + float(self.dmg) / 100)) + "(" + str(self.rx) + "," + str(self.ry) + "," + str(self.rz) + ")"
        return str(float(self.id + float(self.dmg) / 100)) + str("(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")")
        return str(float(self.id + float(self.dmg) / 100))

    def write_str(self):
        return str(self.id) + " " + str(self.dmg) + " " + str(self.x) + " " + str(self.y) + " " + str(
            self.z) + " "

    def set_relative(self, f):
        self.rx = self.x - f[0]
        self.ry = self.y - f[1]
        self.rz = self.z - f[2]

    def copy(self):
        b = Block(self.id, self.dmg, self.x, self.y, self.z)
        b.rx = self.rx
        b.ry = self.ry
        b.rz = self.rz
        return b

    def basic_rel_pos(self, plane):
        if plane == 'xy':
            return [self.rx, self.ry]
        elif plane == 'zy':
            return [self.rz, self.ry]
        else:
            return [self.rx, self.rz]


# A shape class consisting of a collection of blocks.
class Shape:
    def __init__(self, b, plane):
        self.list = []
        self.plane = plane
        self.f = [b.x, b.y, b.z]
        self.ogf = [b.x, b.y, b.z]
        self.min = [b.x, b.y, b.z]
        self.max = [b.x, b.y, b.z]
        self.append(b)
        self.tag = self.__str__()
        self.rotated = False

    def __iter__(self):
        for b in self.list:
            yield b

    def __eq__(self, other):
        if self.plane == other.plane and self.f == other.f and self.list == other.list:
            return True
        else:
            return False

    def compare_eq(self, other):
        if self.plane == other.plane and self.f == other.f:
            c = 0
            for b in self.list:
                for o in other.list:
                    if b.compare_eq(o):
                        c = c + 1
            if c == len(self.list) and c == len(other.list):
                return True
        else:
            return False

    def eq_production(self, other):
        if self.tag == other.tag:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.plane) + " " + str(self.list)

    def write_str(self):
        string = str(self.plane) + " "
        for s in self.list:
            string = string + s.write_str()
        return string

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        return self.list[item]

    def copy(self):
        s = Shape(self.list[0], self.plane)
        c = []
        for b in self.list:
            c.append(b.copy())
        s.list = c
        s.tag = self.tag
        s.min = self.min
        s.max = self.max
        return s

    def extend(self, s):
        for b in s:
            self.append(b)

    def append(self, b):
        bn = (Block(b.id, b.dmg, b.x, b.y, b.z))
        self.new_relative(bn)
        bn.set_relative(self.f)
        self.list.append(bn)
        self.edit_min_max([b.x, b.y, b.z])

    def remove(self, s):
        self.list.remove(s)

    def set_relative(self, f):
        self.f = f
        for b in self.list:
            b.set_relative(f)

    def edit_pos(self, p):
        #self.f = [self.f[0] - p[0], self.f[1] - p[1], self.f[2] - p[2]]
        for b in self.list:
            b.x = b.x - p[0]
            b.y = b.y - p[1]
            b.z = b.z - p[2]
            #b.set_relative(self.f)
        self.normalize_relative()

    def normalize_relative(self):
        f = self.f
        for b in self.list:
            if f[0] + f[1] + f[2] >= b.x + b.y + b.z:
                f = [b.x, b.y, b.z]
        self.set_relative(f)


    def edit_min_max(self, p):
        if p[0] < self.min[0]: self.min[0] = p[0]
        if p[0] > self.max[0]: self.max[0] = p[0]
        if p[1] < self.min[1]: self.min[1] = p[1]
        if p[1] > self.max[1]: self.max[1] = p[1]
        if p[2] < self.min[2]: self.min[2] = p[2]
        if p[2] > self.max[2]: self.max[2] = p[2]

    def width(self):
        return self.max[0] - self.min[0]

    def depth(self):
        return self.max[2] - self.min[2]

    def height(self):
        return self.max[1] - self.min[1]

    def new_relative(self, b):
        if self.f[0] + self.f[1] + self.f[2] >= b.x + b.y + b.z:
            self.set_relative([b.x,b.y,b.z])


# Compare two shape sets and return a score for their similarity.
def similarity_shape_sets(default, shapes):
    score = 0.0
    nb = len(default)
    if len(default) == len(shapes):
        for d in default:
            for s in shapes:
                if d.compare_eq(s):
                    score = score + 1.0
                    # Found the matching s with d
                    break
    score = (score / nb)
    return score


# Create a shape from a list of blocks and a plane.
def shape_from_blocks(blocks, plane):
    s = Shape(blocks[0], plane)
    for b in blocks[1:]:
        s.append(b)
    return s


# Make a copy of a shape set.
def copy_shapes(shapes):
    copy = []
    for s in shapes:
        copy.append(s.copy())
    return copy


# Removes a copy from a shape set.
def remove_copy(shapes, sr):
    tr = []
    for s in shapes:
        if s.eq_production(sr):
            tr.append(s)
            break
    for r in tr:
        shapes.remove(r)
    return shapes


# Returns the first merge that decreased the cost.
def just_merge(shapes, prev_cost, cost_function=0, alpha=1.1, rect=0, duplicate_list=None):
    shapes = copy_shapes(shapes)
    # random.shuffle(shapes)
    for s1 in shapes:
        for s2 in shapes:
            if (rect == 0 and s1.__ne__(s2) and s1.plane == s2.plane) \
                    or (rect == 1 and is_legal_merge(s1, s2)) \
                    or (rect == 2 and s1.__ne__(s2) and s1.plane == s2.plane and contact(s1, s2)):
                s = merge_shape(s1, s2)
                if rect == 0 and not is_rect(s, s.plane):
                    continue
                new_shapes = [x for x in shapes if x != s1 and x != s2]
                new_shapes.append(s)
                if cost_function == 2:
                    copy_list = get_duplicate_shapes(new_shapes)#update_shape_duplicate_list(cost_function, duplicate_list, [s1,s2], [s])
                else: copy_list = duplicate_list
                new_cost = shapes_cost(new_shapes, cost_function, alpha, copy_list)
                if prev_cost - new_cost >= 0:
                    return new_shapes, new_cost, copy_list
    return shapes, prev_cost, duplicate_list


# Returns the best possible merge for a set of shapes
def best_merge(shapes, prev_cost, cost_function=0, alpha=1.1, duplicate_list=None):
    saved_cost = 0
    best = []
    for s1 in shapes:
        # if(len(s1) > 9): continue
        for s2 in shapes:
            # if (len(s2) > 9): continue
            if s1.__ne__(s2) and s1.plane == s2.plane:
                s = merge_shape(s1, s2)
                if not is_rect(s, s.plane):
                    continue
                new_shapes = [x for x in shapes if x != s1 and x != s2]
                new_shapes.append(s)
                if cost_function == 2:
                    copy_list = get_duplicate_shapes(new_shapes)#update_shape_duplicate_list(cost_function, duplicate_list, [s1,s2], [s])
                else:
                    copy_list = duplicate_list
                saved = prev_cost - shapes_cost(new_shapes, cost_function, alpha, copy_list)
                if saved >= saved_cost:
                    saved_cost = saved
                    best = new_shapes
    if len(best) == 0:
        return shapes, prev_cost, duplicate_list
    return best, saved_cost, duplicate_list


# Merges two shapes into one.
def merge_shape(s1, s2):
    m = s1.copy()
    m.extend(s2)
    return m


# Returns the first split found that decreases the cost.
def just_split(shapes, prev_cost, cost_function=0, alpha=1.1, rect=0, duplicate_list=None):
    shapes = copy_shapes(shapes)
    for s in shapes:
        if rect == 0:
            if len(s) % 2 != 0:
                continue
            splits = split_shape_2d(s)
        elif rect == 1:
            splits = split_shape_2d(s)
            splits = legal_splits(splits)
        else:
            splits = split_shape_3d_new(s)
            splits = legal_splits(splits)
        for split in splits:
            if s.__eq__(split[0]) and s.__eq__(split[1]):
                continue

            new_shapes = [x for x in shapes if x != s]
            new_shapes.append(split[0])
            new_shapes.append(split[1])
            #copy_list = update_shape_duplicate_list(cost_function, duplicate_list, [s], split)
            if cost_function == 2:
                copy_list = get_duplicate_shapes(new_shapes) #update_shape_duplicate_list(cost_function, duplicate_list, [s1, s2], [s])
            else:
                copy_list = duplicate_list
            new_cost = shapes_cost(new_shapes, cost_function, alpha, copy_list)
            #print("New split")
            #print(split)
            #print(new_cost)
            #print(prev_cost)
            if prev_cost - new_cost >= 0:
                duplicate_list = copy_list
                return new_shapes, new_cost, duplicate_list
    return shapes, prev_cost, duplicate_list


def best_split(shapes, prev_cost, cost_function=0, alpha=1.1, rect=0, duplicate_list=None):
    saved_cost = 0
    best = [shapes, prev_cost]
    shapes = copy_shapes(shapes)
    for s in shapes:
        if len(s) % 2 != 0:
            continue
        if rect == 0:
            splits = split_shape_2d(s)
        elif rect == 1:
            splits = split_shape_2d(s)
            splits = legal_splits(splits)
        else:
            splits = split_shape_3d(s)
            splits = legal_splits(splits)
        for split in splits:
            if s.__eq__(split[0]) and s.__eq__(split[1]):
                continue

            new_shapes = [x for x in shapes if x != s]
            new_shapes.append(split[0])
            new_shapes.append(split[1])
            if cost_function == 2:
                copy_list = get_duplicate_shapes(
                    new_shapes)  # update_shape_duplicate_list(cost_function, duplicate_list, [s1, s2], [s])
            else:
                copy_list = duplicate_list
            new_cost = shapes_cost(new_shapes, cost_function, alpha, copy_list)
            if prev_cost - new_cost >= 0:
                if saved_cost < prev_cost - new_cost:
                    saved_cost = prev_cost - new_cost
                    best = [new_shapes, new_cost, copy_list]

    return best[0], best[1], best[2]


#Returns the splits that provide legal shapes.
def legal_splits(splits):
    remove = []
    for split in splits:
        if not legal_split(split):
            remove.append(split)
    return [x for x in splits if not remove.__contains__(x)]


#Check if a split is legal.
def legal_split(split):
    for s in split:
        if not legal_shape(s):
            return False
    return True


#Checks if a shape is legal: all blocks can reach each other.
def legal_shape(s):
    found = [s.list[0]]
    not_found = s.list[1:]
    current = found[0]
    closed_list = [current]
    while len(found) != 0:
        current = found.pop(0)
        closed_list.append(current)

        fnd = []
        for b in not_found:
            if distance(current, b) == 1:
                c = False
                for closed_block in closed_list:
                    if b == closed_block:
                        c = True
                if c: continue
                fnd.append(b)
        found.extend(fnd)
        not_found = [x for x in not_found if not found.__contains__(x)]
    if len(not_found) != 0:
        return False
    return True


def split_shape_3d_new(s):
    possible_splits = []
    for w in range(s.min[0] + 1, s.max[0] + 1):
        one = []
        two = []
        for b in s:
            if b.x < w:
                one.append(b)
            else:
                two.append(b)
        if len(one) == 0 or len(two) == 0:
            continue
        possible_splits.append([shape_from_blocks(one, s.plane), shape_from_blocks(two, s.plane)])
    for h in range(s.min[1] + 1, s.max[1] + 1):
        one = []
        two = []
        for b in s:
            if b.y < h:
                one.append(b)
            else:
                two.append(b)
        if len(one) == 0 or len(two) == 0:
            continue
        possible_splits.append([shape_from_blocks(one, s.plane), shape_from_blocks(two, s.plane)])
    for d in range(s.min[2] + 1, s.max[2] + 1):
        one = []
        two = []
        for b in s:
            if b.z < d:
                one.append(b)
            else:
                two.append(b)
        if len(one) == 0 or len(two) == 0:
            continue
        possible_splits.append([shape_from_blocks(one, s.plane), shape_from_blocks(two, s.plane)])
    return possible_splits


#Returns all 3d splits for a 3d shape.
def split_shape_3d(s):
    splits1 = [list(c) for i in xrange(len(s.list)) for c in itertools.combinations(s.list, i + 1)]
    remove = []
    for s in splits1:
        if not legal_shape(shape_from_blocks(s, 'xy')):
            remove.append(s)
    splits1 = [x for x in splits1 if not remove.__contains__(x)]
    check = []
    possible_splits = []
    for e in splits1:
        remainder = [x for x in s if x not in e]
        if remainder not in check and remainder:
            possible_splits.append([shape_from_blocks(e, 'xy'), shape_from_blocks(remainder, 'xy')])
            check.append(e)
    return possible_splits


#Returns all 2d splits for a 2d shape.
def split_shape_2d(s):
    possible_splits = []
    if s.plane != 'zy':
        for w in range(s.min[0] + 1, s.max[0] + 1):
            one = []
            two = []
            for b in s:
                if b.x < w:
                    one.append(b)
                else:
                    two.append(b)
            if len(one) == 0 or len(two) == 0:
                continue
            possible_splits.append([shape_from_blocks(one, s.plane), shape_from_blocks(two, s.plane)])
    if s.plane != 'xz':
        for h in range(s.min[1] + 1, s.max[1] + 1):
            one = []
            two = []
            for b in s:
                if b.y < h:
                    one.append(b)
                else:
                    two.append(b)
            if len(one) == 0 or len(two) == 0:
                continue
            possible_splits.append([shape_from_blocks(one, s.plane), shape_from_blocks(two, s.plane)])
    if s.plane != 'xy':
        for d in range(s.min[2] + 1, s.max[2] + 1):
            one = []
            two = []
            for b in s:
                if b.z < d:
                    one.append(b)
                else:
                    two.append(b)
            if len(one) == 0 or len(two) == 0:
                continue
            possible_splits.append([shape_from_blocks(one, s.plane), shape_from_blocks(two, s.plane)])
    return possible_splits


#Returns true if the merge is a legal merge: merging two different shapes of the same plane that touch each other.
def is_legal_merge(s1, s2):
    if s1.__eq__(s2) or s1.plane != s2.plane:
        return False
    else:
        if not contact(s1, s2):
            return False
        else:
            if s1.plane == 'xy':
                if s1.list[0].z != s2.list[0].z:
                    return False
            elif s1.plane == 'xz':
                if s1.list[0].y != s2.list[0].y:
                    return False
            else:
                if s1.list[0].x != s2.list[0].x:
                    return False
    return True


# Returns true if a shape is a rectangle.
def is_rect(s, plane):
    r = find_rect(s, plane)
    if len(r) == 1:
        if abs(1 + r[0][2] - r[0][0]) * abs(1 + r[0][3] - r[0][1]) == len(s):
            return True
    return False


# Finds the shape rectangles.
def find_rect(s, plane):
    test = np.zeros((2 * len(s) + 1, 2 * len(s) + 1))

    if plane == 'xy':
        z = 999999
        for b in s:
            if z == 999999:
                z = b.z
            else:
                if z != b.z: return []
            if b.rx + len(s) >= 2 * len(s) + 1 or b.ry + len(s) >= 2 * len(s) + 1: return []
            if b.rx + len(s) < 0 or b.ry + len(s) < 0: return []
            test[b.rx + len(s)][b.ry + len(s)] = 1.0
    if plane == 'xz':
        y = 999999
        for b in s:
            if y == 999999:
                y = b.y
            else:
                if y != b.y: return []
            if b.rx + len(s) >= 2 * len(s) + 1 or b.rz + len(s) >= 2 * len(s) + 1: return []
            if b.rx + len(s) < 0 or b.rz + len(s) < 0: return []
            test[b.rx + len(s)][b.rz + len(s)] = 1.0
    if plane == 'zy':
        x = 999999
        for b in s:
            if x == 999999:
                x = b.x
            else:
                if x != b.x: return []
            if b.ry + len(s) >= 2 * len(s) + 1 or b.rz + len(s) >= 2 * len(s) + 1: return []
            if b.ry + len(s) < 0 or b.rz + len(s) < 0: return []
            test[b.ry + len(s)][b.rz + len(s)] = 1.0
    r = get_rectangle(test)
    return r


# Gets the rectangles of a matrix. Based on Prabhat Jha (https://www.geeksforgeeks.org/find-rectangles-filled-0/)
def get_rectangle(s):
    out = []
    index = -1

    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if s[i][j] == 1:
                # storing initial position
                # of rectangle
                out.append([i, j])

                # will be used for the
                # last position
                index = index + 1
                find_end(i, j, s, out, index)
    return out


# Get_rectangle help function. Based on Prabhat Jha (https://www.geeksforgeeks.org/find-rectangles-filled-0/)
def find_end(i, j, s, out, index):
    flagc = 0
    flagr = 0

    for m in range(i, len(s)):
        if s[m][j] == 0:
            flagr = 1  # set the flag
            break
        if s[m][j] == 2:
            pass
        for n in range(j, len(s[0])):
            if s[m][n] == 0:
                flagc = 1
                break
            s[m][n] = 2

    if flagr == 1:
        out[index].append(m - 1)
    else:
        out[index].append(m)

    if flagc == 1:
        out[index].append(n - 1)
    else:
        out[index].append(n)


# [TOO SLOW] Entropy discount for identical shapes.
def shapes_cost2(shapes):
    shapes = copy_shapes(shapes)
    alpha = 1.01
    to_remove = []
    for s1 in shapes:
        for s2 in shapes:
            if (is_duplicate_shape(s1, s2)):
                to_remove.append(s2)

    shapes = [x for x in shapes if x not in to_remove]
    cost = (1 + dl(shapes) + dl(to_remove) / 2) ** alpha  # cost = (1 + dl(shapes)) ** alpha
    for s in shapes:
        cost = cost + entropy(s)
    for s in to_remove:
        cost = cost + entropy(s)

    return cost

def update_shape_duplicate_list(cost,dupe,old,new):
    copy = None
    if cost == 2:
        copy = dupe[:]
        #print("STRAIGHT COPY")
        #print(copy)
        for d in copy:
            for o in old:
                #print("REMOVE")
                #print(d)
                #print(o)
                d = [x for x in d if not x.__eq__(o)]
                #print(o)


                #for e in d:
                #    if e.eq_production(o):
                #        d.remove(o)
                #        print("removed")
        copy = [x for x in copy if len(x)>0]
        for d in copy:
            #print("ADDING")
            #print(d[0])
            for n in new:
                #print(n)
                if is_duplicate_shape(d[0],n):
                    d.append(n)
                    #print("added")
                else:
                    copy.append([n])
    #print("UPDATE")
    #print(copy)
    return copy


# Returns the cost of the given set of shapes.
def shapes_cost(shapes, cost_function=0, alpha=1.1, duplicate_list=None):
    alpha = alpha+0.00001
    # Cost function for largest possible shapes
    if cost_function == -1:
        cost = (1.0 + dl(shapes))
        return cost
    # Cost grows more for every block type
    elif cost_function == 1:
        cost = (1.0 + dl(shapes)) * alpha
        for s in shapes:
            prob = []
            for b in s:
                add_block_type(len(s), prob, b.id, b.dmg)
            cost = cost + entropy(s) * len(prob)
        return cost
    # Cost discount for identical shapes
    elif cost_function == 2:
        no_duplicates = []
        for d in duplicate_list:
            no_duplicates.append(d[0])
        cost = (1.0 + dl(no_duplicates)) * alpha
        for s in no_duplicates:
            cost = cost + entropy(s) #+ len(s)/10
        return cost
    # Standard entropy + DL cost function
    else:
        cost = (1.0 + dl(shapes)) * alpha
        for s in shapes:
            cost = cost + entropy(s)
        return cost


# Returns the entropy of a shape.
def entropy(s):
    e = 0
    prob = []
    # sum block types = for
    for b in s:
        add_block_type(len(s), prob, b.id, b.dmg)
    # Probability of certain block type * log of prob
    for p in prob:
        e = e + p[2] * math.log(p[2], 2)
    e = - e
    return e + 0.00001


# The description length of a set of shapes.
def dl(shapes):
    return len(shapes)


# Perform the hill climbing algorithm on a set of shapes.
def hill_climbing(shapes, rect, merge_split, cost_function=0, alpha=1.1, m=None, duplicate_list=None):
    same = 0
    prev_shape_cost = 99999999
    while same < 2:
        cpy = shapes[:]  # shapes.copy()
        if merge_split == 2:
            new_m, cost_m, duplicate_list = just_merge(cpy, prev_shape_cost, cost_function, alpha, rect, duplicate_list)

            new_s, cost_s, duplicate_list = just_split(cpy, prev_shape_cost, cost_function, alpha, rect, duplicate_list)
            if cost_m < cost_s:
                new = new_m
                cost = cost_m
            else:
                new = new_s
                cost = cost_s
            # print(cost)
            # print(new)
        elif merge_split == 1:
            # start with every shape as large as possible
            if prev_shape_cost == 99999999:
                cpy = hill_climbing(cpy, rect, 0, -1)
                cpy = filter_final_shapes_overlap(cpy, m)
                print("START SHAPES")
                print(cpy)
                if cost_function == 2: duplicate_list = get_duplicate_shapes(cpy)
                prev_shape_cost = shapes_cost(cpy, cost_function, alpha, duplicate_list)
            new, cost, duplicate_list = just_split(cpy, prev_shape_cost, cost_function, alpha, rect, duplicate_list)
        else:
            new, cost, duplicate_list = just_merge(cpy, prev_shape_cost, cost_function, alpha, rect, duplicate_list)
        if cost == prev_shape_cost:
            same = same + 1
        shapes = new
        prev_shape_cost = cost
    return shapes


# Filters the final shape set for a set of the largest possible shapes that encompass all details from the example. Overlap is allowed.
def filter_final_shapes_overlap(shapes, m):
    final = []
    blocks = []
    for row in m:
        for col in row:
            for b in col:
                # if block is not air
                if b.id != 0:
                    blocks.append(b)
    sort = sorted(shapes, key=len, reverse=True)
    while blocks != []:
        for s in sort:
            if len(final) == 0:
                final.append(s)
                for e in s:
                    for b in blocks:
                        if e.id == b.id and e.dmg == b.dmg and e.x == b.x and e.y == b.y and e.z == b.z:
                            blocks.remove(b)

            else:
                go = False
                for e in s:
                    if final_block_check(blocks, e):
                        go = True
                        break
                if go:
                    final.append(s)
                    for e in s:
                        for b in blocks:
                            if e.id == b.id and e.dmg == b.dmg and e.x == b.x and e.y == b.y and e.z == b.z:
                                blocks.remove(b)
    return final


# Filters the final shape set for a set of the largest possible shapes that encompass all details from the example. Overlap is NOT allowed.
def filter_final_shapes_no_overlap(shapes):
    final = []
    blocks = []
    sort = sorted(shapes, key=len, reverse=True)

    for s in sort:
        if len(final) == 0:
            final.append(s)
            for e in s:
                blocks.append(e)
        else:
            go = True
            for e in s:
                if final_block_check(blocks, e):
                    go = False
                    break
            if go:
                final.append(s)
                for e in s:
                    blocks.append(e)
    return final


# Helper function for both filter_final_shapes().
def final_block_check(blocks, e):
    for b in blocks:
        if e.id == b.id and e.dmg == b.dmg and e.x == b.x and e.y == b.y and e.z == b.z:
            return True
    return False


# Split shapes based on shapes in the given plane. Cut shapes on floors and walls.
def post_plane_split(shapes, plane='xz'):
    # Find the shapes in plane that can be split on.
    splitters = []
    for splitter in shapes:
        if splitter.plane == plane:
            splitters.append(splitter)
    for splitter in splitters:
        remove = []
        add = []
        # Check every shape for a possible split.
        for s in shapes:
            # A split requires contact.
            if splitter == s or not contact(splitter, s):
                continue
            else:
                i = 0
                if plane == 'xz':
                    i = splitter.list[0].y
                elif plane == 'xy':
                    i = splitter.list[0].z
                elif plane == 'zy':
                    i = splitter.list[0].x
                top = []
                bottom = []
                middle = []
                for b in s:
                    if split_on_i(plane, b) > i:
                        top.append(b)
                    elif split_on_i(plane, b) < i:
                        bottom.append(b)
                    if split_on_i(plane, b) == i:
                        middle.append(b)
                if len(top) == 0 or len(bottom) == 0:
                    continue
                else:
                    if plane == 'xz':
                        bottom.extend(middle)
                    else:
                        bottom.extend(middle)
                        top.extend(middle)
                    remove.append(s)
                    add.append(shape_from_blocks(top, s.plane))
                    add.append(shape_from_blocks(bottom, s.plane))
        shapes = [i for i in shapes if not remove.__contains__(i)]
        for a in add:
            shapes.append(a)
    return shapes


# Helper function for post_plane_split(). Returns the corresponding value from b according to the given plane.
def split_on_i(plane, b):
    if plane == 'xz':
        return b.y
    elif plane == 'xy':
        return b.z
    else:
        return b.x


# Learn the relations between shapes in a shape set.
def relation_learning(shapes):
    shape_dupe_list = get_duplicate_shapes(shapes)
    rel = []
    copy = copy_shapes(shapes)
    for sl1 in shape_dupe_list:
        for s1 in sl1:
            for s2 in copy:
                if not s1.eq_production(s2):#if s1.__ne__(s2):
                    if contact(s1, s2):
                        rel.append([sl1, s2, s1])
    new_rel = []
    for elem in rel:
        if elem not in new_rel:
            new_rel.append(elem)
    rel = new_rel
    return rel

def relation_learning_prob(shapes):
    shape_dupe_list = get_duplicate_shapes(shapes)
    relations = []
    for s in shapes:
        for dupe in shape_dupe_list:
            for d in dupe:
                if not s.eq_production(d) and contact(s,d):
                    relations.append([s,d,len(dupe)])
    return relations


def get_duplicate_shapes(shapes):
    copy = copy_shapes(shapes)
    shape_dupe_list = []
    for s1 in copy:
        if in_shape_dupe_list(s1, shape_dupe_list):
            continue
        s = [s1]
        for s2 in copy:
            if in_shape_dupe_list(s2, shape_dupe_list):
                continue
            if s1.__ne__(s2) and is_duplicate_shape(s1, s2):
                s.append(s2)
        shape_dupe_list.append(s)
    return shape_dupe_list


# Check if the shape is in the shape duplication list.
def in_shape_dupe_list(shape, shape_dupe_list):
    for sl in shape_dupe_list:
        for s in sl:
            if shape.__eq__(s):
                return True
    return False


# Check for direct contact between two shapes.
def contact(s1, s2):
    for b1 in s1:
        for b2 in s2:
            if distance(b1, b2) == 1:
                return True
    return False


# Return the distance between two blocks.
def distance(b1, b2):
    return sqrt(pow((b2.x - b1.x), 2) + pow((b2.y - b1.y), 2) + pow((b2.z - b1.z), 2))


# Return a production of shapes.
def production(shapes, rel, n=5):
    # Start with a random initial shape.
    w = random.choice(shapes)
    final = [w]
    while n > 0:
        rrel = []
        for r in rel:
            for s in r[0]:
                if s.eq_production(w):
                    rrel.append(r)
        if len(rrel) != 0:
            r = random.choice(rrel)
            og = r[2]
            r = r[1]
            shape = r.copy()
            edit_pos_relation(w, og, shape)
            final.append(shape)
            # Continue with a random shape or the newly appended shape.
            w = random.choice(final)  # w = shape
        n = n - 1
    return final


# Checks for overlap between the final shape set and a new shape s.
def check_overlap(final, s):
    for f in final:
        if f.plane != s.plane: continue
        fmin = [f.list[0].x, f.list[0].y, f.list[0].z]
        fmax = [f.list[0].x, f.list[0].y, f.list[0].z]
        for b in f:
            if fmin[0] > b.x or fmin[1] > b.y or fmin[2] > b.z:
                fmin = [b.x, b.y, b.z]
            if fmax[0] < b.x or fmax[1] < b.y or fmax[2] < b.z:
                fmax = [b.x, b.y, b.z]
        smin = [s.list[0].x, s.list[0].y, s.list[0].z]
        smax = [s.list[0].x, s.list[0].y, s.list[0].z]
        for b in s:
            if smin[0] > b.x or smin[1] > b.y or smin[2] > b.z:
                smin = [b.x, b.y, b.z]
            if smax[0] < b.x or smax[1] < b.y or smax[2] < b.z:
                smax = [b.x, b.y, b.z]
        print("check overlap")
        print(fmin)
        print(fmax)
        print(smin)
        print(smax)
        if smin[0] >= fmin[0] and smin[1] >= fmin[1] and smin[2] >= fmin[2] and smax[0] <= fmax[0] and smax[1] <= fmax[
            1] and smax[2] <= fmax[2]:
            return True
    return False


# Return a production of shapes with a size limitation.
def production_limit(shapes, rel, limit=[10, 10, 10], n=5, rotate_first=False):
    f = None
    if rotate_first:
        w = random_rotate(f, shapes[2])  # random.choice(shapes))
    else:
        w = random.choice(shapes)
    min = [w.list[0].x, w.list[0].y, w.list[0].z]
    max = [w.list[0].x, w.list[0].y, w.list[0].z]
    final = [w]
    tries = 0

    while n > 0:
        # Continue with a random shape.
        f = random.choice(final)
        if tries > 100:
            break
        rrel = []
        for r in rel:  # of the form [[s1, possible identical s], s2, s1]
            for s in r[0]:
                if s.eq_production(f):
                    rrel.append(r)
        if len(rrel) != 0:
            r = random.choice(rrel)
            og = r[2]
            shape = r[1].copy()
            shape = edit_pos_relation(f, og, shape)

            tempmin = min
            tempmax = max
            if shape.list[0].x < min[0]: min[0] = shape.list[0].x
            if shape.list[0].y < min[1]: min[1] = shape.list[0].y
            if shape.list[0].z < min[2]: min[2] = shape.list[0].z
            if shape.list[0].x > max[0]: max[0] = shape.list[0].x
            if shape.list[0].y > max[1]: max[1] = shape.list[0].y
            if shape.list[0].z > max[2]: max[2] = shape.list[0].z
            if max[0] - min[0] > limit[0] or max[1] - min[1] > limit[1] or max[2] - min[2] > limit[2]:
                min = tempmin
                max = tempmax
                tries = tries + 1
                print("limited")
                continue
            else:
                #if final.__contains__(shape):
                #    tries = tries + 1
                #    continue
                if check_overlap(final,shape):
                    tries = tries + 1
                    continue
                tries = 0
                blocked = []
                # if shape.plane == 'xz':
                #    continue
                final.append(shape)  # final.append(random_rotate(f,shape))
                print("append")
                print(shape)
        else:
            continue
        n = n - 1
    return final


def fill_production(shapes, rel, n=100):
    not_enclosed = encl.enclosure_find_3d(shapes)
    print("fill not enclosed")
    print(not_enclosed)
    tries = 0
    while tries < n:
        if len(not_enclosed) == 0:
            print("Fully enclosed", tries)
            return shapes
        f = random.choice(not_enclosed)
        rrel = []
        for r in rel:  # of the form [[s1, possible identical s], s2, s1]
            for s in r[0]:
                if s.eq_production(f):
                    rrel.append(r)
        if len(rrel) != 0:
            r = random.choice(rrel)
            og = r[2]
            shape = r[1].copy()
            shape = edit_pos_relation(f, og, shape)

            copy = copy_shapes(shapes)
            copy.append(shape)
            new_not_enclosed = encl.enclosure_find_3d(copy)
            if len(not_enclosed) > len(new_not_enclosed):
                shapes = copy
                not_enclosed = new_not_enclosed
            else:
                tries += 1
    return shapes


# Rotate s if w is rotated.
def random_rotate(w, s):
    if w is None:
        print("first")
        return rotate_shape(s)
    else:
        if not w.rotated:
            print("prev not rot")
            return s
        else:
            print("prev rot")
            return rotate_shape(s)


#Rotate a shape.
def rotate_shape(s):
    #print(s)
    #print(s.plane)
    if s.plane == 'xy':
        rs = s.copy()
        rs = to_zy(rs)
        #rs[5].id = 14
        #rs[5].dmg = 0
    elif s.plane == 'zy':
        rs = s.copy()
        rs = to_xy(rs)
        #rs[5].id = 16
        #rs[5].dmg = 0
    else:
        rs = rotate_xz(s)
    #print(rs)
    #print(rs.plane)
    rs.rotated = True
    return rs

#Rotate a shape.
def rotate_shape_n(s,w,og):
    if w.plane == 'xy':
        og_copy = to_xy(og)
    else:
        og_copy = to_zy(og)
    p = [0, 0, 0]
    if s.plane == 'xy':
        rs = s.copy()
        rs = to_zy(rs)
        p[0] = og_copy.f[0] - w.f[0]
        p[1] = og_copy.f[1] - w.f[1]
        p[2] = og_copy.f[2] - w.f[2]
        #print("edit p")
        #print(p)
        #print(og.f)
        #print(w.f)
        rs.edit_pos(p)
    elif s.plane == 'zy':
        rs = s.copy()
        rs = to_xy(rs)
        p[0] = og_copy.f[0] - w.f[0]
        p[1] = og_copy.f[1] - w.f[1]
        p[2] = og_copy.f[2] - w.f[2]
        rs.edit_pos(p)
    else:
        rs = rotate_xz(s)
    rs.rotated = True
    return rs


# Edit the position of a new shape according to the position, and orientation of the shape that produced it.
def edit_pos_relation(w, og, shape):
    copy = shape.copy()
    w.normalize_relative()
    og.normalize_relative()
    p = [0, 0, 0]
    if w.plane == 'xz' and w.rotated and w.plane == og.plane:
        print("rotate xz")
        copy = rotate_shape(copy)
    elif w.plane == og.plane:
        print("same plane")
        p[0] = og.f[0] - w.f[0]
        p[1] = og.f[1] - w.f[1]
        #print("og")
        #print(og)
        #print(og.f)
        #print("w")
        #print(w)
        #print(w.f)
        p[2] = og.f[2] - w.f[2]
        #print("p")
        #print(p)
        #print("og copy")
        #print(copy)
        copy.edit_pos(p)
    else:
        print("not og plane")
        copy = rotate_shape_n(copy,w,og)
    return copy


# Check if the s2 is the same as s1 aside from it's location and orientation
def is_duplicate_shape(s1, s2):
    if len(s1) != len(s2):
        return False
    m = len(s1)
    for b1 in s1:
        for b2 in s2:
            if same_type(b1.id, b1.dmg, b2.id, b2.dmg) and b1.basic_rel_pos(s1.plane) == b2.basic_rel_pos(s2.plane):
                m = m - 1
                break
    if m == 0:
        return True
    return False


# Convert a shape to the same shape in the xz plane.
def to_xz(s):
    if s.plane == 'xz': return s.copy()
    if s.plane == 'xy':
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.z
            b.z = temp
        sd.plane = 'xz'
        sd.normalize_relative()
        return sd
    if s.plane == 'zy':
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.x
            b.x = temp
        sd.plane = 'xz'
        sd.normalize_relative()
        return s


# Convert a shape to the same shape in the xy plane.
def to_xy(s):
    if s.plane == 'xy': return s.copy()
    if s.plane == 'xz':
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.z
            b.z = temp
        sd.plane = 'xy'
        sd.normalize_relative()
        return sd
    if s.plane == 'zy':
        sd = s.copy()
        for b in sd:
            temp = b.z
            b.z = -b.x
            b.x = temp
        sd.plane = 'xy'
        sd.normalize_relative()
        return sd


# Convert a shape to the same shape in the zy plane.
def to_zy(s):
    if s.plane == 'zy': return s.copy()
    if s.plane == 'xz':
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.x
            b.x = temp
        sd.plane = 'zy'
        sd.normalize_relative()
        return sd
    if s.plane == 'xy':
        sd = s.copy()
        for b in sd:
            temp = b.z
            b.z = -b.x
            b.x = temp
        sd.plane = 'zy'
        sd.normalize_relative()
        return sd


# Rotate an xz shape.
def rotate_xz(s):
    new = []
    copy = s.copy()
    for b in copy:
        tmp = b.x
        b.x = b.z
        b.z = tmp
        new.append(b)
    return shape_from_blocks(new, s.plane)


# [Unfinished] Extends a shape with a given length.
def extend_shape(s, l=1):
    if (s.plane == 'xy'):
        print("EXTEND")
        print(s)
        minx = s[0].x
        maxx = s[0].x
        for b in s:
            if (b.x < minx): minx = b.x
            if (b.x > maxx): maxx = b.x
        mid = int((maxx - minx + 1) / 2)
        middle = []
        right = []
        for b in s:
            if (b.x == mid): middle.append(b)
            if (b.x > mid): right.append(b)
        for i in range(1, l + 1):
            for m in middle:
                m = m.copy()
                m.x = m.x + i
                s.append(m)
        for r in right:
            r.x = r.x + l
            r.set_relative(s.f)
    if (s.plane == 'zy'):
        print("EXTEND")
        print(s)
        minz = s[0].z
        maxz = s[0].z
        for b in s:
            if (b.z < minz): minz = b.z
            if (b.z > maxz): maxz = b.z
        mid = int((maxz - minz + 1) / 2)
        middle = []
        right = []
        for b in s:
            if (b.z == mid): middle.append(b)
            if (b.z > mid): right.append(b)
        for i in range(1, l + 1):
            for m in middle:
                m = m.copy()
                m.z = m.z + 1
                s.append(m)
        for r in right:
            r.z = r.z + 1
            r.set_relative(s.f)
    if (s.plane == 'xz'):
        return s
        print("EXTEND")
        print(s)
        minz = s[0].z
        maxz = s[0].z
        for b in s:
            if (b.z < minz): minz = b.z
            if (b.z > maxz): maxz = b.z
        mid = int((maxz - minz + 1) / 2)
        middle = []
        right = []
        for b in s:
            if (b.z == mid): middle.append(b)
            if (b.z > mid): right.append(b)
        for m in middle:
            m = m.copy()
            m.z = m.z + 1
            s.append(m)
        for r in right:
            r.z = r.z + 1
            r.set_relative(s.f)
        minx = s[0].x
        maxx = s[0].x
        for b in s:
            if (b.x < minx): minx = b.x
            if (b.x > maxx): maxx = b.x
        mid = int((maxx - minx + 1) / 2)
        middle = []
        right = []
        for b in s:
            if (b.x == mid): middle.append(b)
            if (b.x > mid): right.append(b)
        for m in middle:
            m = m.copy()
            m.x = m.x + 1
            s.append(m)
        for r in right:
            r.x = r.x + 1
            r.set_relative(s.f)
    print("res")
    print(s)
    return s


def normalize_relative(shapes):
    for s in shapes:
        s.normalize_relative()
    return shapes
