import random

class Point:
    def _init_(self,x,y):

        """
        Initialise a point project
        :param x: the x position on the axis
        :param y: the y position on the axis
        """

        self.x=x
        self.y=y

    def _str_(self):
        """
        Magic method tht is called when we try to print an instance
        :return: <x,y>
        """
        return f"p({self.x}, {self.y})"
    def _repr_(self):
        return self._str_()  #use the same way of printing as str

    def distance_orig(self):
        return (self.x*2+self.y2)*0.5 #Square root of the sum of x and y squared

p=Point(1,2) #P is an instance of 1 and 2
p2=Point(2,3)
p4=Point(4.4,-55)

print(f"p.x={p.x} and p.y={p.y}")
print(f"p4.x={p4.x} and p4.y={p4.y}")
p.x=20
print(f"p.x={p.x} and p.y={p.y}")
print(p)

points= []
for i in range(5):
    points.append(Point(random.randint(-10,10),
                       random.randint(-10,10)))
    print("I got these 5 random points:")
    for p in points:
        print(p)

points.sort()
print(points)