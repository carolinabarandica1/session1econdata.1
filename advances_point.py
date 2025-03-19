from session1_2 import ColorPoint


class PointException(Exception):
    pass


class AdvancedPoint(ColorPoint):
    COLORS = ['red', 'green', 'blue', 'yellow', 'black', 'magenta', 'cyan', 'white', 'burgundy', 'periwinkle',
              'marsala']

    def __init__(self, x, y, color):
        if color not in self.COLORS:
            raise PointException(f'Invalid color, must be one of {self.COLORS}')
        super().__init__(x, y, color)
        self._x = x
        self._y = y
        self._color = color

    @classmethod
    def add_color(cls, color):
        '''
        add a new valid color for our class
        '''
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color='red'):
        '''
        create a new point from a tuple rather than 2 individual viewsa
        '''
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        '''
        calculate the distance between two points
        '''
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, other):
        '''
        calculate the distance to another point
        '''
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color


AdvancedPoint.add_color("rojo")
p = AdvancedPoint(1, 2, "blue")
print(p)
print(p.distance_orig())

p2 = AdvancedPoint.from_tuple((3, 2))
print(p2)
print(AdvancedPoint.distance_2_points(p, p2))
print(p.distance_to_other(p2))


