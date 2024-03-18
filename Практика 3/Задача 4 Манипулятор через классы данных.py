from dataclasses import dataclass
@dataclass
class Manipulator:
  x:float
  y:float
  z:float
  def __add__(self,other):
   return Manipulator(self.x + other.x,self.y+other.y,self.z+other.z)
class Link(Manipulator):
  x:float
  y:float
  z:float
Robot=Manipulator(0,0,0)
Position1=Manipulator(20,0,20)
Link1=Link(0,0,40)
Link2=Link(30,0,40)
Link3=Link(30,0,70)
Link4=Link(60,0,70)
Link5=Link(60,0,100)
Link6=Link(80,0,100)
Robot1=Robot+Position1
print(Link6.x)
print(Robot1.x,Robot1.y,Robot1.z)
