from display import *
from matrix import *
from draw import *

def parse_file2( fname, edges, polygons, csystems, screen, zbuffer, color,view, ambient, light, areflect, dreflect, sreflect):
    f = open(fname)
    lines = f.readlines()

    clear_screen(screen)
    clear_zbuffer(zbuffer)

    #move
    t = make_translate(250, 250, 0)
    matrix_mult(csystems[-1], t)
    csystems[-1] = [x[:] for x in t]

    #rotate
    '''
    theta = float(45) * (math.pi / 180)
    t = make_rotX(theta)
    matrix_mult(csystems[-1], t)
    csystems[-1] = [x[:] for x in t]
    t = make_rotY(theta)
    matrix_mult(csystems[-1], t)
    csystems[-1] = [x[:] for x in t]
    '''

    vertices = []

    c = 0
    while c < len(lines):
        line = lines[c].strip()
        #print ':' + line + ':'
        if c < 14581:
            stringArr = lines[c].strip().split(' ')
            for i in range(3):
                stringArr[i] = float(stringArr[i])
            vertices.append(stringArr)
        elif c >= 14582:
            chosenVertices = lines[c].strip().split(' ')
            for i in range(4):
                chosenVertices[i] = int(chosenVertices[i])

            add_polygon(polygons,vertices[chosenVertices[1]][0],vertices[chosenVertices[1]][1],vertices[chosenVertices[1]][2],
            vertices[chosenVertices[2]][0],vertices[chosenVertices[2]][1],vertices[chosenVertices[2]][2],
            vertices[chosenVertices[3]][0],vertices[chosenVertices[3]][1],vertices[chosenVertices[3]][2])
        c+=1
    matrix_mult(csystems[-1], polygons)
    draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)


    csystems.append( [x[:] for x in csystems[-1]] )
    '''csystems.pop()
    #scale
    t = make_scale(float(args[0]), float(args[1]), float(args[2]))
    matrix_mult(csystems[-1], t)
    csystems[-1] = [x[:] for x in t]

    #rotate
    theta = float(args[1]) * (math.pi / 180)

    if args[0] == 'x':
        t = make_rotX(theta)
    elif args[0] == 'y':
        t = make_rotY(theta)
    else:
        t = make_rotZ(theta)
    matrix_mult(csystems[-1], t)
    csystems[-1] = [x[:] for x in t]
    '''
    display(screen)
    save_extension(screen, args[0])
