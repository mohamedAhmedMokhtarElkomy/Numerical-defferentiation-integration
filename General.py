class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Class for general methods required by differentiation and integration
class Numerical:
    def __init__(self, n=1):
        self.equation = ""
        self.points = []
        self.n = n
    #
    #     # check whether the input is equation or table of points
    #     # str -> equation
    #     # list -> points
    #     if isinstance(equOrPoints, str):
    #         # Check equation is right expression
    #         try:
    #             self.__getPoint(1)
    #         except:
    #             self.__error("Wrong equation format")
    #     else:
    #         self.points = equOrPoints

    # used for evaluating single point ( x ) from equation
    def getPoint(self, x) -> float:
        return eval(self.equation)

    # Lagrange interpolation
    def interpolate(self, xi: int) -> float:
        # Initialize result
        result = 0.0
        for i in range(self.n):

            # Compute individual terms of above formula
            term = self.points[i].y
            for j in range(self.n):
                if j != i:
                    term = term * (xi - self.points[j].x) / (self.points[i].x - self.points[j].x)

            # Add current term to result
            result += term

        return result

    # for handling errors
    def error(self, message):
        print(f"Error found: {message}")
