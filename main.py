import math

from sympy import integrate

import sympy as sym

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getPoints(equ, a, b, n):

    h = (b - a) / n

    points = []

    x = a
    while x <= b:
        y = eval(equ)
        points.append(Point(x, y))
        x += h
    return points, h

def getPoint(equ, x) -> float:
    return eval(equ)





#using points
def trapezoidal(points, h) -> float:

    a = points[0]
    b = points[-1]

    # Value of integration
    I = 0.0

    for i in range(1,len(points) - 1):
        I += points[i].y
    print(I)

    I = (h / 2) * (a.y + b.y + 2 * I)

    return I

def simpsonComposite(points, n:int) -> float:

    I = 0.0
    a = points[0]
    b = points[-1]

    h = (b.x - a.x) / n
    l = n / 2
    for i in range(1, int(n/2) + 1):
        I += points[2*i -1].y
    I = 4 * I

    for i in range(1, int(n / 2) - 1 + 1):
        I += 2 * points[2 * i].y
    I += a.y + b.y
    I = I * (h/3)

    return I

def simpson(points) -> float:

    a = points[0]
    b = points[-1]

    # I = interpolate(points, (a.x + b.x) / 2, len(points))
    I = getPoint("x**2", (0 + 2) / 2)
    I *= 4
    I += a.y + b.y
    I *= (b.x - a.x)
    I /= 6

    return I

def interpolate(f: list, xi: int, n: int) -> float:
    # Initialize result
    result = 0.0
    for i in range(n):

        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)

        # Add current term to result
        result += term

    return result

if __name__ == '__main__':
    # points = (Point(0, 0), Point(1, 10), Point(2, 12), Point(3, 14))

    # print(simpson(points))
    # equ1 = "0.2+25*x-200*(x**2)+675*(x**3)-900*(x**4)+400*(x**5)"
    # p, h = getPoints(equ1, 0, 0.8, 10)
    # print(trapezoidal(p, h))

    #mid = 2
    #trap=4
    #simpson = 2.667
    # equ2 = "x**2"
    # p2, h2 = getPoints(equ2, 0, 2, 1)
    # print(f"simpson: {simpson(p2)}")
    # print(f"trapezoid: {trapezoidal(p2, h2)}")

    equ3 = "x**2"
    p3, h3 = getPoints(equ3, 2, 6, 4)
    print(f"simpson: {simpsonComposite(p3,4)}")
    print(f"trapezoid: {trapezoidal(p3, h3)}")

    # x = sym.symbols('x')
    # print(sym.integrate(sym.cos(x), x))