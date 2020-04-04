import random as random

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

def main():
    split_grammar([], [])

if __name__ == "__main__":
    main()