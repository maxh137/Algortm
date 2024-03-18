from dataclasses import dataclass
@dataclass(repr=True)
class Servodrive:
  angle:float
  speed:float
  acceleration:float
  weight:int
  def __str__(self):
     return f'Сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
  def __repr__(self):
     return f'Сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'

@dataclass(order=True,repr=True)
class Linear(Servodrive):
    def __str__(self):
     return f'Линейный сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
    def __repr__(self):
     return f'Линейный сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'


 

@dataclass(order=True,repr=True)
class Rotate(Servodrive):
    def __str__(self):
     return f'Вращательный сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
    def __repr__(self):
     return f'Вращательный сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'


 

@dataclass(order=True,repr=True)
class Syn(Rotate):
    def __str__(self):
     return f'Синхронный сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
    def __repr__(self):
     return f'Синхронный сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'
 

@dataclass(order=True,repr=True)
class Asyn(Rotate):
    def __str__(self):
     return f'Асинхронный сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
    def __repr__(self):
     return f'Асинхронный сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'         


a=Asyn(170,25,92,70)
print(a.angle)  
print(repr(a))
print(str(a))
