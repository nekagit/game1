import math


class Vector:

    x: float
    y: float

    def __init__(self, *largs):
        if largs:
            self.x = largs[0]
            self.y = largs[1]
        else:
            self.x = 0
            self.y = 0

    def __del__(self):
        pass

    def __str__(self):
        value = "(" + str(self.x) + ", " + str(self.y) + ")"
        return value

    def __mul__(self, val):
        if type(val) in (int, float):
            self.x *= val
            self.y *= val
            return self
        else:
            return Vector(self.x * val.x, self.y * val.y)

    def __imul__(self, val):
        if type(val) in (int, float):
            self.x *= val
            self.y *= val
        else:
            self.x *= val.x
            self.y *= val.y
        return self

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __iadd__(self, v):
        self.x += v.x
        self.y += v.y
        return self

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __isub__(self, v):
        self.x -= v.x
        self.y -= v.y
        return self

    def invert(self):
        self.x *= -1
        self.y *= -1

    def magnitude(self):
        '''
        Gets the magnitude of the vector
        '''
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def squareMagnitude(self):
        '''
        Gets the magnitude of the vector. 
        Used for e.g comparison since sqrt does not need to be called,
        which can slow down the performance
        '''
        return math.pow(self.x, 2) + math.pow(self.y, 2)

    def normalize(self):
        '''
        Turn a non-zero vector into a vector of unit length
        '''
        l = self.magnitude()
        if(l > 0):
            self.x *= (1/l)
            self.y *= (1/l)

    def addScaledVector(self, v, scale):
        self.x += v.x * scale
        self.y += v.y * scale

    def componentProductUpdate(self, v):
        '''
        Performs a component-wise product with the given vector and
        sets this vector to its result
        '''
        self.x *= v.x
        self.y *= v.y

    def componentProduct(self, v):
        '''
        Calculates and returns a component-wise product of this
        vector with the given vector.
        '''
        return Vector(self.x * v.x, self.y * v.y)

    def scalarProduct(self, v):
        '''
        Calculates and returns a component-wise product of this
        vector with the given vector.
        '''
        return self.x * v.x + self.y + v.y




