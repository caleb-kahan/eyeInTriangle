from display import *
from matrix import *
from draw import *

ARG_COMMANDS = [ 'box', 'sphere', 'torus', 'circle', 'bezier', 'hermite', 'line', 'scale', 'move', 'rotate', 'save' ]


def parse_file2( fname, edges, polygons, csystems, screen, zbuffer, color,view, ambient, light, areflect, dreflect, sreflect):
    f = open(fname)
    lines = f.readlines()

    clear_screen(screen)
    clear_zbuffer(zbuffer)

    vertices = []

    c = 0
    while c < len(lines):
        line = lines[c].strip()
        #print ':' + line + ':'
        if c < 3658:
            stringArr = lines[c].strip().split(' ')
            for i in range(3):
                stringArr[i] = float(stringArr[i])
            vertices.append(stringArr)
        elif c >= 3658:
            chosenVertices = lines[c].strip().split(' ')
            for i in range(3):
                chosenVertices[i] = float(chosenVertices[i])
            add_polygon(polygons,vertices[chosenVertices[0]][0],vertices[chosenVertices[0]][1],vertices[chosenVertices[0]][2]),
                                 vertices[chosenVertices[1]][0],vertices[chosenVertices[1]][1],vertices[chosenVertices[1]][2]),
                                 vertices[chosenVertices[2]][0],vertices[chosenVertices[2]][1],vertices[chosenVertices[1]][2]))

    matrix_mult(csystems[-1], polygons)
    draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)

        elif line == 'push':
            csystems.append( [x[:] for x in csystems[-1]] )

        elif line == 'pop':
            csystems.pop()


        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(csystems[-1], t)
            csystems[-1] = [x[:] for x in t]


        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(csystems[-1], t)
            csystems[-1] = [x[:] for x in t]

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)

            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult(csystems[-1], t)
            csystems[-1] = [x[:] for x in t]

        elif line == 'ident':
            ident(transform)

        elif line == 'apply':
            matrix_mult( transform, edges )
            matrix_mult( transform, polygons )

        elif line == 'clear':
            clear_screen(screen)
            clear_zbuffer(zbuffer)

        elif line == 'display' or line == 'save':
            #clear_screen(screen)
            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])
        c+= 1
