import math
import time
from math import pi

class Light:
    """Internal class Light"""

    # ----------------- Light -------------------------------------------------------------
    def __init__(self, x, y, b):
        self._x = x
        self._y = y
        self._b = b

    def setx(self, x):
        self._x = x

    def sety(self, y):
        self._y = y

    def setb(self, b):
        self._b = b

    def setxy(self, x, y):
        self.setx(x)
        self.sety(y)

    def setxyb(self, x, y, b):
        self.setxy(x, y)
        self.setb(b)

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def getb(self):
        return self._b

    def getxy(self):
        return (self._x, self._y)

    def getxyb(self):
        return (self._x, self._y, self._b)

    def move(self, t, d):
        self.setx(math.cos(t) * d)
        self.sety(math.sin(t) * d)

    def movoffset(self, t, d, x, y):
        self.setx(math.cos(t) * d + x)
        self.sety(math.sin(t) * d + y)


# ---------------- End of Light -----------------------------------------------------------------

class Circle:
    """Circle containing all the lights for the sweep"""

    def __init__(self, num_lights, radius = 0.1, brightness=128, parent=None, epsilon=0.1, middle_x =.33, middle_y=.32, ):
        self._n = num_lights
        self._mx = middle_x
        self._my = middle_y
        self._b = brightness
        self._r = radius
        self._parent = parent
        self._e = epsilon
        self._theta = 2*pi/self._n
        self._lights = self.populate()
        self.populate()
        self.initsweep()

    def populate(self):
        lights = []
        for i in range(self._n):
            lights.append(Light(self._mx,self._my,self._b))
        return lights

    def initsweep(self):

        for i in range(self._n):
            self._lights[i].movoffset(i*self._theta, self._r, self._mx, self._my)

    def sweep(self, step):
        offset = 0
        twopi = pi*2
        offset = self._e*step

        for i in range(self._n):
            self._lights[i].movoffset(i * self._theta +offset, self._r, self._mx, self._my)

        return self._lights
