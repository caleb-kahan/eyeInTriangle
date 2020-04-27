from display import *
from draw import *
from parser import *
from matrix import *
import math


# lighting values
view = [0,
        0,
        1];
normalize(view)

ambient = [50,
           50,
           50]
light = [[0.5,
          0.75,
          1],
         [0,
          255,
          255]]
normalize(light[0])
areflect = [.1,
            .1,
            .1]
dreflect = [.5,
            .5,
            .5]
sreflect = [.5,
            .5,
            .5]



screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
