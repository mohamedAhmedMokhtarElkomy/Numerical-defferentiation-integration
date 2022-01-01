class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#using points
def trapizoidal(points, h) -> float:

    a = points[0]
    b = points[-1]

    # Value of integration
    I = 0.0

    for i in range(1,len(points) - 1):
        I += points[i].y
    print(I)

    I = (h / 2) * (a.y + b.y + 2 * I)

    return I


if __name__ == '__main__':
    points = (Point(0, 0), Point(1, 10), Point(2, 12), Point(3, 14))

    print(trapizoidal(points, 1.0))
