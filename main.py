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


class NumericalIntegration:
    def __init__(self, a, b, equOrPoints, n=1):

        self.h = ((b - a) / n)
        self.equation = ""
        self.points = []
        self.a = a
        self.b = b
        self.n = n

        # if n > 1:
        #     self.h = ((b.x - a.x) / n)
        # else:
        #     self.h = (b.x - a.x)

        # check whether the input is equation or table of points
        if isinstance(equOrPoints, str):
            self.equation = equOrPoints
            try:
                self.__getPoints()
            except:
                self.__error("Wrong equation format")
        else:
            self.points = equOrPoints

    # convert equation to points
    def __getPoints(self):

        x = self.a
        while x <= self.b:
            y = eval(self.equation)
            self.points.append(Point(x, y))
            x += self.h

            # used for getting single point ( x ) from equation

    def __getPoint(self, x) -> float:
        return eval(self.equation)

    def __error(self, message):
        print(f"Error found: {message}")

    def trapezoidal(self) -> float:

        # Value of integration
        I = 0.0
        for j in range(1, self.n):
            I += self.points[j].y
        I = (self.h / 2) * (self.points[0].y + self.points[-1].y + 2 * I)

        return I

    def simpson(self) -> float:

        I = 0.0

        # j = 1
        # while True:
        #     I += self.points[(2 * j) - 2].y
        #     I += 4 * self.points[(2 * j) - 1].y
        #     I += self.points[2 * j].y
        #     I *= (self.h / 3)
        #     j+=1
        #     if j > (self.n / 2):
        #         break

        if self.n == 1:
            # I = interpolate(points, (a.x + b.x) / 2, len(points))
            I = (4 * self.__getPoint((self.a + self.b) / 2)) + self.points[0].y + self.points[-1].y
            I *= (self.h / 6)
        else:
            for j in range(1, int(self.n / 2)):
                I +=  2 * self.points[j * 2].y

            for j in range(1, int(self.n / 2) + 1):
                I += 4 * self.points[(j * 2) - 1].y

            I += self.points[0].y + self.points[-1].y
            I *= (self.h / 3)

        return I

    # TODO
    def integration(self):
        return


def midPoint(points) -> float:
    a = points[0]
    b = points[-1]

    I = getPoint("x**2", (a.x + b.x) / 2)
    I *= (b.x - a.x)

    return I


def midPointComposite(points, n: int) # print(simpson(points))
    # equ1 = "0.2+25*x-200*(x**2)+675*(x**3)-900*(x**4)+400*(x**5)"
    # p, h = getPoints(equ1, 0, 0.8, 10)
    # print(trapezoidal(p, h))

    # mid = 2
    # trap=4
    # simpson = 2.667
    # equ2 = "x**2"
    # p2, h2 = getPoints(equ2, 0, 2, 1)
    # print(f"midpoint: {midPoint(p2)}")
    # print(f"trapezoid: {trapezoidal(p2, h2)}")
    # print(f"simpson: {simpson(p2)}")

    # equ3 = "x**2"
    # p3, h3 = getPoints(equ3, 2, 6, 4)
    # print(f"midpoint: {midPointComposite(p3, 4)}")
    # print(f"simpson: {simpsonComposite(p3, 4)}")
    # print(f"trapezoid: {trapezoidal(p3, h3)}")

    # x = sym.symbols('x')
    # print(sym.integrate(sym.cos(x), x))-> float:
    I = 0.0
    a = points[0]
    b = points[-1]
    h = (b.x - a.x) / n

    for i in range(0, int(n / 2) + 1):
        I += points[(2 * i)].y

    I *= 2 * h

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

    a = 0
    b = 0.8
    # equ = "0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)"
    # function = NumericalIntegration(0, 0.8, equ, 10)
    equ = "x**2"
    function = NumericalIntegration(2, 6, equ, 4)
    print(f"trapezoidal: {function.trapezoidal()}")
    print(f"simpson: {function.simpson()}")
