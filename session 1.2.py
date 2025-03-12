from point import Point


class ColorPoint(Point):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"


p = ColorPoint(1, 2, "red")
print(p)

colors = ['red','green','blue','yellow','black','magenta','cyan','white','burgundy','periwinkle','marsala']