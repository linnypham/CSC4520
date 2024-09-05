from math import sqrt, pi
def quadratic(a,b,c):
    result = []
    square = sqrt(b**2-4*a*c)
    x1 = (-b+square)/2*a
    x2 = (-b-square)/2*a
    return x1,x2

def circumferenceCircle(radius):
    result = 2 * pi * radius
    return result

def areaCircle(radius):
    result = pi * radius**2
    return result