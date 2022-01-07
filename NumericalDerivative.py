from General import Numerical


class NumericalDerivative(Numerical):
    def __init__(self, equOrPoints, x, h=None):
        super().__init__()

        self.h = h
        self.x = x

        # check whether the input is equation or table of points
        # str -> equation
        # list -> points
        if isinstance(equOrPoints, str):
            self.equation = equOrPoints
            if h is None:
                self.error("h not given")

            try:
                self.getPoint(1)
            except:
                self.error("Wrong equation format")
        else:
            self.points = equOrPoints
            self.n = len(self.points) - 1
            self.h = self.__findH()

    # Check first if the point is found in points or not
    # if not then use getPoint to evaluate (x)
    def __evaluatePoint(self, x) -> float:
        if len(self.points) > 0:
            for point in self.points:
                if x == point.x:
                    return point.y
            return self.interpolate(x)
        else:
            return self.getPoint(x)

    def __findH(self) -> float:
        # Initial values
        h = self.points[-1].x - self.points[0].x

        # Find h by getting the lowest step between two points
        for i in range(1, len(self.points)):
            j = self.points[i].x - self.points[i - 1].x
            if j < h:
                h = j
        if h > self.x:
            return h - self.x
        else:
            return self.x - h

    def twoForward(self) -> float:
        D = 0.0

        D = self.__evaluatePoint(self.x + self.h)
        D -= self.__evaluatePoint(self.x)
        D /= self.h

        return D

    def twoBackward(self) -> float:
        D = 0.0

        D = self.__evaluatePoint(self.x)
        D -= self.__evaluatePoint(self.x - self.h)
        D /= self.h

        return D

    def threeForward(self) -> float:
        D = 0.0

        D -= (3 * self.__evaluatePoint(self.x))
        D += (4 * self.__evaluatePoint(self.x + self.h))
        D -= self.__evaluatePoint(self.x + (2 * self.h))
        D /= (2 * self.h)

        return D

    def threeBackward(self) -> float:
        D = 0.0

        D += (3 * self.__evaluatePoint(self.x))
        D -= (4 * self.__evaluatePoint(self.x - self.h))
        D += self.__evaluatePoint(self.x - (2 * self.h))
        D /= (2 * self.h)

        return D

    def central(self) -> float:
        D = 0.0

        D = self.__evaluatePoint(self.x + self.h)
        D -= self.__evaluatePoint(self.x - self.h)
        D /= (2 * self.h)

        return D

    def solveTwo(self, index):
        if index < 2:
            return self.twoForward()
        else:
            return self.twoBackward()

    def solveThree(self, index):
        if index < 3:
            return self.threeForward()
        else:
            return self.threeBackward()

    def all(self):

        if len(self.points) > 0:
            index = 1
            for point in self.points:
                self.x = point.x
                print(f"f'({point.x}) = {self.solveTwo(index)}")
                index += 1
            index = 1
            for point in self.points:
                self.x = point.x
                print(f"f'({point.x}) = {self.solveThree(index)}")
                index += 1
        else:
            print(f"2PF: {self.twoForward()}")
            print(f"2PB: {self.twoBackward()}")
            print(f"3PF: {self.threeForward()}")
            print(f"3PB: {self.threeBackward()}")
            print(f"central: {self.central()}")
