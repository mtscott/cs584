import numpy as np

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y  

class LineSegment:
  def __init__(self, p1, p2):
    self.start = Point(p1.x,p1.y)
    self.end = Point(p2.x, p2.y)

def rhs(LS, p):
    a = Point(LS.start.x - LS.end.x, LS.start.y - LS.end.y)
    b = Point(p.x - LS.end.x, p.y - LS.end.y)
    area = a.x * b.y - a.y * b.x
    
    if np.sign(area) == 1:
        return 1
    elif np.sign(area) == -1:
        return -1
    else:
        return 0
    
def diffside(LS1, LS2):
    prod = rhs(LS1, LS2.start) * rhs(LS1, LS2.end)
    if prod == -1:
        return 1
    else:
        return 0
        
def cross(LS1, LS2):
    a = diffside(LS1, LS2)
    b = diffside(LS2, LS1)
    return (a & b)

def areaTri(p1,p2,p3):
    a = Point(p2.x - p1.x, p2.y - p1.y)
    b = Point(p3.x - p1.x, p3.y - p1.y)
    area = a.x * b.y - a.y * b.x
    return 0.5 * np.abs(area)