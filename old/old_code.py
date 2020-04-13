# Returns the best possible split for a set of shapes
def best_split_old(shapes):
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


# Splits a shape into two shapes - find the best split according to the minimal cost of the shapes
def split_shape_old(s):
    # r = find_rect(s)
    subshapes = sub_shapes(s)
    print(subshapes)
    possible_splits = []
    for sub in subshapes:
        # print("SUB")
        # print(sub)
        if is_rect(sub[0], sub[0].plane) and is_rect(sub[1], sub[1].plane):
            possible_splits.append(sub)
    print("POSSIBLE")
    print(possible_splits)
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
def sub_shapes(s):
    subshapes = []
    sub = []
    size = len(s)
    comb = combinations(s, size / 2)
    # print("Comb")
    for c in comb:
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

# Check if the shape is the same except for location and orientation
def is_duplicate_shape_old(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1.plane == s2.plane:
        m = len(s1)
        # FLIP S2 ON FOUR SIDES TO CHECK IF EQUAL
        for b1 in s1:
            for b2 in s2:
                if b1.id == b2.id and b1.dmg == b2.dmg and b1.rx == b2.rx and b1.ry == b2.ry and b1.rz == b2.rz:
                    m = m - 1
                    break
        if m == 0:
            return True
    else:
        m = len(s1)
        # FLIP S2 ON FOUR SIDES TO CHECK IF EQUAL
        for b1 in s1:
            for b2 in s2:
                if b1.id == b2.id and b1.dmg == b2.dmg:
                    if (s1.plane == 'zy' and s2.plane == 'xy') or (s1.plane == 'xy' and s2.plane == 'zy'):
                        if b1.rx == b2.rz and b1.ry == b2.ry and b1.rz == b2.rx:
                            m = m - 1
                            break
                    if (s1.plane == 'xy' and s2.plane == 'xz') or (s1.plane == 'xz' and s2.plane == 'xy'):
                        if b1.rx == b2.rx and b1.ry == b2.rz and b1.rz == b2.ry:
                            m = m - 1
                            break
                    if (s1.plane == 'xz' and s2.plane == 'zy') or (s1.plane == 'zy' and s2.plane == 'xz'):
                        if b1.rx == b2.ry and b1.ry == b2.rx and b1.rz == b2.rz:
                            m = m - 1
                            break
        if m == 0:
            return True
    return False

# Converts all
def all_xy_to_zy(shapes, rules):
    new_shapes = []
    for s in shapes:
        if s.plane == 'xy':
            ns = s.copy()
            ns = to_zy(ns)
            ns.edit_pos([ns.f[0], ns.f[1], ns.f[2]])
            new_shapes.append(ns)
        if s.plane == 'zy':
            ns = s.copy()
            new_shapes.append(to_xy(ns))
        else:
            continue
    shapes.extend(new_shapes)
    new_rules = []
    for r in rules:
        for s in new_shapes:
            if r[1].eq_production(s):
                new_rules.append([r[0], s, r[2]])
            for p in r[0]:
                if p.eq_production(s):
                    r[0].append(s)
                    break
    rules.extend(new_rules)
    return [new_shapes, rules]