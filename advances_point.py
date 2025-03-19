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

    @classmethod
    def add_color(cls, color):
        '''
        add a new valid color for our class
        '''
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate,color ='red'):
        '''
        create a new point from a tuple rather than 2 individual viewsa
        '''
        x,y = coordinate
        return AdvancedPoint(x,y,color)

AdvancedPoint.add_color("rojo")
p = AdvancedPoint(1, 2, "blue")
print(p)
print(p.distance_orig())


