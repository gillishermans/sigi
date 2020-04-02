import numpy as np
from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
import math as math
from itertools import combinations
import itertools
import random

# Based on A* implementation by Nicholas Swift.
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return str(self.position)

# Searches for path to all ends. Based on A* implementation by Nicholas Swift.
def search_for_3d(shapes_space,shapes,ends):

    found = [[0 for col in range(2)] for row in range(len(shapes))]
    print(found)

    end_nodes = []
    for e in ends:
        end_node = Node(None, e[0])
        end_node.g = end_node.h = end_node.f = 0
        start_node = Node(None, e[1])
        start_node.g = start_node.h = start_node.f = 0
        end_nodes.append([end_node,start_node])
    print(ends)
    print(end_nodes)
    start_node = Node(None, [0, 0, 0])
    start_node.g = start_node.h = start_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    print("Open list")
    print(open_list)

    # Loop until you find the end
    while len(open_list) > 0:
        #print(open_list)
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        #if current_node == end_node:
        #    return True
        i = 0
        for e in end_nodes:
            if current_node == e[0]:
                found[i][0] = 1
                print("found",found)
            if current_node == e[1]:
                found[i][1] = 1
                print("found",found)
            i += 1

        # Generate children
        children = []
        for new_position in [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]:#[(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = [current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2]]

            # Make sure within range
            if node_position[0] > (len(shapes_space) - 1) or node_position[0] < 0 or\
               node_position[1] > (len(shapes_space[len(shapes_space)-1]) -1) or node_position[1] < 0 or\
               node_position[2] > len(shapes_space[0][0]) -1 or node_position[2] < 0:
                continue

            # Make sure walkable terrain
            if shapes_space[node_position[0]][node_position[1]][node_position[2]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            c = False
            for closed_child in closed_list:
                if child == closed_child:
                    c = True
            if c: continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = 0 #5*((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            c = False
            for open_node in open_list:
                if child == open_node: #and child.g > open_node.g:
                    c = True
            if c: continue

            # Add the child to the open list
            open_list.append(child)
            #print(child)

    remove = []
    i = 0
    for f in found:
        if f[0] == 1 and f[1] == 1:
            remove.append(shapes[i])
        i += 1
    return remove

# Searches for path to all ends. Based on A* implementation by Nicholas Swift.
def search_for(shapes_space,shapes,ends):

    found = [[0 for col in range(2)] for row in range(len(shapes))]
    print(found)

    end_nodes = []
    for e in ends:
        end_node = Node(None, e[0])
        end_node.g = end_node.h = end_node.f = 0
        start_node = Node(None, e[1])
        start_node.g = start_node.h = start_node.f = 0
        end_nodes.append([end_node,start_node])
    print(ends)
    print(end_nodes)
    start_node = Node(None, [0, 0])
    start_node.g = start_node.h = start_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    print("Open list")
    print(open_list)

    # Loop until you find the end
    while len(open_list) > 0:
        #print(open_list)
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        #if current_node == end_node:
        #    return True
        i = 0
        for e in end_nodes:
            if current_node == e[0]:
                found[i][0] = 1
                print("found",found)
            if current_node == e[1]:
                found[i][1] = 1
                print("found",found)
            i += 1

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = [current_node.position[0] + new_position[0], current_node.position[1] + new_position[1]]

            # Make sure within range
            if node_position[0] > (len(shapes_space) - 1) or node_position[0] < 0 or node_position[1] > (len(shapes_space[len(shapes_space)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if shapes_space[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            c = False
            for closed_child in closed_list:
                if child == closed_child:
                    c = True
            if c: continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = 0 #5*((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            c = False
            for open_node in open_list:
                if child == open_node: #and child.g > open_node.g:
                    c = True
            if c: continue

            # Add the child to the open list
            open_list.append(child)
            #print(child)

    remove = []
    i = 0
    for f in found:
        if f[0] == 1 and f[1] == 1:
            remove.append(shapes[i])
        i += 1
    return remove


def build_production_space_3d(shapes):
    minx = 99999999
    maxx = 0
    miny = 99999999
    maxy = 0
    minz = 99999999
    maxz = 0
    for s in shapes:
        for b in s:
            if b.x < minx: minx = b.x
            if b.x > maxx: maxx = b.x
            if b.y < miny: miny = b.y
            if b.y > maxy: maxy = b.y
            if b.z < minz: minz = b.z
            if b.z > maxz: maxz = b.z
    print(minx)
    print(maxx)
    print(miny)
    print(maxy)
    print(minz)
    print(maxz)
    space = [[[0 for e in range(maxz-minz+3)] for col in range(maxy-miny+2)] for row in range(maxx-minx+3)]
    print(space)
    print(len(space))
    print(len(space[0]))
    print(len(space[0][0]))
    for s in shapes:
        for b in s:
            #print(b.x - minx)
            #print(b.z - minz)
            space[b.x - minx+1][b.y - miny][b.z - minz+1] = b.id
            #print(space)
    for s in space:
        print(s)
    return space, minx, miny, minz

def build_production_space(shapes):
    minx = 99999999
    maxx = 0
    minz = 99999999
    maxz = 0
    for s in shapes:
        for b in s:
            #if b.y > 1: continue
            if b.x < minx: minx = b.x
            if b.x > maxx: maxx = b.x
            if b.z < minz: minz = b.z
            if b.z > maxz: maxz = b.z
    print(minx)
    print(maxx)
    print(minz)
    print(maxz)
    space = [[0 for col in range(maxz-minz+3)] for row in range(maxx-minx+3)]
    print(space)
    for s in shapes:
        for b in s:
            if b.y > 1: continue
            #print(b.x - minx)
            #print(b.z - minz)
            space[b.x - minx+1][b.z - minz+1] = b.id
            #print(space)
    for s in space:
        print(s)
    return space, minx, minz

# Find all enclosures in just one path finding sweep.
def enclosure_update_3d(shapes):
    shapes_space, minx, miny, minz = build_production_space_3d(shapes)
    ends = []
    for s in shapes:
        start = []
        end = []
        if s.plane == 'xy':
            for i in range(len(s.list)):
                start = [s.list[i].x - minx + 1, s.list[i].y - miny, s.list[i].z + 1 - minz + 1]
                end = [s.list[i].x - minx + 1, s.list[i].y - miny, s.list[i].z - 1 - minz + 1]
                if shapes_space[start[0]][start[1]][start[2]] == 0 and shapes_space[end[0]][end[1]][end[2]] == 0: break
        elif s.plane == 'xz':
            for i in range(len(s.list)):
                start = [s.list[i].x - minx + 1, s.list[i].y + 1 - miny, s.list[i].z - minz + 1]
                end = [s.list[i].x - minx + 1, s.list[i].y - 1 - miny, s.list[i].z - minz + 1]
                if shapes_space[start[0]][start[1]][start[2]] == 0 and shapes_space[end[0]][end[1]][end[2]] == 0: break
        elif s.plane == 'zy':
            for i in range(len(s.list)):
                start = [s.list[i].x + 1 - minx + 1, s.list[i].y - miny, s.list[i].z - minz + 1]
                end = [s.list[i].x - 1 - minx + 1, s.list[i].y - miny, s.list[i].z - minz + 1]
                if shapes_space[start[0]][start[1]][start[2]] == 0 and shapes_space[end[0]][end[1]][end[2]] == 0: break
        ends.append([start, end])
    remove = search_for_3d(shapes_space, shapes, ends)
    print("Not enclosed: ")
    print(remove)
    return [x for x in shapes if not remove.__contains__(x)]

# Find all enclosures in just one path finding sweep.
def enclosure_update(shapes):
    shapes_space, minx, minz = build_production_space(shapes)
    ends = []
    for s in shapes:
        start = []
        end = []
        if s.plane == 'xy':
            for i in range(len(s.list)):
                start = [s.list[i].x - minx + 1, s.list[i].z + 1 - minz + 1]
                end = [s.list[i].x - minx + 1, s.list[i].z - 1 - minz + 1]
                if shapes_space[start[0]][start[1]] == 0 and shapes_space[end[0]][end[1]] == 0: break

        elif s.plane == 'xz':
            continue
        elif s.plane == 'zy':
            for i in range(len(s.list)):
                start = [s.list[i].x + 1 - minx + 1, s.list[i].z - minz + 1]
                end = [s.list[i].x - 1 - minx + 1, s.list[i].z - minz + 1]
                if shapes_space[start[0]][start[1]] == 0 and shapes_space[end[0]][end[1]] == 0: break
        ends.append([start, end])
    remove = search_for(shapes_space, [x for x in shapes if x.plane != 'xz'], ends)
    print("Not enclosed: ")
    print(remove)
    return [x for x in shapes if not remove.__contains__(x)]

# Updates the shape set by deleting non enclosed shapes.
def enclosure_update_old(shapes):
    remove = []
    shapes_space, minx, minz = build_production_space(shapes)
    for s in shapes:
        #Find start (one side of shape)
        #Find end (other side of shape)
        start = []
        end = []
        if s.plane == 'xy':
            #start = [s.list[0].x,s.list[0].y,s.list[0].z + 1]
            #end = [s.list[0].x, s.list[0].y, s.list[0].z - 1]
            for i in range(len(s.list)):
                start = [s.list[i].x - minx + 1, s.list[i].z + 1 - minz + 1]
                end = [s.list[i].x - minx + 1, s.list[i].z - 1 - minz + 1]
                if shapes_space[start[0]][start[1]] == 0 and shapes_space[end[0]][end[1]] == 0: break

        elif s.plane == 'xz':
            #start = [s.list[0].x, s.list[0].y + 1, s.list[0].z]
            #end = [s.list[0].x, s.list[0].y - 1, s.list[0].z]
            continue
        elif s.plane == 'zy':
            #start = [s.list[0].x + 1, s.list[0].y, s.list[0].z]
            #end = [s.list[0].x - 1, s.list[0].y, s.list[0].z]
            for i in range(len(s.list)):
                start = [s.list[i].x + 1 - minx + 1, s.list[i].z - minz + 1]
                end = [s.list[i].x - 1 - minx + 1, s.list[i].z - minz + 1]
                if shapes_space[start[0]][start[1]] == 0 and shapes_space[end[0]][end[1]] == 0: break

        print("Find path")
        print(start)
        print(end)
        if astar(shapes_space,start,end):
            print("Found a path.")
            remove.append(s)
    print("Not enclosed: ")
    print(remove)
    return [x for x in shapes if not remove.__contains__(x)]



# Updates a list of probabilities for blocks.
def add_block(nb, prob, blockid, dmg):
    for b in prob:
        if b[0] == blockid and b[3] == dmg:
            b[1] = b[1] + 1.0
            b[2] = b[1] / nb
            return
    prob.append([blockid, 1.0, 1.0 / nb, dmg])


# A single block class
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

    def compare_eq(self, other):
        if self.id == other.id and self.dmg == other.dmg and self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else: return False

    def __float__(self):
        return float(self.id + float(self.dmg) / 100)

    def __repr__(self):
        return str(self)

    def __str__(self):
        # return str(float(self.id + float(self.dmg) / 100)) + " pos (" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"+ " rel pos (" + str(self.rx) + "," + str(self.ry) + "," + str(self.rz) + ")"
        return str(float(self.id + float(self.dmg) / 100)) + " rel pos (" + str(self.rx) + "," + str(self.ry) + "," +str(self.rz) + ")"
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

    def __iter__(self):
        for b in self.list:
            yield b

    def __eq__(self, other):
        if self.plane == other.plane and self.f == other.f and self.list == other.list:
            return True
        else:
            return False

    def compare_eq(self,other):
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
        self.f = [self.f[0] - p[0], self.f[1] - p[1], self.f[2] - p[2]]
        for b in self.list:
            b.x = b.x - p[0]
            b.y = b.y - p[1]
            b.z = b.z - p[2]
            b.set_relative(self.f)

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


# Compare two shape sets and return a score for their similarity.
def similarity_shape_sets(default,shapes):
    score = 0.0
    nb = len(default)
    if len(default) == len(shapes):
        for d in default:
            for s in shapes:
                if d.compare_eq(s):
                    score = score + 1.0
                    #Found the matching s with d
                    break
    score = (score / nb)
    return score


# Return the similarity of two shapes.
#def similarity_shapes(d,s):




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
        if (s.eq_production(sr)):
            tr.append(s)
            break
    for r in tr:
        shapes.remove(r)
    return shapes


# Returns the first merge that decreased the cost.
def just_merge(shapes, prev_cost, cost_function=0, alpha=1.1):
    shapes = copy_shapes(shapes)
    # random.shuffle(shapes)
    for s1 in shapes:
        # if (len(s1) > 25): continue
        for s2 in shapes:
            # if (len(s2) > 25): continue
            if s1.__ne__(s2) and s1.plane == s2.plane:
                s = merge_shape(s1, s2)
                if not is_rect(s):
                    continue
                new_shapes = [x for x in shapes if x != s1 and x != s2]
                new_shapes.append(s)
                new_cost = shapes_cost(new_shapes, cost_function, alpha)
                if prev_cost - new_cost >= 0:
                    return new_shapes, new_cost
    return shapes, prev_cost


# Returns the best possible merge for a set of shapes
def best_merge(shapes, prev_cost, cost_function=0, alpha=1.1):
    saved_cost = 0
    best = []
    for s1 in shapes:
        # if(len(s1) > 9): continue
        for s2 in shapes:
            # if (len(s2) > 9): continue
            if s1.__ne__(s2) and s1.plane == s2.plane:
                s = merge_shape(s1, s2)
                if not is_rect(s):
                    continue
                new_shapes = [x for x in shapes if x != s1 and x != s2]
                new_shapes.append(s)
                saved = prev_cost - shapes_cost(new_shapes, cost_function, alpha)
                if saved >= saved_cost:
                    saved_cost = saved
                    best = new_shapes
    if len(best) == 0:
        return shapes, prev_cost
    return best, saved_cost


# Merges two shapes into one.
def merge_shape(s1, s2):
    m = s1.copy()
    m.extend(s2)
    return m


# [NOT WORKING] Split post processing for finding duplicate shapes inside one larger shape
def post_split1(shapes):
    splits = []
    for s in shapes:
        if len(s) % 2 != 0:
            continue
        subshapes = sub_shapes(s)
        print(subshapes)
        possible_splits = []
        for sub in subshapes:
            if len(sub[0]) == len(sub[1]) and is_rect(sub[0]) and is_rect(sub[1]):
                possible_splits.append(sub)
        print(possible_splits)
        for split in possible_splits:
            if (s.__eq__(split[0]) and s.__eq__(split[1])):
                continue
            if is_duplicate_shape(split[0], split[1]):
                splits.append([s, split[0], split[1]])
                print([s, split[0], split[1]])
        print("None for this shape")
    for split in splits:
        shapes.remove(s)
        shapes.append(split[0])
        shapes.append(split[1])
    return shapes


# [WORKS FOR Y-HALF SPLITS - NOTHING MORE] Split post processing for finding duplicate shapes inside one larger shape
def post_split(shapes):
    splits = []
    print("POST")
    prev_cost = shapes_cost(shapes)
    print("old cost")
    print(prev_cost)
    print(shapes)
    for s in shapes:
        if len(s) % 2 != 0 or s.plane == 'xz':
            continue
        s1, s2 = half_splits(s)
        if (len(s1) == 0 or len(s2) == 0):
            continue
        new_shapes = copy_shapes(shapes)
        remove_copy(new_shapes, s)
        new_shapes.append(s1)
        new_shapes.append(s2)
        print("new cost")
        print(shapes_cost1(new_shapes))
        if is_duplicate_shape(s1, s2):
            splits.append([s, s1, s2])
        elif prev_cost - shapes_cost(new_shapes) >= 0:
            splits.append([s, s1, s2])
    for split in splits:
        remove_copy(shapes, split[0])
        shapes.append(split[1])
        shapes.append(split[2])
    print("POST")
    print(shapes)
    return shapes


# [WORKS FOR Y-HALF SPLITS - NOTHING MORE] Splits the shape in half.
def half_splits(s):
    minh = 0
    maxh = 0
    for b in s:
        if (minh == 0 and maxh == 0):
            minh = b.y
            maxh = b.y
        elif (b.y < minh):
            minh = b.y
        elif (b.y > maxh):
            maxh = b.y
    split = (maxh - minh) / 2
    s1 = []
    s2 = []
    for b in s:
        if (b.y <= split):
            s1.append(b)
        else:
            s2.append(b)
    if (len(s1) == 0 or len(s2) == 0):
        return s1, s2
    h1 = shape_from_blocks(s1, s.plane)
    h2 = shape_from_blocks(s2, s.plane)
    return h1, h2


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
                print(i)
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


def just_split(shapes):
    new_cost = 0
    for s in shapes:
        split = split_shape(s)
        if (s.__eq__(split[0]) and s.__eq__(split[1])):
            continue
        if shape_cost(s) - (shape_cost(split[0]) + shape_cost(split[1])) > 0:
            saved_cost = shape_cost(s) - (shape_cost(split[0]) + shape_cost(split[1]))
            best = [s, split[0], split[1]]
            break
    if len(best) == 0:
        return shapes
    shapes.remove(s)
    shapes.append(split[0])
    shapes.append(split[1])
    return shapes


# Returns the best possible split for a set of shapes
def best_split(shapes):
    saved_cost = 0
    best = []
    for s in shapes:
        split = split_shape(s)
        if (s.__eq__(split[0]) and s.__eq__(split[1])):
            continue
        if shape_cost(s) - (shape_cost(split[0]) + shape_cost(split[1])) > saved_cost:
            saved_cost = shape_cost(s) - (shape_cost(split[0]) + shape_cost(split[1]))
            best = [s, split[0], split[1]]
    if len(best) == 0:
        return shapes
    shapes.remove(s)
    shapes.append(split[0])
    shapes.append(split[1])
    return shapes


# splits a shape into two shapes - find the best split according to the minimal cost of the shapes
def split_shape(s):
    # r = find_rect(s)
    subshapes = sub_shapes(s)
    # print(subshapes)
    possible_splits = []
    for sub in subshapes:
        # print("SUB")
        # print(sub)
        if is_rect(sub[0]) and is_rect(sub[1]):
            possible_splits.append(sub)
    # print("POSSIBLE")
    # print(possible_splits)
    # print(s)
    best = [s, s]
    cost = shape_cost(best[0])
    # print("COST")
    # print(cost)
    for i in range(0, len(possible_splits)):
        # print("COSTif")
        # print(shape_cost(possible_splits[i][0]) + shape_cost(possible_splits[i][1]))
        if shape_cost(possible_splits[i][0]) + shape_cost(possible_splits[i][1]) < cost:
            best = possible_splits[i]
            cost = shape_cost(best[0]) + shape_cost(best[1])
    return best


# finds the sub_shape combinations for a certain shape
def sub_shapes_new(s):
    subshapes = []
    sub = []
    size = len(s)
    comb = combinations(s, size / 2)
    for c in comb:
        # print(c)
        if len(c) == 1:
            sub.append([c[0]])
        else:
            l = []
            for e in c:
                l.append(e)
            sub.append(l)
    for i in range(0, len(sub)):
        subs = Shape(sub[i][0], s.plane)
        subs.extend(sub[i][1:])
        sob = [a for a in s if a not in sub[i]]
        sobs = Shape(sob[0], s.plane)
        sobs.extend(sob[1:])
        subsob = [subs, sobs]
        subshapes.append(subsob)
    return subshapes


# finds the sub_shape combinations for a certain shape
def sub_shapes(s):
    subshapes = []
    sub = []
    for i in range(1, len(s)):
        comb = combinations(s, i)
        for c in comb:
            # print(c)
            if len(c) == 1:
                sub.append([c[0]])
            else:
                l = []
                for e in c:
                    l.append(e)
                sub.append(l)
    for i in range(0, len(sub)):
        subs = Shape(sub[i][0], s.plane)
        subs.extend(sub[i][1:])
        sob = [a for a in s if a not in sub[i]]
        sobs = Shape(sob[0], s.plane)
        sobs.extend(sob[1:])
        subsob = [subs, sobs]
        subshapes.append(subsob)
    return subshapes


# Returns true if a shape is a rectangle.
def is_rect(s):
    r = find_rect(s)
    if len(r) == 1:
        if abs(1 + r[0][2] - r[0][0]) * abs(1 + r[0][3] - r[0][1]) == len(s):
            return True
    return False


# find the shape rectangles
def find_rect(s):
    test = np.zeros((2 * len(s) + 1, 2 * len(s) + 1))

    if s.plane == 'xy':
        z = 999999
        for b in s:
            if (z == 999999):
                z = b.z
            else:
                if (z != b.z): return []
            if b.rx + len(s) >= 2 * len(s) + 1 or b.ry + len(s) >= 2 * len(s) + 1: return []
            if b.rx + len(s) < 0 or b.ry + len(s) < 0: return []
            test[b.rx + len(s)][b.ry + len(s)] = 1.0
    if s.plane == 'xz':
        y = 999999
        for b in s:
            if (y == 999999):
                y = b.y
            else:
                if (y != b.y): return []
            # print(str(b.rx) + ', ' + str(b.ry) + ', ' + str(b.rz))
            if b.rx + len(s) >= 2 * len(s) + 1 or b.rz + len(s) >= 2 * len(s) + 1: return []
            if b.rx + len(s) < 0 or b.rz + len(s) < 0: return []
            test[b.rx + len(s)][b.rz + len(s)] = 1.0
    if s.plane == 'zy':
        x = 999999
        for b in s:
            if (x == 999999):
                x = b.x
            else:
                if (x != b.x): return []
            # print(str(b.rx) + ', ' + str(b.ry) + ', ' + str(b.rz))
            if b.ry + len(s) >= 2 * len(s) + 1 or b.rz + len(s) >= 2 * len(s) + 1: return []
            if b.ry + len(s) < 0 or b.rz + len(s) < 0: return []
            test[b.ry + len(s)][b.rz + len(s)] = 1.0
    r = get_rectangle(test)
    return r


# gets the rectangles of a matrix - Prabhat Jha (https://www.geeksforgeeks.org/find-rectangles-filled-0/)
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


# get_rectangle help function - Prabhat Jha (https://www.geeksforgeeks.org/find-rectangles-filled-0/)
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
        cost = cost + shape_cost(s)
    for s in to_remove:
        cost = cost + shape_cost(s)

    return cost


# Returns the cost of the given set of shapes.
def shapes_cost(shapes, cost_function=0, alpha = 1.1):
    if cost_function == 0:
        cost = (1.0 + dl(shapes)) * alpha
        for s in shapes:
            cost = cost + shape_cost(s)
        return cost
    else:
        #alpha = 150
        cost = (1 + dl(shapes)) * alpha
        for s in shapes:
            cost = cost + other_entropy(s)
        return cost


# Cost function of a shape: entropy (and hamming distance - maybe later).
def shape_cost(s):
    return entropy(s)  # other_entropy(s)


# Returns the entropy of a shape.
def entropy(s):
    nb = len(s)
    e = 0
    prob = []
    # sum block types = for
    for b in s:
        add_block(nb, prob, b.id, b.dmg)
    # Probability of certain block type * log of prob
    for p in prob:
        e = e + p[2] * math.log(p[2], 2)
    e = - e
    return e + 0.00001


# returns the entropy of a shape
def other_entropy(s):
    nb = len(s)
    e = 0
    prob = []
    # sum block types = for
    for b in s:
        add_block(nb, prob, b.id, b.dmg)
    # Probability of certain block type * log of prob
    for p in prob:
        e = e + p[2] * math.log(p[2], 2)
    e = - e*math.exp(len(prob))
    return e


# The description length of a set of shapes.
def dl(shapes):
    return len(shapes)


# Perform the hill climbing algorithm on a set of shapes.
def hill_climbing(shapes, cost_function=0, alpha=1.1):
    same = 0
    prev_shape_cost = 99999999
    while same < 2:
        # choice
        cpy = shapes[:]  # shapes.copy()
        new, cost = just_merge(cpy, prev_shape_cost, cost_function, alpha)  # best_merge(cpy) #
        if cost == prev_shape_cost:
            same = same + 1
        shapes = new
        prev_shape_cost = cost
    # until we reach an optima
    # same = 0
    # while(same < 2 ):
    #    #choice
    #    cpy = shapes[:]  # shapes.copy()
    #    new = just_split(cpy)
    #    if shapes_cost(shapes) == shapes_cost(new):
    #       same = same +1
    #    shapes = new
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
                if go == True:
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


# Learn the relations between shapes in a shape set.
def relation_learning(shapes):
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
    rel = []
    copy = copy_shapes(shapes)
    for sl1 in shape_dupe_list:
        for s1 in sl1:
            for s2 in copy:
                if s1.__ne__(s2):
                    if contact(s1, s2):
                        rel.append([sl1, s2, s1])
    new_rel = []
    for elem in rel:
        if elem not in new_rel:
            new_rel.append(elem)
    rel = new_rel
    return rel


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
    #Start with a random initial shape.
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
            #Continue with a random shape or the newly appended shape.
            w = random.choice(final)  # w = shape
        n = n - 1
    return final


# Checks for overlap between the final shape set and a new shape s.
def check_overlap(final, s):
    for f in final:
        if f.plane != s.plane: continue
        fmin = [f.list[0].x,f.list[0].y,f.list[0].z]
        fmax = [f.list[0].x, f.list[0].y,f.list[0].z]
        for b in f:
            if fmin[0] > b.x or fmin[1] > b.y or fmin[2] > b.z:
                fmin = [b.x,b.y,b.z]
            if fmax[0] < b.x or fmax[1] < b.y or fmax[2] < b.z:
                fmax = [b.x,b.y,b.z]
        smin = [s.list[0].x, s.list[0].y, s.list[0].z]
        smax = [s.list[0].x, s.list[0].y, s.list[0].z]
        for b in s:
            if smin[0] > b.x or smin[1] > b.y or smin[2] > b.z:
                smin = [b.x, b.y, b.z]
            if smax[0] < b.x or smax[1] < b.y or smax[2] < b.z:
                smax = [b.x, b.y, b.z]
        if smin[0] >= fmin[0] and smin[1] >= fmin[1] and smin[2] >= fmin[2] and smax[0] <= fmax[0] and smax[1] <= fmax[1] and smax[2] <= fmax[2]:
            return True
    return False


# Return a production of shapes with a size limitation.
def production_limit(shapes, rel, limit=[10, 10, 10], n=5):
    w = random.choice(shapes)
    min = [w.list[0].x, w.list[0].y, w.list[0].z]
    max = [w.list[0].x, w.list[0].y, w.list[0].z]
    final = [w]
    tries = 0
    nrtries = 0
    blocked = []
    while n > 0:
        w = random.choice(final)
        if (tries > 100):
            break
        if (nrtries > 100):
            break
        rrel = []
        for r in rel:
            for s in r[0]:
                if s.eq_production(w):
                    rrel.append(r)
        remove = []
        for rr in blocked:
            for r in rrel:
                if (r == rr):
                    remove.append(r)
        for r in remove:
            rrel.remove(r)
        if len(rrel) != 0:
            r = random.choice(rrel)
            og = r[2]
            shape = r[1].copy()
            edit_pos_relation(w, og, shape)

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
                blocked.append(r)
                w = random.choice(final)
                continue
            else:
                if final.__contains__(shape):
                    continue
                if check_overlap(final,shape):
                    continue
                tries = 0
                blocked = []
                final.append(shape)
                # Continue with a random shape or the newly appended shape.
                w = random.choice(final)  # w = shape
        else:
            w = random.choice(final)
            nrtries = nrtries + 1
            continue
        n = n - 1
    # If contact with none or only one other shape: remove the shape.
    done = False
    while not done:
        remove = []
        for s1 in final:
            i = 0
            for s2 in final:
                if contact(s1,s2): i = i+1
                if i > 1: break
            if i <= 1: remove.append(s1)
        if len(remove) == 0:
            done = True
        print("PRUNE")
        print(remove)
        final = [s for s in final if not remove.__contains__(s)]
    return final


def one_plane_contact(shape,shapes):
    contact_blocks = []
    contact_shape = 0
    for s in shapes:
        for b1 in shape:
            for b2 in s:
                if distance(b1, b2) == 1:
                    contact_blocks.append(b2)
                    #if()
        return False


# Edit the position of a new shape according to the position of the shape that produced it.
def edit_pos_relation(w, og, shape):
    p = [0, 0, 0]
    if w.plane == og.plane:
        p[0] = og.f[0] - w.f[0]
        p[1] = og.f[1] - w.f[1]
        p[2] = og.f[2] - w.f[2]
        shape.edit_pos(p)
    else:
        if og.plane == 'xy':
            shape = to_xy(shape)
        if og.plane == 'xz':
            shape = to_xz(shape)
        if og.plane == 'zy':
            shape = to_zy(shape)
    return shape


# Check if the shape is the same except for location and orientation
def is_duplicate_shape(s1, s2):
    if (len(s1) != len(s2)):
        return False
    if (s1.plane == s2.plane):
        m = len(s1)
        # FLIP S2 ON FOUR SIDES TO CHECK IF EQUAL
        for b1 in s1:
            for b2 in s2:
                if (b1.id == b2.id and b1.dmg == b2.dmg and b1.rx == b2.rx and b1.ry == b2.ry and b1.rz == b2.rz):
                    m = m - 1
                    break
        if (m == 0):
            return True
    else:
        m = len(s1)
        # FLIP S2 ON FOUR SIDES TO CHECK IF EQUAL
        for b1 in s1:
            for b2 in s2:
                if (b1.id == b2.id and b1.dmg == b2.dmg):
                    if ((s1.plane == 'zy' and s2.plane == 'xy') or (s1.plane == 'xy' and s2.plane == 'zy')):
                        if (b1.rx == b2.rz and b1.ry == b2.ry and b1.rz == b2.rx):
                            m = m - 1
                            break
                    if ((s1.plane == 'xy' and s2.plane == 'xz') or (s1.plane == 'xz' and s2.plane == 'xy')):
                        if (b1.rx == b2.rx and b1.ry == b2.rz and b1.rz == b2.ry):
                            m = m - 1
                            break
                    if ((s1.plane == 'xz' and s2.plane == 'zy') or (s1.plane == 'zy' and s2.plane == 'xz')):
                        if (b1.rx == b2.ry and b1.ry == b2.rx and b1.rz == b2.rz):
                            m = m - 1
                            break
        if (m == 0):
            return True
    return False


# def flip(shape):

# EDIT RELATIVE HERE?
def to_xz(s):
    if (s.plane == 'xz'): return s.copy()
    if (s.plane == 'xy'):
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.z
            b.z = temp
        sd.plane = 'xz'
        sd.set_relative([sd.list[0].x, sd.list[0].y, sd.list[0].z])
        return sd
    if (s.plane == 'zy'):
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.x
            b.x = temp
        sd.plane = 'xz'
        sd.set_relative([sd.list[0].x, sd.list[0].y, sd.list[0].z])
        return s


def to_xy(s):
    if (s.plane == 'xy'): return s.copy()
    if (s.plane == 'xz'):
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.z
            b.z = temp
        sd.plane = 'xy'
        sd.set_relative([sd.list[0].x, sd.list[0].y, sd.list[0].z])
        return sd
    if (s.plane == 'zy'):
        sd = s.copy()
        for b in sd:
            temp = b.z
            b.z = -b.x
            b.x = -temp
        sd.plane = 'xy'
        sd.set_relative([sd.list[0].x, sd.list[0].y, sd.list[0].z])
        return sd


def to_zy(s):
    if (s.plane == 'zy'): return s.copy()
    if (s.plane == 'xz'):
        sd = s.copy()
        for b in sd:
            temp = b.y
            b.y = b.x
            b.x = temp
        sd.plane = 'zy'
        sd.set_relative([sd.list[0].x, sd.list[0].y, sd.list[0].z])
        return sd
    if (s.plane == 'xy'):
        sd = s.copy()
        for b in sd:
            temp = b.z
            b.z = -b.x
            b.x = temp
        sd.plane = 'zy'
        sd.set_relative([sd.list[0].x, sd.list[0].y, sd.list[0].z])
        return sd


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


def all_xy_to_zy(shapes, rules):
    new_shapes = []
    for s in shapes:
        # if (s.plane == 'xy'):
        #    ns = s.copy()
        #    ns = to_zy(ns)
        #    ns.edit_pos([ns.f[0],ns.f[1],ns.f[2]])
        #    new_shapes.append(ns)
        if (s.plane == 'zy'):
            ns = s.copy()
            new_shapes.append(to_xy(ns))
        else:
            continue
    shapes.extend(new_shapes)
    new_rules = []
    for r in rules:
        for s in new_shapes:
            if (r[1].eq_production(s)):
                new_rules.append([r[0], s, r[2]])
            for p in r[0]:
                if (p.eq_production(s)):
                    r[0].append(s)
                    break
    rules.extend(new_rules)
    return [new_shapes, rules]
    return [shapes, rules]


def main2():
    shapes3m3m3 = []
    main_shape_append(shapes3m3m3, Block(3, 0, 0, 0, 0))
    main_shape_append(shapes3m3m3, Block(3, 0, 0, 1, 0))
    main_shape_append(shapes3m3m3, Block(3, 0, 0, 2, 0))
    main_shape_append(shapes3m3m3, Block(4, 0, 0, 3, 0))
    main_shape_append(shapes3m3m3, Block(4, 0, 0, 4, 0))
    main_shape_append(shapes3m3m3, Block(3, 0, 1, 0, 0))
    main_shape_append(shapes3m3m3, Block(1, 0, 1, 1, 0))
    main_shape_append(shapes3m3m3, Block(3, 0, 1, 2, 0))
    main_shape_append(shapes3m3m3, Block(4, 0, 1, 3, 0))
    main_shape_append(shapes3m3m3, Block(4, 0, 1, 4, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 2, 0, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 2, 1, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 2, 2, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 2, 3, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 2, 4, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 3, 0, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 3, 1, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 3, 2, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 3, 3, 0))
    main_shape_append(shapes3m3m3, Block(20, 0, 3, 4, 0))
    shapesb = []
    main_shape_append(shapesb, Block(20, 0, 0, 0, 0))
    main_shape_append(shapesb, Block(20, 0, 0, 1, 0))
    main_shape_append(shapesb, Block(20, 0, 0, 2, 0))
    main_shape_append(shapesb, Block(20, 0, 0, 3, 0))
    main_shape_append(shapesb, Block(4, 0, 1, 0, 0))
    main_shape_append(shapesb, Block(4, 0, 1, 1, 0))
    main_shape_append(shapesb, Block(4, 0, 1, 2, 0))
    main_shape_append(shapesb, Block(4, 0, 1, 3, 0))

    a = Shape(Block(98, 0, 0, 0, 0), 'xy')
    a.append(Block(98, 0, 1, 0, 0))
    a.append(Block(98, 0, 0, 1, 0))
    a.append(Block(98, 0, 1, 1, 0))
    b = Shape(Block(5, 0, 2, 0, 0), 'xy')
    b.append(Block(5, 0, 3, 0, 0))
    c = Shape(Block(98, 0, 0, 1, 0), 'zy')
    c.append(Block(98, 0, 1, 1, 0))
    c.append(Block(20, 0, 0, 1, 1))
    c.append(Block(20, 0, 1, 1, 1))
    c.append(Block(98, 0, 0, 1, 2))
    c.append(Block(98, 0, 1, 1, 2))
    d = Shape(Block(98, 0, 0, 0, 2), 'xy')
    d.append(Block(98, 0, 1, 0, 2))
    d.append(Block(98, 0, 0, 1, 2))
    d.append(Block(98, 0, 1, 1, 2))
    shapes = [a, b, c, d]
    print(shapes)
    rel = relation_learning(copy_shapes(shapes))
    print("FINAL RELATIONS")
    for r in rel:
        print(r)
    final = production(shapes, rel)
    print("FINAL PRODUCTION")
    for s in final:
        print(s)
    return


def main():
    split_grammar([], [])


def main_shape_append(shapes, b):
    shapes.append(Shape(b, 'xz'))
    shapes.append(Shape(b, 'xy'))
    shapes.append(Shape(b, 'zy'))


class Beam():
    def __init__(self, x, y, z, xx, yy, zz):
        self.x = x
        self.y = y
        self.z = z
        self.xx = xx
        self.yy = yy
        self.zz = zz

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "pos (" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")" + " rpos (" + str(
            self.xx) + "," + str(self.yy) + "," + str(self.zz) + ")"

    def split_x(self, r):
        b1 = Beam(self.x, self.y, self.z, r, self.yy, self.zz)
        b2 = Beam(self.x + r - 1, self.y, self.z, self.xx - r, self.yy, self.zz)
        return [b1, b2]

    def split_x_of(self, r):
        nb = abs(self.xx / r)
        list = []
        for i in range(0, nb):
            list.append(Beam(self.x + i * (r - 1), self.y, self.z, r, self.yy, self.zz))
        return list

    def split_y(self, r):
        b1 = Beam(self.x, self.y, self.z, self.xx, r, self.zz)
        b2 = Beam(self.x, self.y + r, self.z, self.xx, self.yy - r, self.zz)
        return [b1, b2]

    def split_floors_of(self, r):
        nb = abs(self.yy / r)
        list = []
        for i in range(0, nb):
            list.append(Beam(self.x, self.y + i * r, self.z, self.xx, r, self.zz))
        return list

    def split_z(self, r):
        b1 = Beam(self.x, self.y, self.z, self.xx, self.yy, r)
        b2 = Beam(self.x, self.y, self.z + r - 1, self.xx, self.yy, self.zz - r)
        return [b1, b2]

    def split_z_of(self, r):
        nb = abs(self.zz / r)
        list = []
        for i in range(0, nb):
            p = 0
            if (i != 0): p = -1
            list.append(Beam(self.x, self.y, self.z + i * (r - 1), self.xx, self.yy, r))
        return list

    def fill_beam1(self, shapes, rules):
        # t = all_xy_to_zy(shapes,rules)
        # shapes = t[0]
        # rules = t[1]
        # 6 beam faces: try to fill all
        # start with 1, then look for rules to fill the rest
        # if no rule available, leave the beam face open
        final = []
        # first xy
        c = []
        for s in shapes:
            if s.plane == 'xy':
                s = s.copy()
                s.edit_pos([s.f[0], s.f[1], s.f[2]])
                s.edit_pos([self.x, self.y, self.z + (self.zz - 1)])
                c.append(s)
        final.append(random.choice(c))
        # first zy
        p = self.find_plane_shape(final[0], rules, 'zy')
        final.append(p)
        p = self.find_plane_shape(final[1], rules, 'xy')
        final.append(p)
        p = self.find_plane_shape(final[2], rules, 'xz', +(self.yy + 1))
        final.append(p)
        p = self.find_plane_shape(final[3], rules, 'zy', -(self.xx - 1))
        final.append(p)
        print("FILL")
        print(final)
        return final

    def fill_beam(self, shapes, rules):
        final = []
        # first xy
        c = []
        for s in shapes:
            if s.plane == 'xy':
                s = s.copy()
                s.edit_pos([s.f[0], s.f[1], s.f[2]])
                s.edit_pos([self.x, self.y, self.z + (self.zz - 1)])
                c.append(s)
        final.append(random.choice(c))

        if final[0].width() < self.xx:
            p = self.find_plane_shape(final[0], rules, 'xy',+ (self.zz - 1),final[0].width())
            final.append(p)


        # first zy
        p = self.find_plane_shape(final[0], rules, 'zy')
        final.append(p)

        if p.depth() < self.zz:
            p = self.find_plane_shape(p, rules, 'zy',0,p.depth())
            final.append(p)

        p = self.find_plane_shape(p, rules, 'xy')
        final.append(p)
        p = self.find_plane_shape(p, rules, 'xz', +(self.yy + 1))
        final.append(p)

        if p.depth() < self.zz:
            print("depth")
            p = self.find_plane_shape(p, rules, 'xz',+(self.yy + 1),p.depth())
            final.append(p)

        if p.width() < self.xx:
            p = self.find_plane_shape(p, rules, 'xz',+(self.yy + 1),0,-p.width())
            final.append(p)

        p = self.find_plane_shape(p, rules, 'zy', -(self.xx-1))
        final.append(p)

        if p.depth() < self.zz:
            p = self.find_plane_shape(p, rules, 'zy',-(self.xx-1),p.depth())
            final.append(p)

        print("FILL")
        print(final)
        return final

    def find_plane_shape(self, prev, rules, plane, j=0, zz=0, xx=0):
        rrel = []
        for r in rules:
            for s in r[0]:
                if (prev.eq_production(s) and r[1].plane == plane):
                    rrel.append(r)
        if (len(rrel) == 0):
            return prev
        r = random.choice(rrel)
        p = r[1].copy()
        p.edit_pos([p.f[0], p.f[1], p.f[2]])
        if plane == 'xy':
            p.edit_pos([self.x + xx, self.y, (self.z + j)])
        if plane == 'xz':
            p.edit_pos([self.x + xx, self.y + j, self.z + zz])
        if plane == 'zy':
            p.edit_pos([self.x + j, self.y, self.z + zz])
        return p


def split_grammar(shapes, rules):
    print("SPLIT")
    b = Beam(0, 0, 0, 9, -4, 9)  # b = Beam(-10,0,0,6,3,3)#
    # print(b)
    # b = b.split_y(-4)
    # bb = []
    # bb.extend(b[0].split_x(5))#b = b.split_x(3)#
    # bb.extend(b[1].split_x(5))
    # print(bb)
    # bbb = []
    # for b in bb:
    #    bbb.extend(b.split_z(5))
    final = []
    # i=0
    bb = []
    # bb.append(Beam(0,0,0,5,-4,5))
    bb.append(b)
    for beam in bb:
        # if(i>2): break
        print("BEAM")
        print(beam)
        final.extend(beam.fill_beam(shapes, rules))
        print(final)
        # i = i+1

    #final = []
    #list = automatic_split()
    #i = 0
    #e = random.randrange(1, len(list))
    #for beam in list:
    #    if (i > e): break
    #    if (random.randrange(0, 10) == 0): continue
    #    final.extend(beam.fill_beam(shapes, rules))
    #    i = i + 1
    return final


def automatic_split(w=5, h=-4, d=5):
    b = Beam(0, 0, 0, random.randrange(1, 5) * w, random.randrange(1, 5) * h, random.randrange(1, 5) * d)  #
    list = []
    # split floors
    if (b.yy < h):
        list = b.split_floors_of(h)
    else:
        list.append(b)
    copy = list
    list = []
    for beam in copy:
        if (beam.xx > w):
            list.extend(beam.split_x_of(w))
        else:
            list.append(beam)
    copy2 = list
    list = []
    for beam in copy2:
        if (beam.zz > d):
            list.extend(beam.split_z_of(d))
        else:
            list.append(beam)
    return list


if __name__ == "__main__":
    main()
