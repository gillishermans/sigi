import numpy as np
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
import math as math
from  itertools import combinations
import itertools
import random

#A single block class
class Block:
    def __init__(self, blockid, dmg, x, y, z):
        self.id = blockid
        self.dmg = dmg
        self.x = x
        self.y = y
        self.z = z
        self.rx = x
        self.ry = y
        self.rz = z

    def __float__(self):
        return float(self.id + float(self.dmg)/100)
    def __repr__(self):
        return str(self)

    def __str__(self):
        #return str(float(self.id + float(self.dmg) / 100)) + " pos (" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"+ " rel pos (" + str(self.rx) + "," + str(self.ry) + "," + str(self.rz) + ")"
        return str(float(self.id + float(self.dmg) / 100)) + " rel pos (" + str(self.rx) + "," + str(self.ry) + "," +str(self.rz) + ")"
        return str(float(self.id + float(self.dmg) / 100))

    def set_relative(self,f):
        self.rx = self.x-f[0]
        self.ry = self.y-f[1]
        self.rz = self.z-f[2]

#A shape class consisting of a plane of blocks
class Shape:
    def __init__(self,b,plane):
        self.list = []
        self.plane = plane
        self.f = [b.x,b.y,b.z]
        self.ogf = [b.x,b.y,b.z]
        self.append(b)

    def __iter__(self):
        for b in self.list:
            yield b

    def __eq__(self, other):
        if self.plane == other.plane and self.f == other.f and self.list == other.list:
            return True
        else:
            return False

    def eq_no_plane(self,other):
        if self.f == other.f and self.list == other.list:
            return True
        else:
            return False

    def eq_production(self,other):
        if self.list == other.list:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.plane) + " " +  str(self.list)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        return self.list[item]

    def copy(self):
        s = Shape(self.list[0], self.plane) #self.f
        s.list = self.list[:]
        return s

    def extend(self,s):
        for b in s:
            self.append(b)

    def append(self,b):
        bn = (Block(b.id,b.dmg,b.x,b.y,b.z))
        bn.set_relative(self.f)
        #b.set_relative(self.f)
        self.list.append(bn)

    #def get_relative(self,item):
    #    b = item
    #    #print("RELATIVE")
    #    #print('(' + str(self.f[0]) + ', ' + str(self.f[1]) + ', ' + str(self.f[2]) + ')')
    #    #print('(' + str(b.x) + ', ' + str(b.y) + ', ' + str(b.z) + ')')
    #    return Block(b.id, b.dmg, b.x - self.f[0], b.y - self.f[1], b.z - self.f[2])

    def remove(self,s):
        self.list.remove(s)

    def set_relative(self,f):
        print(f)
        self.f = f
        for b in self.list:
            b.set_relative(f)


class Relation:
    def __init__(self,s1,s2,planes):
        self.s1 = s1
        self.s2 = s2
        #self.pl = self.plane(s1.plane,s2.plane)




def add_block(nb,prob,blockid,dmg):
    for b in prob:
        if b[0] == blockid and b[3] == dmg:
            b[1] = b[1]+1.0
            b[2] = b[1]/nb
            return
    prob.append([blockid,1.0,1.0/nb,dmg])

def just_merge(shapes):
    for s1 in shapes:
        #if (len(s1) > 9): continue
        for s2 in shapes:
            #if (len(s2) > 9): continue
            if s1.__ne__(s2) and s1.plane == s2.plane:
                        #print("JUST")
                        #print(s1)
                        #print(s2)
                        s = merge_shape(s1,s2)
                        #print(s)
                        if not is_rect(s):
                            continue
                        #print("RECT")
                        new_shapes = [x for x in shapes if x!=s1 and x!=s2]
                        new_shapes.append(s)
                        #print(new_shapes)
                        saved = shapes_cost(shapes) - shapes_cost(new_shapes)
                        #print(saved)
                        if saved >= 0:
                            return new_shapes
    return shapes

#Returns the best possible merge for a set of shapes
def best_merge(shapes):
    saved_cost = 0
    best = []
    for s1 in shapes:
        #if(len(s1) > 9): continue
        for s2 in shapes:
            #if (len(s2) > 9): continue
            #print("BEST  MERGE")
            #print(shapes)
            #print(s1)
            #print(s2)
            if s1.__ne__(s2) and s1.plane == s2.plane:
                s = merge_shape(s1,s2)
                if not is_rect(s):
                    continue
                new_shapes = [x for x in shapes if x!=s1 and x!=s2]
                new_shapes.append(s)
                saved = shapes_cost(shapes) - shapes_cost(new_shapes)
                #saved = shape_cost(s1) + shape_cost(s2) - shape_cost(s)
                if saved >= saved_cost:
                    saved_cost = saved
                    best = new_shapes
                #else:
                    #print("NOT BETTER")
            #else:
                #print("NOT EQUAL")
    if len(best) == 0:
        #print("NO BETTER MERGE")
        return shapes
    #print("appendshit")
    #print(shapes)
    #print(best[2])
    #print(best[0])
    #print(best[1])
    #shapes = [x for x in shapes if x!=best[0] and x!=best[1]]
    #shapes.append(best[2])
    #print(shapes)
    #print("endappendshit")
    return best #shapes

#merges two shapes into one
def merge_shape(s1,s2):
    m = s1.copy()
    m.extend(s2)
    return m

# Returns the best possible split for a set of shapes
def best_split(shapes):
    saved_cost = 0
    best = []
    for s in shapes:
        split = split_shape(s)
        if(s.__eq__(split[0]) and s.__eq__(split[1])):
            continue
        if shape_cost(s) - (shape_cost(split[0]) + shape_cost(split[1])) > saved_cost:
            saved_cost = shape_cost(s) - (shape_cost(split[0]) + shape_cost(split[1]))
            best = [s,split[0],split[1]]
    if len(best) == 0:
        return shapes
    print("SPLIT THESE")
    print(s)
    print(split[0])
    print(split[1])
    shapes.remove(s)
    shapes.append(split[0])
    shapes.append(split[1])
    return shapes

#splits a shape into two shapes - find the best split according to the minimal cost of the shapes
def split_shape(s):
    #r = find_rect(s)
    subshapes = sub_shapes(s)
    print(subshapes)
    possible_splits = []
    for sub in subshapes:
        print("SUB")
        print(sub)
        if is_rect(sub[0]) and is_rect(sub[1]):
            possible_splits.append(sub)
    print("POSSIBLE")
    print(possible_splits)
    print(s)
    best = [s,s]
    cost = shape_cost(best[0])
    print("COST")
    print(cost)
    for i in range(0,len(possible_splits)):
        print("COSTif")
        print(shape_cost(possible_splits[i][0]) + shape_cost(possible_splits[i][1]))
        if shape_cost(possible_splits[i][0]) + shape_cost(possible_splits[i][1]) < cost:
            best = possible_splits[i]
            cost = shape_cost(best[0]) + shape_cost(best[1])
    return best

#finds the sub_shape combinations for a certain shape
def sub_shapes(s):
    subshapes = []
    sub = []
    for i in range(1,len(s)):
        comb = combinations(s,i)
        for c in comb:
            print(c)
            if len(c) == 1:
                sub.append([c[0]])
            else:
                l = []
                for e in c:
                    l.append(e)
                sub.append(l)
    for i in range(0,len(sub)):
        subs = Shape(sub[i][0], s.plane)
        subs.extend(sub[i][1:])
        sob = [a for a in s if a not in sub[i]]
        sobs = Shape(sob[0], s.plane)
        sobs.extend(sob[1:])
        subsob = [subs, sobs]
        subshapes.append(subsob)
    return subshapes

#returns true if a shape is a rectangle
def is_rect(s):
    r = find_rect(s)
    if len(r) == 1:
        if abs(1 + r[0][2] - r[0][0]) * abs(1 + r[0][3] - r[0][1]) == len(s):
            return True
    return False

#find the shape rectangles
def find_rect(s):
    test = np.zeros((2*len(s)+1,2*len(s)+1))

    if s.plane == 'xy':
        z = 999999
        for b in s:
            if (z==999999): z = b.z
            else:
                if (z != b.z): return []
            #print("BLOCK FIND RECT")
            #print(s)
            #print(b)
            #print(str(b.x) + ', ' + str(b.y) + ', ' + str(b.z))
            #print(str(b.rx) + ', ' + str(b.ry) + ', ' + str(b.rz))
            if b.rx+len(s) >= 2*len(s)+1 or b.ry+len(s) >= 2*len(s)+1: return []
            if b.rx+len(s) < 0 or b.ry+len(s) < 0: return []
            test[b.rx+len(s)][b.ry+len(s)] = 1.0
    if s.plane == 'xz':
        y = 999999
        for b in s:
            if (y==999999): y = b.y
            else:
                if (y != b.y): return []
            #print(str(b.rx) + ', ' + str(b.ry) + ', ' + str(b.rz))
            if b.rx + len(s) >= 2 * len(s) + 1 or b.rz + len(s) >= 2 * len(s) + 1: return []
            if b.rx + len(s) < 0 or b.rz + len(s) < 0: return []
            test[b.rx+len(s)][b.rz+len(s)] = 1.0
    if s.plane == 'zy':
        x = 999999
        for b in s:
            if (x == 999999): x = b.x
            else:
                if(x != b.x): return []
            #print(str(b.rx) + ', ' + str(b.ry) + ', ' + str(b.rz))
            if b.ry + len(s) >= 2 * len(s) + 1 or b.rz + len(s) >= 2 * len(s) + 1: return []
            if b.ry + len(s) < 0 or b.rz + len(s) < 0: return []
            test[b.ry+len(s)][b.rz+len(s)] = 1.0

    #print("FULL")
    #print(test)
    r = get_rectangle(test)
    #print("RECTANGLE FOUND")
    #print(r)
    return r

#gets the rectangles of a matrix - Prabhat Jha (https://www.geeksforgeeks.org/find-rectangles-filled-0/)
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
                findend(i, j, s, out, index)
    return out

#get_rectangle help function - Prabhat Jha (https://www.geeksforgeeks.org/find-rectangles-filled-0/)
def findend(i, j, s, out, index):
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

def shapes_cost2(shapes):
    alpha = 1.5
    cost = (1+dl(shapes))*alpha
    for s in shapes:
        cost = cost + shape_cost(s)
    return cost

def shapes_cost(shapes):
    alpha = 1.25
    cost = (1+dl(shapes))**alpha
    for s in shapes:
        cost = cost + shape_cost(s)
    return cost

#cost function of a shape: entropy, hamming distance and MDL
def shape_cost(s):
    return entropy(s)

#returns the entropy of a shape
def entropy(s):
    nb = len(s)
    entropy = 0
    prob = []
    # sum block types = for
    for b in s:
        add_block(nb, prob, b.id, b.dmg)
    #Probability of certain block type * log of prob
    for p in prob:
        entropy = entropy + p[2] * math.log(p[2],2)
    entropy = - entropy
    return entropy

#the description length cost
def dl(shapes):
    return len(shapes)

def hill_climbing(shapes):
    #choose between merge\split of a shape for a better cost
    same = 0
    while(same < 2 ):
        new = choice(shapes)
        #print("OLD")
        #print(shapes)
        #print("NEW")
        #print(new)
        if shapes_cost(new) == shapes_cost(shapes):
            same = same +1
        shapes = new
    #until we reach an optima
    return shapes

def choice(shapes):
    #print("CHOICE")
    #print(shapes)
    cpy = shapes[:]#shapes.copy()
    merge = just_merge(cpy) #best_merge(cpy) #
    #print("CHOICE MERGE")
    #print(merge)
    #print(shapes_cost(merge))
    return merge
    #cpy = shapes[:]
    #split = best_split(cpy)#shapes.copy())
    #print("CHOICE SPLIT")
    #print(split)
    #print(dl(split))
    #print(merge)
    #print(dl(merge))
    #if shapes_cost(merge) > shapes_cost(split):
    #    print("SPLIT WIN")
    #    return split
    #else:
    #   print("MERGE WIN")
    #    return merge

def filter_final_shapes_total(shapes,m):
    final = []
    blocks = []
    for row in m:
        for col in row:
            for b in col:
                #if block is not air
                if b.id != 0:
                    blocks.append(b)
    sort = sorted(shapes, key=len, reverse=True)
    while blocks != []:
        for s in sort:
            if len(final)==0:
                final.append(s)
                for e in s:
                    for b in blocks:
                        if e.id == b.id and e.dmg == b.dmg and e.x == b.x and e.y == b.y and e.z == b.z:
                            blocks.remove(b)

            else:
                go = False
                for e in s:
                    if final_block_check(blocks,e):
                        go  = True
                        break
                if go == True:
                    final.append(s)
                    for e in s:
                        for b in blocks:
                            if e.id == b.id and e.dmg == b.dmg and e.x == b.x and e.y == b.y and e.z == b.z:
                                blocks.remove(b)
    print("FINAL")
    print(final)
    return final

def filter_final_shapes(shapes):
    final = []
    blocks = []
    sort = sorted(shapes, key=len, reverse=True)

    for s in sort:
        if len(final)==0:
            final.append(s)
            for e in s:
                blocks.append(e)
        else:
            go = True
            for e in s:
                if final_block_check(blocks,e):
                    go  = False
                    break
            if go == True:
                final.append(s)
                for e in s:
                    blocks.append(e)
    print("FINAL")
    print(final)
    return final

def final_block_check(blocks,e):
    for b in blocks:
        if e.id == b.id and e.dmg == b.dmg and e.x == b.x and e.y == b.y and e.z == b.z:
            return True
    return False

#Learn the relations between shapes in a shape set
def relation_learning2(shapes):
    print("RELATIONS")
    print(shapes)
    rel =[]
    for s1 in shapes:
        for s2 in shapes:
            if s1.__ne__(s2):
                if contact(s1,s2):
                    rel.append([s1,s2])
    #duplicates
    print("DUPE")
    d = []
    for s1 in shapes:
        for s2 in shapes:
            if (s1.__ne__(s2) and is_duplicate_shape(s1, s2)):
                for r in rel:
                    if r[0].__eq__(s1):
                        d.append([s2,r[1]])
                    if r[0].__eq__(s2):
                        d.append([s1,r[1]])
                    if r[1].__eq__(s1):
                        d.append([r[0], s2])
                    if r[1].__eq__(s2):
                        d.append([r[0], s1])
            print(rel)
    for i in d:
        rel.append(i)
    print("ADDED RULES")
    print(rel)
    new_rel = []
    for elem in rel:
        if elem not in new_rel:
            new_rel.append(elem)
    rel = new_rel
    print("REMOVE DUPE")
    print(rel)
    return rel

#Learn the relations between shapes in a shape set
def relation_learning(shapes):
    print("FIND RELATIONS FOR")
    print(shapes)
    shapesc = []
    for s in shapes:
        shapesc.append(s.copy())
    shapes = shapesc
    shape_dupe_list = []
    for s1 in shapes:
        if(in_shape_dupe_list(s1,shape_dupe_list)):
            continue
        s = []
        s.append(s1)
        for s2 in shapes:
            if (in_shape_dupe_list(s2, shape_dupe_list)):
                continue
            if (s1.__ne__(s2) and is_duplicate_shape(s1, s2)):
                s.append(s2)
        shape_dupe_list.append(s)
    print("DUPE LIST")
    print(shape_dupe_list)

    rel =[]
    for sl1 in shape_dupe_list:
        for sl2 in shape_dupe_list:
            for s1 in sl1:
                for s2 in sl2:
                    if s1.__ne__(s2):
                        if contact(s1,s2):
                            rel.append([sl1,sl2,s1])

    print("ADDED RULES")
    print(rel)
    new_rel = []
    for elem in rel:
        if elem not in new_rel:
            new_rel.append(elem)
    rel = new_rel
    print("REMOVE DUPE")
    print(rel)
    return rel

def in_shape_dupe_list(shape,shape_dupe_list):
    for sl in shape_dupe_list:
        for s in sl:
            if(shape.__eq__(s)):
                return True
    return False

#Direct contact between shapes
def contact(s1,s2):
    for b1 in s1:
        for b2 in s2:
            if distance(b1,b2) == 1:
                return True
    return False

def distance(b1,b2):
    return sqrt(pow((b2.x-b1.x),2)+pow((b2.y-b1.y),2)+pow((b2.z-b1.z),2))

def production2(shapes,rel,n=5):
    print("PRODUCTION")
    final = [random.choice(shapes)]
    w = random.choice(final)
    print(w)
    while n > 0:
        rrel = []
        for r in rel:
            if r[0] == w:
                rrel.append(r)
        if (len(rrel) != 0):
            r = random.choice(rrel)
            #EDIT POSITION OF R[1]
            shape = r[1].copy()
            shape.set_relative(w.f)
            final.append(shape)
            w = shape
        n = n -1
    return final

def production(shapes,rel,n=5):
    print("PRODUCTION")
    #final = [random.choice(shapes)]
    w = random.choice(shapes)
    print(w)
    #c = False
    #wrel = w.f
    #if(w.plane == 'xy'):
    #    w = to_zy(w)
    #    c = True
    #elif(w.plane == 'zy'):
    #    w = to_xy(w)
    #    c = True
    #elif(w.plane == 'xz'):
    #    print("TOP")
    final = [w]
    while n > 0:
        rrel = []
        for r in rel:
            for s in r[0]:
                #HERE
                if s.eq_production(w):
                    rrel.append(r)
        if (len(rrel) != 0):
            r = random.choice(rrel)
            og = r[2]
            r = r[1]
            r = random.choice(r)
            #EDIT POSITION OF R[1]
            print("S")
            print(r)
            shape = r.copy()
            print(shape)
            #if(c):
            #    if (shape.plane == 'xy'):
            #        shape = to_zy(shape)
            #        shape.set_relative(w.f)
            #    elif (shape.plane == 'zy'):
            #        shape = to_xy(shape)
            #        shape.set_relative(w.f)
            #    elif (shape.plane == 'xz'):
            #        #shape.set_relative(wrel)
            #        print("Top")

            #p = [og.f[0]-w.f[0],og.f[1]-w.f[1],og.f[2]-w.f[2]]
            #p = [w.f[0] - og.f[0], w.f[1] - og.f[1], w.f[2] - og.f[2]]
            shape.set_relative(edit_pos_relation(w,og))
            print(shape)
            final.append(shape)
            w = shape
        n = n -1
    return final

def edit_pos_relation(w,og):
    p = [0,0,0]
    if(w.ogf[0] !=og.f[0]):
        p[0] = (w.ogf[0] - og.f[0])
    else:
        p[0] = (w.f[0])
    if(w.ogf[1] !=og.f[1]):
        p[1] = (w.ogf[1] - og.f[1])
    else:
        p[1] = (w.f[1])
    if(w.ogf[2] !=og.f[2]):
        p[2] = (w.ogf[2] - og.f[2])
    else:
        p[2] = (w.f[2])
    print("PPPP")
    print(p)
    return p



#Check if the shape is the same except for location and orientation
def is_duplicate_shape(s1,s2):
    if (len(s1) != len(s2)):
        #print("same")
        return False
    if (s1.plane == s2.plane):
        m = len(s1)
        #FLIP S2 ON FOUR SIDES TO CHECK IF EQUAL
        for b1 in s1:
            for b2 in s2:
                if (b1.id == b2.id and b1.dmg == b2.dmg and b1.rx == b2.rx and b1.ry == b2.ry and b1.rz == b2.rz):
                    m = m-1
                    break
        if (m == 0):
            #print("same plane " + s2.plane)
            return True
    else:
        m = len(s1)
        #FLIP S2 ON FOUR SIDES TO CHECK IF EQUAL
        for b1 in s1:
            for b2 in s2:
                if (b1.id == b2.id and b1.dmg == b2.dmg):
                    if ((s1.plane == 'zy' and s2.plane == 'xy') or (s1.plane == 'xy' and s2.plane == 'zy')):
                        if (b1.rx == b2.rz and b1.ry == b2.ry and b1.rz == b2.rx):
                            m = m - 1
                            break
                    if ((s1.plane == 'xy' and s2.plane == 'xz') or (s1.plane == 'xz' and s2.plane == 'xy')):
                        if  (b1.rx == b2.rx and b1.ry == b2.rz and b1.rz == b2.ry):
                            m = m - 1
                            break
                    if ((s1.plane == 'xz' and s2.plane == 'zy') or (s1.plane == 'zy' and s2.plane == 'xz')):
                        if (b1.rx == b2.ry and b1.ry == b2.rx and b1.rz == b2.rz):
                            m = m - 1
                            break
        if (m == 0):
            #print(s2.plane)
            return True
    #print(s2.plane)
    return False

#def flip(shape):

#EDIT RELATIVE HERE?
def to_xz(s):
    if(s.plane == 'xz'): return s.copy()
    if(s.plane == 'xy'):
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.z
            b.z = temp
        sd.plane = 'xz'
        sd.set_relative([sd.list[0].x,sd.list[0].y,sd.list[0].z])
        return sd
    if (s.plane == 'zy'):
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.x
            b.x = temp
        sd.plane = 'xz'
        sd.set_relative([sd.list[0].x,sd.list[0].y,sd.list[0].z])
        return s
def to_xy(s):
    if (s.plane == 'xy'): return s.copy()
    if(s.plane == 'xz'):
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.z
            b.z = temp
        sd.plane = 'xy'
        sd.set_relative([sd.list[0].x,sd.list[0].y,sd.list[0].z])
        return sd
    if (s.plane == 'zy'):
        sd = s.copy()
        for b in sd:
            temp = b.z
            b.z = b.x
            b.x = temp
        sd.plane = 'xy'
        sd.set_relative([sd.list[0].x,sd.list[0].y,sd.list[0].z])
        return sd
def to_zy(s):
    if (s.plane == 'zy'): return s.copy()
    if(s.plane == 'xz'):
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.x
            b.x = temp
        sd.plane = 'zy'
        sd.set_relative([sd.list[0].x,sd.list[0].y,sd.list[0].z])
        return sd
    if(s.plane == 'xy'):
        sd = s.copy()
        for b in sd:
            temp = b.z
            b.z = b.x
            b.x = temp
        sd.plane = 'zy'
        sd.set_relative([sd.list[0].x,sd.list[0].y,sd.list[0].z])
        return sd



def main():
    shapes3m3m3 =[]
    main_shape_append(shapes3m3m3,Block(3, 0, 0, 0, 0))
    main_shape_append(shapes3m3m3,Block(3, 0, 0, 1, 0))
    main_shape_append(shapes3m3m3,Block(3, 0, 0, 2, 0))
    main_shape_append(shapes3m3m3, Block(4, 0, 0, 3, 0))
    main_shape_append(shapes3m3m3, Block(4, 0, 0, 4, 0))
    main_shape_append(shapes3m3m3,Block(3, 0, 1, 0, 0))
    main_shape_append(shapes3m3m3,Block(1, 0, 1, 1, 0))
    main_shape_append(shapes3m3m3,Block(3, 0, 1, 2, 0))
    main_shape_append(shapes3m3m3, Block(4, 0, 1, 3, 0))
    main_shape_append(shapes3m3m3, Block(4, 0, 1, 4, 0))
    main_shape_append(shapes3m3m3,Block(20, 0, 2, 0, 0))
    main_shape_append(shapes3m3m3,Block(20, 0, 2, 1, 0))
    main_shape_append(shapes3m3m3,Block(20, 0, 2, 2, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 2, 3, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 2, 4, 0))
    main_shape_append(shapes3m3m3,Block(20, 0, 3, 0, 0))
    main_shape_append(shapes3m3m3,Block(20, 0, 3, 1, 0))
    main_shape_append(shapes3m3m3,Block(20, 0, 3, 2, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 3, 3, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 3, 4, 0))
    shapesb = []
    main_shape_append(shapesb,Block(20, 0, 0, 0, 0))
    main_shape_append(shapesb,Block(20, 0, 0, 1, 0))
    main_shape_append(shapesb,Block(20, 0, 0, 2, 0))
    main_shape_append(shapesb,Block(20, 0, 0, 3, 0))
    main_shape_append(shapesb,Block(4, 0, 1, 0, 0))
    main_shape_append(shapesb,Block(4, 0, 1, 1, 0))
    main_shape_append(shapesb,Block(4, 0, 1, 2, 0))
    main_shape_append(shapesb,Block(4, 0, 1, 3, 0))
    shapes = shapesb
    shapes = hill_climbing(shapes)
    print(shapes)
    shapes = filter_final_shapes(shapes)
    print(shapes)
    print(shapes_cost(shapes))
    rel = relation_learning(shapes)
    print(rel)
    final = production(shapes,rel)
    print(final)
    return

def main_shape_append(shapes,b):
    shapes.append(Shape(b,'xz'))
    shapes.append(Shape(b, 'xy'))
    shapes.append(Shape(b, 'zy'))

if __name__ == "__main__":
    main()