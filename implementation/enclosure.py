# Based on A* implementation by Nicholas Swift.
class Node():

    def __init__(self, position=None):
        self.position = position

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
        end_node = Node(e[0])
        end_node.f = 0
        start_node = Node(e[1])
        start_node.f = 0
        end_nodes.append([end_node,start_node])
    print(ends)
    print(end_nodes)
    start_node = Node([0, 0, 0])
    start_node.f = 0

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
        for new_position in [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]:

            # Get node position
            node_position = [current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2]]

            # Make sure within range
            if node_position[0] > (len(shapes_space) - 1) or node_position[0] < 0 or\
               node_position[1] > (len(shapes_space[0]) -1) or node_position[1] < 0 or\
               node_position[2] > len(shapes_space[0][0]) -1 or node_position[2] < 0:
                continue

            # Make sure walkable terrain
            if shapes_space[node_position[0]][node_position[1]][node_position[2]] != 0:
                continue

            # Create new node
            new_node = Node(node_position)

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
            child.f = current_node.f + 1

            # Child is already in the open list
            c = False
            for open_node in open_list:
                if child == open_node:
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
        end_node = Node(e[0])
        end_node.f = 0
        start_node = Node(e[1])
        start_node.f = 0
        end_nodes.append([end_node,start_node])
    print(ends)
    print(end_nodes)
    start_node = Node([0, 0])
    start_node.f = 0

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
            if node_position[0] > (len(shapes_space) - 1) or node_position[0] < 0 or node_position[1] > (len(shapes_space[0]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if shapes_space[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(node_position)

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
            child.f = current_node.f + 1

            # Child is already in the open list
            c = False
            for open_node in open_list:
                if child == open_node:
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
    space = [[[0 for e in range(maxz-minz+3)] for col in range(maxy-miny+3)] for row in range(maxx-minx+3)]
    for s in shapes:
        for b in s:
            space[b.x - minx+1][b.y - miny][b.z - minz+1] = b.id
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
            if b.x < minx: minx = b.x
            if b.x > maxx: maxx = b.x
            if b.z < minz: minz = b.z
            if b.z > maxz: maxz = b.z
    space = [[0 for col in range(maxz-minz+3)] for row in range(maxx-minx+3)]
    for s in shapes:
        for b in s:
            if b.y > 1: continue
            space[b.x - minx+1][b.z - minz+1] = b.id
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
def enclosure_find_3d(shapes):
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
    return remove

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
