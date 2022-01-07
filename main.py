from NumericalIntegration import *
from NumericalDerivative import *
import math

if __name__ == '__main__':
    points = [Point(1, 2.1), Point(1.5, 3.2), Point(2, 3.4), Point(2.5, 2.8), Point(3, 2.7)]

    print("1-Points")
    print("2-Equation")
    print("3-exp")

    # integration example 1
    points1 = [Point(0, 0), Point(1, 10), Point(2, 12), Point(3, 14)]
    function = NumericalIntegration(0, 3, points1)
    function.all()
    print("============================================================")

    # integration example 2
    points2 = [Point(1, 2.1), Point(1.5, 3.2), Point(2, 3.4), Point(2.5, 2.8), Point(3, 2.7)]
    function = NumericalIntegration(1, 3, points2)
    function.all()
    print("============================================================")

    # integration example 3
    equ3 = "0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)"
    function = NumericalIntegration(0, 0.8, equ3, 2)
    function.all()
    print("============================================================")

    # integration example 4
    equ4 = "x**2"
    function = NumericalIntegration(0, 2, equ4)
    function.all()
    print("============================================================")

    # integration example 5
    equ5 = True
    function = NumericalIntegration(0, 2, equ5, 2)
    print(function.simpson())
    print("============================================================")

    # derivative example 1
    equ2 = "-0.1*(x**4) - 0.15*(x**3) - 0.5*(x**2) - 0.25*x + 1.2"
    function2 = NumericalDerivative(equ2, 0.5, 0.5)
    function2.all()
    print("============================================================")

    # derivative example 1
    equ2 = "-0.1*(x**4) - 0.15*(x**3) - 0.5*(x**2) - 0.25*x + 1.2"
    function2 = NumericalDerivative(equ2, 0.5, 0.25)
    function2.all()
    print("============================================================")

    # derivative example 3
    # points3 = [Point(0, 30.1), Point(5, 48.2), Point(10, 50), Point(15, 40.2)]
    # function = NumericalDerivative(points3)
    # function.all()
    # print("============================================================")

    # derivative example 4
    points3 = [Point(-1, -2), Point(3, 6), Point(5, 22), Point(7, 46)]
    function = NumericalDerivative(points3, 4)
    print(function.twoForward())
    print("============================================================")
    print(function.interpolate(7))

    # derivative example 5
    points4 = [Point(0, 0), Point(3, 225), Point(5, 383), Point(8, 623), Point(10, 742)]
    function = NumericalDerivative(points4, 0)
    print(function.all())
    print("============================================================")

    print(function.interpolate(10))
