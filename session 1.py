import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p = Point(1, 2)
p2 = Point(2, 3)
p4 = Point(4.4, -55)

print(f'p.x={p.x} and p.y={p.y}')
print(f'p4.x={p4.x} and p4.y={p4.y}')
p.x = 20

print(f'p.x={p.x} and p.y={p.y}')
print(p)


points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10), random.randint(-10, 10)))

print("I got these 5 random points:")
for p in points:
    print(p)
