import math
from dataclasses import dataclass,field

@dataclass
class Point:
  latitude:float
  longitude:float

@dataclass
class Sphere:
    radius:int
    points:list=field(default_factory=list)

    def addPoint(self,point):
        self.points.append(point)

    def calcDist(self,point1,point2):
         point1.latitude=math.radians(point1.latitude)
         point2.latitude=math.radians(point2.latitude)
         point1.longitude=math.radians(point1.longitude)
         point2.longitude=math.radians(point2.longitude)
         dLatitude=point2.latitude-point1.latitude
         dLongitude=point2.longitude-point1.longitude
         a=math.sin(dLatitude/2)**2+math.cos(point1.latitude)*math.cos(point1.latitude)*math.sin(dLongitude/2)**2
         c=2*math.asin(math.sqrt(a))
         return self.radius*c

earth=Sphere(6371)

Tver=Point(56.8524,35.8235)
Kazan=Point(55.7910,49.1114)
Zero=Point(0.0,0.0)
Negative=Point(-30.0,-30.0)

earth.addPoint(Tver)
earth.addPoint(Kazan)
earth.addPoint(Zero)
earth.addPoint(Negative)

print(earth.calcDist(Tver,Kazan))
print(earth.calcDist(Tver,Zero))
print(earth.calcDist(Kazan,Negative))
