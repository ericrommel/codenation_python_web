class Point:
    ''' Point class represents and manipulates x, y coords. '''

    def __init__(self, x=0, y=0):
        ''' Creates a new point at the origin '''
        self.x = x
        self.y = y

    def distance_from_origin(self):
        ''' Compute my distance from the origin '''
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def print_point(self, point):
        print("({0}, {1})".format(point.x, point.y))

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self):
        # return self.to_string()
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        ''' Return the halfway point between myself and the target '''
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

def midpoint(p1, p2):
    ''' Return the midpoint of points p1 and p2 '''
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)
p = Point(0, 0)  # Instantiate an object of type Point
q = Point(3, 4)

print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y

p.x = 3
p.y = 4
q.x = 7
q.y = 10
print("(x={0}, y={1})".format(p.x, p.y), end=". ")
distance_squared_from_origin = p.x * p.x + p.y * p.y
print("Distance squared from origin is {0}".format(distance_squared_from_origin))
print("Using method: ", p.distance_from_origin())
p.print_point(q)
print(p.to_string())
print(str(q))
print(str(p))
s = Point(5, 6)
r = Point(8, 9)
t = midpoint(s, r)
print(t)
u = s.halfway(r)
print(u)
print(Point(3, 4).halfway(Point(5, 12)))
