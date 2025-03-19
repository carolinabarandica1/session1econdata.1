import random
from session1 import Point

class ColorPoint(Point):
    def __init__(self, x, y, color):
        if not isinstance(x,(int,float)):
            raise TypeError ("x must be a number")
        if not isinstance(y,(int,float)):
            raise TypeError("y must be a number")

        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, 2, "red")
print(p.distance_orig())
print(p)

colors = ['red', 'green', 'blue', 'yellow', 'black', 'magenta', 'cyan', 'white', 'burgundy', 'periwinkle', 'marsala']

color_points = []
for i in range(18):
    color_points.append(ColorPoint(random.randint(-10, 10), random.randint(-10, 10), random.choice(colors)))

print(color_points)

color_points.sort(key=lambda p: (p.x**2 + p.y**2))

print(color_points)
color_points.sort()
print(color_points)

