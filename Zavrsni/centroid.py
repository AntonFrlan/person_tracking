class Centroid():
    def __init__(self, dot, width, height, maxDis=40):
        self.dot = dot
        self.width = width
        self.height = height
        self.oldDot = None
        self.maxDis = maxDis
        self.dis = 0
        self.found = True
        self.speed = 0

    def check(self, xa, ya, xb, yb):
        if self.dot is not None and not self.found:
            if xa < self.dot[0][0] < xb and ya < self.dot[0][1] < yb:
                return True
        return False

    def update(self, dot=None, xa=None, ya=None, xb=None, yb=None):
        if xa is None:
            xa = self.dot[0][0] - self.width
            ya = self.dot[0][1] - self.height
            xb = self.dot[0][0] + self.width
            yb = self.dot[0][1] + self.height
        if not self.found:
            self.width = int((xb - xa) / 2)
            self.height = int((yb - ya) / 2)
            if dot is not None:
                self.dot = dot
            else:
                self.dot[0][0] = (xa + xb) / 2
                self.dot[0][1] = (ya + yb) / 2
            self.found = True

    def disReset(self):
        self.dis = 0

    def old(self):
        if self.oldDot is not None:
            self.speed = self.dot - self.oldDot
        self.oldDot = self.dot

    def changeFound(self):
        self.found = not self.found

    def nestani(self, w, h):
        self.dis += 1
        x = self.dot[0][0]
        y = self.dot[0][1]
        if self.dis >= self.maxDis or x < 0 or y < 0 or x > w or y > h:
            return True
        return False

    def errorLK(self):
        if 60 < abs(self.dot[0][0] - self.oldDot[0][0]) or 60 < abs(self.dot[0][1] - self.oldDot[0][1]):
            return True
        return False
