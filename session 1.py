class Point:
    def __init__(self, x, y):

        """
        initialize a point object.
        :param x: the x position on the axis
        :param y: the y position on the axis
        """

        self.x = x
        self.y = y

p = Point(1,2)
p2 = Point(2,3)
p4 = Point(4.4,-55)

print(f'p.x={p.x} and p.y={p.y}')
print(f'p4.x={p4.x} and p4, y = {p4.y}')
p.x = 20

print(f'p.x={p.x} and p.y={p.y}')