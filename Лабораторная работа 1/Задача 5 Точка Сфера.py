import math
class Point:
 def __init__(self,latitude,longitude) -> None:
     self.latitude=math.radians(latitude)
     self.longitude=math.radians(longitude)

class Sphere:
    def __init__(self,radius) -> None:
        self.radius=radius
        self.points=[]

    def addPoint(self,point) -> None:
        self.points.append(point)

    def calcDist(self,point1,point2) -> float:
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
