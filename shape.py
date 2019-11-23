import numpy as np
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
import math as math
from  itertools import combinations

class Block:
    def __init__(self, blockid, dmg, x, y, z):
        self.id = blockid
        self.dmg = dmg
        self.x = x
        self.y = y
        self.z = z
        self.used = False
        self.rx = x
        self.ry = y
        self.rz = z

    def __float__(self):
        return float(self.id + float(self.dmg)/100)
    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(float(self.id + float(self.dmg) / 100))
        #return '('+str(self.id)+', '+str(self.dmg)+') at ('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'

    def set_used(self,b):
        self.used = b

    def set_relative(self,f):
        self.rx = self.x-f[0]
        self.ry = self.y-f[1]
        self.rz = self.z-f[2]

class Shape:
    def __init__(self,b,plane):
        self.list = []
        self.plane = plane
        self.f = [b.x,b.y,b.z]
        self.append(b)

    #def __init__(self,b,plane,f):
    #    self.list = []
    #    self.plane = plane
    #    self.f = f
    #    self.append(b)

    def __iter__(self):
        for b in self.list:
            yield b

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, item):
        return self.list[item]

    def copy(self):
        s = Shape(self.list[0], self.plane) #self.f
        s.list = self.list
        return s

    def extend(self,s):
        for b in s:
            self.append(b)

    def append(self,b):
        bn = (Block(b.id,b.dmg,b.x,b.y,b.z))
        bn.set_relative(self.f)
        #b.set_relative(self.f)
        self.list.append(bn) #(Block(b.id,b.dmg,b.x,b.y,b.z))

    def get_relative(self,item):
        #b = self.list[item]
        b = item
        print("RELATIVE")
        print('(' + str(self.f[0]) + ', ' + str(self.f[1]) + ', ' + str(self.f[2]) + ')')
        print('(' + str(b.x) + ', ' + str(b.y) + ', ' + str(b.z) + ')')
        return Block(b.id, b.dmg, b.x - self.f[0], b.y - self.f[1], b.z - self.f[2])

#HILL CLIMBING ALGO...

#extends a shape
def extend_shape(s,plane):
    dx, dy, dzx, dzy = 0, 0, 0, 0
    #we have xy, xz and zy planes
    if plane == 'xy':
        dx = 1
        dy = 1
    if plane == 'xz':
        dx = 1
        dzy = 1
    if plane == 'zy':
        dzx = 1
        dy = 1
    p = check_pos(m,b.x + dx,b.y,b.z + dzx)
    if p.id != 0:
        s, m = match_rect(p,m,plane)
        shape.extend(s)

    p = check_pos(m,b.x - dx,b.y,b.z - dzx)
    if p.id != 0:
        s, m = match_rect(p,m,plane)
        shape.extend(s)

    p = check_pos(m,b.x,b.y + dy,b.z + dzy)
    if p.id != 0:
        s, m = match_rect(p,m,plane)
        shape.extend(s)

    p = check_pos(m,b.x,b.y - dy,b.z - dzy)
    if p.id != 0:
        s, m = match_rect(p,m,plane)
        shape.extend(s)
    return s

#merges two shapes into one
def merge_shape(s1,s2):
    m = s1.copy()
    m.extend(s2)
    if is_rect(m):
        return m
    return s1

#splits a shape into two shapes - find the best split as well
def split_shape(s):
    #r = find_rect(s)
    subshapes = sublists(s)
    print(subshapes)
    possible_splits = []
    for sub in subshapes:
        print("SUB")
        print(sub)
        if is_rect(sub[0]) and is_rect(sub[1]):
            print("BOTH RECT")
            possible_splits.append(sub)
    print("POSSIBLE")
    print(possible_splits)
    return

def sublists(s):
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

def sub_shapes(s):
    subshapes = [[]]
    e = True
    for i in range(len(s)+1):
        for j in range(i + 1, len(s)):
            sub = s[i:j]
            subs = Shape(sub[0],s.plane) #Shape(sub[0],s.plane,[sub[0].x,sub[0].y,sub[0].z])
            subs.extend(sub[1:])
            sob = [a for a in s if a not in sub]
            sobs = Shape(sob[0],s.plane) #Shape(sob[0],s.plane,[sob[0].x,sob[0].y,sob[0].z])
            sobs.extend(sob[1:])
            subsob = [subs,sobs]
            if e:
                subshapes[0] = subsob
                e = False
            else:
                subshapes.append(subsob)
    return subshapes

def is_rect(s):
    r = find_rect(s)
    if len(r) == 1:
        if abs(1 + r[0][2] - r[0][0]) * abs(1 + r[0][3] - r[0][1]) == len(s):
            return True
    return False

#find the shape rectangles
def find_rect(s):
    print("PLANE")
    print(s.plane)
    test = np.zeros((2*len(s)+1,2*len(s)+1))
    print(s)
    print(s.f)

    if s.plane == 'xy':
        for b in s:
            #print(str(b.x) + ', ' + str(b.y) + ', ' + str(b.z))
            #print(str(b.rx) + ', ' + str(b.ry) + ', ' + str(b.rz))
            test[b.rx+len(s)][b.ry+len(s)] = 1.0
    if s.plane == 'xz':
        for b in s:
            #print(str(b.rx) + ', ' + str(b.ry) + ', ' + str(b.rz))
            test[b.rx+len(s)][b.rz+len(s)] = 1.0
    if s.plane == 'zy':
        for b in s:
            #print(str(b.rx) + ', ' + str(b.ry) + ', ' + str(b.rz))
            test[b.ry+len(s)][b.rz+len(s)] = 1.0

    print("FULL")
    print(test)

    r = get_rectangle(test)
    print("RECTANGLE FOUND")
    print(r)
    return r


def findend(i, j, s, out, index):
    x = len(s)
    y = len(s[0])

    # flag to check column edge case,
    # initializing with 0
    flagc = 0

    # flag to check row edge case,
    # initializing with 0
    flagr = 0

    for m in range(i, x):

        # loop breaks where first 1 encounters
        if s[m][j] == 0:
            flagr = 1  # set the flag
            break

        # pass because already processed
        if s[m][j] == 5:
            pass

        for n in range(j, y):

            # loop breaks where first 1 encounters
            if s[m][n] == 0:
                flagc = 1  # set the flag
                break

            # fill rectangle elements with any
            # number so that we can exclude
            # next time
            s[m][n] = 5

    if flagr == 1:
        out[index].append(m - 1)
    else:
        # when end point touch the boundary
        out[index].append(m)

    if flagc == 1:
        out[index].append(n - 1)
    else:
        # when end point touch the boundary
        out[index].append(n)


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

#cost function
def cost(s):
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
    print(prob)
    for p in prob:
        entropy = entropy + p[2] * math.log(p[2],2)
    entropy = - entropy
    return entropy

def hamming_distance(s):
    return

def main():
    print("MERGE")
    s = Shape(Block(20,0,0,0,0),'xy')
    s.append(Block(21,0,1,0,0))
    #s.append(Block(22,0,2,0,0))
    s2 = Shape(Block(30,0,0,1,0),'xy')
    s2.append(Block(31,0,1,1,0))
    #s2.append(Block(32,0,2,1,0))
    find_rect(s2)
    m = merge_shape(s,s2)
    print(m)
    print("SPLIT")
    #print(sub_shapes(s))
    #print(sublists(s))
    split_shape(m)
    return

if __name__ == "__main__":
    main()