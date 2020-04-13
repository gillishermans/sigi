from math import sqrt, tan, sin, cos, pi, ceil, floor, acos, atan, asin, degrees, radians, log, atan2, acos, asin
import math as math
from random import *
import numpy as np
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import utilityFunctions as utilityFunctions
import sys
from sem2_shape import Block, Shape
import sem2_shape as shp
import split_grammar as splt
import enclosure as encl
import in_out as io

inputs = (
    ("Read an example structure into disk.", "label"),
    ("Creator: Gillis Hermans", "label")
)


# Perform the filter: scan the structure, extract the shapes and shape relations and produce a new structure.
def perform(level, box, options):
    m = io.scan_structure(level, box)
    io.write_array(m)


