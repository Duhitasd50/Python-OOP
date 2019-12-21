import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
                (self.x - other_point.x)**2 +
                (self.y - other_point.y)**2)

# how to use it:
point1 = Point()
point2 = Point()

point1.reset()
point2.move(5,0)
print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1) ==
        point1.calculate_distance(point2))
point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))


point = Point()
point.x = 5
print(point.x)
print(point.y)    
# ===================================================================================================
class Point:
    'Represents a point in two-dimensional geometric coordinates'
    def __init__(self, x=0, y=0):
        ''' Intialize the position of a new point. The x and y co-ordinates
        can be specified. If they are not, the point defaults to the origin''' 
        self.move(x, y)
        
    def move(self, x, y):
        '''Move the point to a new location in 2D space'''
        self.x = x
        self.y = y
        
    def reset(self):
        '''Reset the point back to the geometric origin: 0, 0'''
        self.move(0, 0)
        
# constructing a point

point = Point(3)
print(point.x, point.y)
    
    
    
    
    
    