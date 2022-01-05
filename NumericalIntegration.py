from General import Point, Numerical

class NumericalIntegration(Numerical):
    def __init__(self, a, b, equOrPoints, n=1):
        super().__init__(n)

        self.h = ((b - a) / n)
        # self.equation = ""
        # self.points = []
        self.a = a
        self.b = b
        self.n = n

        # check whether the input is equation or table of points
        # str -> equation
        # list -> points
        if isinstance(equOrPoints, str):
            self.equation = equOrPoints
            try:
                self.__getPoints()
            except:
                self.error("Wrong equation format")
        else:
            self.points = equOrPoints
            self.h, self.n = self.__checkTablePoints()

    # Method for getting needed points from equation
    def __getPoints(self):
        x = self.a
        # Loop from a to b steps by h
        while x <= self.b:
            y = eval(self.equation)
            self.points.append(Point(x, y))
            x += self.h

    # Table points steps with h
    # Method assures that all points if not it fills the gaps
    # It returns h & n
    def __checkTablePoints(self) -> (float, int):

        # Initial values
        h = self.points[-1].x - self.points[0].x
        n = int(len(self.points) - 1)

        # Find h by getting the lowest step between two points
        for i in range(1, len(self.points)):
            j = self.points[i].x - self.points[i - 1].x
            if j < h:
                h = j
        # If h = (b - a) / n then return
        if h == (self.points[-1].x - self.points[0].x) / n:
            return h, n
        # Else mean 1 point or more is missed in table
        # Get the missed point
        else:
            n = int((self.points[-1].x - self.points[0].x) / h)
            self.n = n
            for i in range(1, len(self.points)):
                j = self.points[i].x - self.points[i - 1].x
                if j > h:
                    x = self.points[i].x - h
                    self.points.insert(i, Point(
                        x,
                        self.interpolate(x)
                    ))
        return h, n

    def midPoint(self) -> float:
        I = 0.0

        if self.n == 1:
            # I = interpolate(points, (a.x + b.x) / 2, len(points))
            I = self.getPoint((self.a + self.b) / 2)
            I *= self.h
        else:
            for j in range(0, int(self.n / 2)):
                I += self.points[(j * 2)+1].y

            I += self.points[0].y + self.points[-1].y
            I *= (2 * self.h)

        return I


    def trapezoidal(self) -> float:

        # Value of integration
        I = 0.0
        for j in range(1, self.n):
            I += self.points[j].y
        I = (self.h / 2) * (self.points[0].y + self.points[-1].y + 2 * I)

        return I

    def simpson(self) -> float:

        I = 0.0

        if self.n == 1:
            # I = interpolate(points, (a.x + b.x) / 2, len(points))
            I = (4 * self.getPoint((self.a + self.b) / 2)) + self.points[0].y + self.points[-1].y
            I *= (self.h / 6)
        else:
            for j in range(1, int(self.n / 2)):
                I += 2 * self.points[j * 2].y

            for j in range(1, int(self.n / 2) + 1):
                I += 4 * self.points[(j * 2) - 1].y

            I += self.points[0].y + self.points[-1].y
            I *= (self.h / 3)

        return I

    # TODO
    def integration(self):
        return