import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 8

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(normal)
    color = arrayAdd(calculate_ambient(ambient,areflect),
           arrayAdd(calculate_diffuse(light,dreflect,normal),
           calculate_specular(light,sreflect,view,normal)))
    color = [limit_color(int(color[0])),limit_color(int(color[1])),limit_color(int(color[2]))]
    return color
def calculate_ambient(alight, areflect):
    color = arrayMulti(alight,areflect)
    color = [limit_color(color[0]),limit_color(color[1]),limit_color(color[2])]
    return color

def calculate_diffuse(light, dreflect, normal):
    finalDiff = dot_product(normal,light[LOCATION])
    if finalDiff < 0:
        finalDiff = 0
    finalDiff = scaleArray(arrayMulti(light[COLOR],dreflect),finalDiff)
    finalDiff = [limit_color(finalDiff[0]),limit_color(finalDiff[1]),limit_color(finalDiff[2])]
    return finalDiff

def calculate_specular(light, sreflect, view, normal):
    finalSpec = 2 * dot_product(normal,light[LOCATION])
    if finalSpec < 0:
        finalSpec = 0
    finalSpec = scaleArray(normal,finalSpec)
    finalSpec = arraySubtract(finalSpec,light[LOCATION])
    finalSpec = dot_product(finalSpec,view)
    if finalSpec < 0:
        finalSpec = 0
    finalSpec = finalSpec ** SPECULAR_EXP
    finalSpec = scaleArray(arrayMulti(light[COLOR],sreflect),finalSpec)
    finalSpec = [limit_color(finalSpec[0]),limit_color(finalSpec[1]),limit_color(finalSpec[2])]
    return finalSpec

def limit_color(color):
    if color >255:
        return 255
    elif color<0:
        return 0
    return color

def arrayMulti(array1, array2):
    product = []
    for i in range(len(array1)):
        product.append(array1[i]*array2[i])
    return product
def scaleArray(array1,scale):
    array2 = []
    for i in range(len(array1)):
        array2.append(scale * array1[i])
    return array2
def arraySubtract(array1,array2):
    difference = []
    for i in range(len(array1)):
        difference.append(array1[i]-array2[i])
    return difference
def arrayAdd(array1,array2):
    sum = []
    for i in range(len(array1)):
        sum.append(array1[i]+array2[i])
    return sum
#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
