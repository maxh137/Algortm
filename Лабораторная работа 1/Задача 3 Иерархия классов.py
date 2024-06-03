class Servodrive:
 def __init__(self,turn_angle:float,rotation_speed:float,acceleration:float,weight:int):
  self.angle=turn_angle
  self.speed=rotation_speed
  self.acceleration=acceleration
  self.weight=weight
 def __str__(self):
     return f'Сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
 def __repr__(self):
     return f'Сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'

class Linear(Servodrive): 
 def __init__(self,turn_angle,rotation_speed,acceleration,weight) -> None:
  super().__init__(turn_angle,rotation_speed,acceleration,weight)

class Rotate(Servodrive): 
 def __init__(self,turn_angle,rotation_speed,acceleration,weight) -> None:
  super().__init__(turn_angle,rotation_speed,acceleration,weight)

class Syn(Rotate): 
 def __init__(self,turn_angle,rotation_speed,acceleration,weight) -> None:
  super().__init__(turn_angle,rotation_speed,acceleration,weight)

class Asyn(Rotate): 
 def __init__(self,turn_angle,rotation_speed,acceleration,weight) -> None:
  super().__init__(turn_angle,rotation_speed,acceleration,weight)    


a=Asyn(170,25,92,70)
b=Syn(300,15,48,50)
c=Asyn(160,20,74,50)
d=Linear(270,25,56,60) 
print(str(a))
print(repr(a))
print(str(b))
print(repr(b))
print(str(c))
print(repr(c))
print(str(d))
print(repr(d))

