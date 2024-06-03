# Практика №1
1. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры список целых чисел. Вывести в консоль, затем перевернуть его и снова вывести в консоль.
``` python
from random import randint
list_1=[]
for i in range(15):
  list_1.append(randint(1,100))
print('исходный список:',list_1)
list_1.reverse()
print('перевернутый список:',list_1)
'''
[out]:
# 1 выборка входных данных
исходный список: [52, 18, 49, 37, 48, 86, 80, 64, 54, 91, 22, 81, 35, 44, 29]
перевернутый список: [29, 44, 35, 81, 22, 91, 54, 64, 80, 86, 48, 37, 49, 18, 52]
# 2 выборка входных данных
исходный список: [26, 35, 96, 36, 42, 12, 23, 97, 64, 12, 20, 52, 73, 37, 9]
перевернутый список: [9, 37, 73, 52, 20, 12, 64, 97, 23, 12, 42, 36, 96, 35, 26]
# 3 выборка входных данных
исходный список: [59, 69, 51, 27, 29, 99, 19, 77, 6, 61, 54, 100, 58, 58, 44]
перевернутый список: [44, 58, 58, 100, 54, 61, 6, 77, 19, 99, 29, 27, 51, 69, 59]
# 4 выборка входных данных
исходный список: [62, 45, 73, 33, 19, 19, 18, 24, 83, 60, 71, 47, 66, 2, 99]
перевернутый список: [99, 2, 66, 47, 71, 60, 83, 24, 18, 19, 19, 33, 73, 45, 62]
'''
```
2. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры два списка целых чисел. Вывести их в консоль. Создать новый пустой список. Добавить в него все четные (по индексу) элементы первого списка и все нечетные (по индексу) элементы второго списка. Вывести третий список в консоль.
``` python
from random import randint
list_1=[]
for i in range(15):
  list_1.append(randint(1,1000))
print("Первый список:",list_1)
list_2=[]
for i in range(15):
  list_2.append(randint(1,1000))
print("Второй список:",list_2)
list_3=list_1[1::2]+list_2[::2]
print("Третий список с четными из первого и нечетными из второго списка:",list_3)
'''
[out]:
# 1 выборка входных данных
Первый список: [300, 967, 330, 824, 952, 779, 255, 49, 484, 630, 545, 371, 955, 703, 282]
Второй список: [83, 623, 492, 852, 163, 371, 765, 653, 352, 262, 957, 224, 139, 730, 282]
Третий список с четными из первого и нечетными из второго списка: [967, 824, 779, 49, 630, 371, 703, 83, 492, 163, 765, 352, 957, 139, 282]
# 2 выборка входных данных
Первый список: [437, 33, 736, 703, 421, 776, 955, 634, 741, 647, 472, 109, 820, 318, 175]
Второй список: [942, 724, 175, 876, 820, 357, 827, 684, 942, 683, 190, 348, 817, 297, 225]
Третий список с четными из первого и нечетными из второго списка: [33, 703, 776, 634, 647, 109, 318, 942, 175, 820, 827, 942, 190, 817, 225]
# 3 выборка входных данных
Первый список: [883, 554, 789, 687, 347, 116, 612, 324, 650, 200, 228, 366, 999, 860, 665]
Второй список: [773, 943, 640, 882, 610, 70, 898, 708, 837, 21, 909, 570, 806, 731, 874]
Третий список с четными из первого и нечетными из второго списка: [554, 687, 116, 324, 200, 366, 860, 773, 640, 610, 898, 837, 909, 806, 874]
# 4 выборка входных данных
Первый список: [695, 999, 176, 628, 976, 772, 204, 71, 726, 528, 355, 732, 806, 315, 265]
Второй список: [341, 54, 225, 374, 31, 994, 840, 412, 255, 285, 390, 776, 619, 976, 542]
Третий список с четными из первого и нечетными из второго списка: [999, 628, 772, 71, 528, 732, 315, 341, 225, 31, 840, 255, 390, 619, 542]
'''
```
3. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры список произвольных элементов (целые числа, числа с плавающей точкой, строки). Вывести в консоль. Убрать из него все дубликаты через приведение типов. Вывести в консоль.
``` python
from random import randint
list_1=[]
for i in range(20):
  list_1.append(randint(1,10))
print("Исходный список:",list_1)
list_1=list(set(list_1))
print("Список без дубликатов:",list_1)
'''
[out]:
#1 выборка входных данных
Исходный список: [6, 10, 4, 9, 10, 6, 1, 10, 6, 6, 10, 7, 9, 6, 2, 4, 10, 6, 7, 8]
Список без дубликатов: [1, 2, 4, 6, 7, 8, 9, 10]
# 2 выборка входных данных
Исходный список: [7, 1, 10, 8, 9, 5, 2, 6, 1, 3, 9, 1, 4, 5, 6, 1, 9, 10, 5, 2]
Список без дубликатов: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#3 выборка входных данных
Исходный список: [6, 9, 6, 3, 8, 3, 1, 3, 10, 10, 9, 3, 7, 9, 6, 7, 2, 3, 2, 1]
Список без дубликатов: [1, 2, 3, 6, 7, 8, 9, 10]
#4 выборка входных данных
Исходный список: [8, 5, 10, 8, 2, 5, 1, 7, 1, 4, 6, 10, 3, 9, 7, 2, 7, 3, 9, 4]
Список без дубликатов: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
```
4. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры словарь, где ключом является строка, значением — целое число или число с плавающей точкой. Вывести в консоль. Для всех уникальных значений создать кортеж, где первым элементом будет значение, вторым — список связанных с ним ключей. Собрать эти кортежи в список, вывести его в консоль.
```python
#1 выборка входных данных
dicty=dict({'letter':1,'yellow':4,'crayon':2})
print('словарь:',dicty)
a=dicty.values()
b=list(set(a))
tuple_1=()
list_1=[]
for key,value in dicty.items():
 if value in b:
       tuple_1=(value,key)
       list_1.append(tuple_1)
print('список кортежей:',list_1)
'''
[out]:
словарь: {'letter': 1, 'yellow': 4, 'crayon': 2}
список кортежей: [(1, 'letter'), (4, 'yellow'), (2, 'crayon')]
'''
#2 выборка входных данных
dicty=dict({'letter':1,'town':3,'place':5,'hill':6})
print('словарь:',dicty)
a=dicty.values()
b=list(set(a))
tuple_1=()
list_1=[]
for key,value in dicty.items():
 if value in b:
       tuple_1=(value,key)
       list_1.append(tuple_1)
print('список кортежей:',list_1)
'''
[out]:
словарь: {'letter': 1, 'town': 3, 'place': 5, 'hill': 6}
список кортежей: [(1, 'letter'), (3, 'town'), (5, 'place'), (6, 'hill')]
'''
#3 выборка входных данных
dicty=dict({'book':7,'toy':2,'ice':5,'voice':6,'note':8})
print('словарь:',dicty)
a=dicty.values()
b=list(set(a))
tuple_1=()
list_1=[]
for key,value in dicty.items():
 if value in b:
       tuple_1=(value,key)
       list_1.append(tuple_1)
print('список кортежей:',list_1)
'''
[out]:
словарь: {'book': 7, 'toy': 2, 'ice': 5, 'voice': 6, 'note': 8}
список кортежей: [(7, 'book'), (2, 'toy'), (5, 'ice'), (6, 'voice'), (8, 'note')]
'''
#4 выборка входных данных
dicty=dict({'church':10,'home':4,'card':3,'finger':7,'memory':6})
print('словарь:',dicty)
a=dicty.values()
b=list(set(a))
tuple_1=()
list_1=[]
for key,value in dicty.items():
 if value in b:
       tuple_1=(value,key)
       list_1.append(tuple_1)
print('список кортежей:',list_1)
'''
[out]:
словарь: {'church': 10, 'home': 4, 'card': 3, 'finger': 7, 'memory': 6}
список кортежей: [(10, 'church'), (4, 'home'), (3, 'card'), (7, 'finger'), (6, 'memory')]
'''
```
5. Сгенерировать, используя модуль псевдослучайных чисел `random`, или ввести с клавиатуры два словаря, где ключом является строка, значением — целое число или число с плавающей точкой. Вывести в консоль. Найти пересечения множеств значений словарей. Создать новый словарь, содержащий только те пары ключ-значение, значения из которых входит в пересечение. Вывести в консоль.
```python
dicty_1=dict({'letter':7,'building':12,'crayon':2,'book':4,'white':3,'red':6,'green':1,'light':9,'ball':6,'black':2})
print("Первый словарь:",dicty_1)
dicty_2=dict({'milk':11,'notebook':3,'green':1,'book':4,'apple':6,'glasses':10,'watch':5})
print("Второй словарь:",dicty_2)
a=dicty_1.values()
b=dicty_2.values()
c=set(a).intersection(b)
print("Пересечение множеств значений словарей:",c)
dicty_3=dict({})
for k,v in dicty_1.items():
 if v in c:
     dicty_3[k]=v
for k,v in dicty_2.items():
 if v in c:
     dicty_3[k]=v
print("Словарь с пересечениями значений:",dicty_3)
'''
[out]:
#1 выборка входных данных
Первый словарь: {'letter': 7, 'building': 12, 'crayon': 2, 'book': 4, 'white': 3, 'red': 6, 'green': 1, 'light': 9, 'ball': 6, 'black': 2}
Второй словарь: {'milk': 11, 'notebook': 3, 'green': 1, 'book': 4, 'apple': 6, 'glasses': 10, 'watch': 5}
Пересечение множеств значений словарей: {1, 3, 4, 6}
Словарь с пересечениями значений: {'book': 4, 'white': 3, 'red': 6, 'green': 1, 'ball': 6, 'notebook': 3, 'apple': 6}
'''
#2 выборка входных данных
dicty_1=dict({'letter':7,'building':12,'crayon':3,'book':7,'white':3,'red':6,'green':1,'light':9,'ball':11,'black':5})
print("Первый словарь:",dicty_1)
dicty_2=dict({'milk':11,'notebook':5,'green':1,'book':4,'apple':6,'glasses':10,'watch':5,'town':8,'wall':13})
print("Второй словарь:",dicty_2)
a=dicty_1.values()
b=dicty_2.values()
c=set(a).intersection(b)
print("Пересечение множеств значений словарей:",c)
dicty_3=dict({})
for k,v in dicty_1.items():
 if v in c:
     dicty_3[k]=v
for k,v in dicty_2.items():
 if v in c:
     dicty_3[k]=v
print("Словарь с пересечениями значений:",dicty_3)
'''
[out]:
Первый словарь: {'letter': 7, 'building': 12, 'crayon': 3, 'book': 7, 'white': 3, 'red': 6, 'green': 1, 'light': 9, 'ball': 11, 'black': 5}
Второй словарь: {'milk': 11, 'notebook': 5, 'green': 1, 'book': 4, 'apple': 6, 'glasses': 10, 'watch': 5, 'town': 8, 'wall': 13}
Пересечение множеств значений словарей: {1, 11, 5, 6}
Словарь с пересечениями значений: {'red': 6, 'green': 1, 'ball': 11, 'black': 5, 'milk': 11, 'notebook': 5, 'apple': 6, 'watch': 5}
'''
#3 выборка входных данных
dicty_1=dict({'letter':7,'building':12,'crayon':3,'book':7,'white':8,'red':6,'green':1,'light':9,'ball':11,'black':3})
print("Первый словарь:",dicty_1)
dicty_2=dict({'milk':11,'notebook':5,'green':1,'book':4,'apple':6,'glasses':12,'watch':5,'town':2,'wall':4})
print("Второй словарь:",dicty_2)
a=dicty_1.values()
b=dicty_2.values()
c=set(a).intersection(b)
print("Пересечение множеств значений словарей:",c)
dicty_3=dict({})
for k,v in dicty_1.items():
 if v in c:
     dicty_3[k]=v
for k,v in dicty_2.items():
 if v in c:
     dicty_3[k]=v
print("Словарь с пересечениями значений:",dicty_3)
'''
[out]:
Первый словарь: {'letter': 7, 'building': 12, 'crayon': 3, 'book': 7, 'white': 8, 'red': 6, 'green': 1, 'light': 9, 'ball': 11, 'black': 3}
Второй словарь: {'milk': 11, 'notebook': 5, 'green': 1, 'book': 4, 'apple': 6, 'glasses': 12, 'watch': 5, 'town': 2, 'wall': 4}
Пересечение множеств значений словарей: {1, 11, 12, 6}
Словарь с пересечениями значений: {'building': 12, 'red': 6, 'green': 1, 'ball': 11, 'milk': 11, 'apple': 6, 'glasses': 12}
'''
#4 выборка входных данных
dicty_1=dict({'letter':5,'building':2,'crayon':0,'book':7,'white':8,'red':6,'green':1,'light':9,'ball':11,'black':15})
print("Первый словарь:",dicty_1)
dicty_2=dict({'milk':16,'notebook':14,'field':1,'book':4,'apple':6,'glasses':12,'watch':3,'town':2,'wall':4})
print("Второй словарь:",dicty_2)
a=dicty_1.values()
b=dicty_2.values()
c=set(a).intersection(b)
print("Пересечение множеств значений словарей:",c)
dicty_3=dict({})
for k,v in dicty_1.items():
 if v in c:
     dicty_3[k]=v
for k,v in dicty_2.items():
 if v in c:
     dicty_3[k]=v
print("Словарь с пересечениями значений:",dicty_3)
'''
[out]:
Первый словарь: {'letter': 5, 'building': 2, 'crayon': 0, 'book': 7, 'white': 8, 'red': 6, 'green': 1, 'light': 9, 'ball': 11, 'black': 15}
Второй словарь: {'milk': 16, 'notebook': 14, 'field': 1, 'book': 4, 'apple': 6, 'glasses': 12, 'watch': 3, 'town': 2, 'wall': 4}
Пересечение множеств значений словарей: {1, 2, 6}
Словарь с пересечениями значений: {'building': 2, 'red': 6, 'green': 1, 'field': 1, 'apple': 6, 'town': 2}
'''
```
#Практика 2
1. Скопировать из Википедии данные по кодам аэропортов (например, отсюда [https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:\_P](https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_P)). Сохранить их в JSON-подобном формате с использованием словарей. Реализовать функцию получения кода по названию аэропорта. Реализовать и русское, и английское название. Предусмотреть, что аэропорта может не существовать.
``` python
import json
with open('airport.json','r') as file:
 airport_d=json.load(file)
airport_json_string=json.dumps(airport_d)
airport_data=json.loads(airport_d)
print('Введите название аэропорта:')
a=airport_data.get(input())
print('Код аэропорта:',a)

2. Реализовать в консоли таск-трекер. Данные хранить в словаре во время работы программы, выгружать список задач в JSON-файл, при запуске загружать файл (используя модуль `json`). Реализовать возможность ввода произвольной строки с описанием задачи, возможность отметки задания выполненным, возможность ввода произвольных категорий.
``` python
import json
with open('task.json','r') as file:
 task_d=json.load(file)
task_tracker_data=json.loads(task_d)
print(task_tracker_data)
print('Введите описание задачи и степень ее выполнения')
a=json.dumps({input():input()})
new_task=json.loads(a)
task_tracker_data.update(new_task)
print(task_tracker_data)
task_tracker_json_string=json.dumps(task_tracker_data)
with open('task.json','w') as file:
 json.dump(task_tracker_json_string,file)

3. Реализовать в консоли трекер бюджета. Данные хранить в словаре во время работы программы, выгружать список задач в JSON-файл, при запуске загружать файл (используя модуль `json`). Реализовать возможность ввода произвольной строки с описанием операции и суммой расхода/дохода, возможность ввода произвольных категорий.
``` python
import json
budget_d="""
{
	"Изначальный бюджет":"50000",
	"Покупка 1":"-4500",
	"Покупка 2":"-2700"
}
"""
budget_tracker_data=json.loads(budget_d)
with open('budget.json','w') as file:
 json.dump(budget_d,file)
print(budget_tracker_data)
print('Введите описание дохода\расхода и введите сумму дохода\расхода')
a=json.dumps({input():input()})
new_oper=json.loads(a)
budget_tracker_data.update(new_oper)
print(budget_tracker_data)
budget_json_string=json.dumps(budget_tracker_data)
with open('task.json','w') as file:
 json.dump(budget_json_string,file)
```
# Лабораторная работа №1: Особенности ООП в Python
1. Реализовать структуру данных «очередь» (первый пришел, первый ушел) с помощью класса с возможностью просмотра, добавления и удаления элементов.
```python
class Ochered():
 def __init__(self):
  self.queue=[]
 def enqueue(self,item):
  self.queue.append(item)
 def dequeue(self):
     return self.queue.pop(0)
 def size(self):
     return len(self.queue)
Ochered1=Ochered()
Ochered1.enqueue(1)
Ochered1.enqueue(17)
Ochered1.enqueue(32)
Ochered1.enqueue(43)
Ochered1.enqueue(51)
Ochered1.dequeue()
print('очередь 1:',Ochered1.queue)
Ochered2=Ochered()
Ochered2.enqueue(4)
Ochered2.enqueue(11)
Ochered2.enqueue(18)
Ochered2.enqueue(22)
Ochered2.enqueue(25)
Ochered2.enqueue(43)
Ochered2.dequeue()
print('очередь 2:',Ochered2.queue)
Ochered3=Ochered()
Ochered3.enqueue(12)
Ochered3.enqueue(15)
Ochered3.enqueue(27)
Ochered3.enqueue(33)
Ochered3.dequeue()
Ochered3.dequeue()
print('очередь 3:',Ochered3.queue)
Ochered4=Ochered()
Ochered4.enqueue(7)
Ochered4.enqueue(10)
Ochered4.enqueue(28)
Ochered4.enqueue(52)
Ochered4.enqueue(75)
Ochered4.enqueue(86)
Ochered4.dequeue()
print('очередь 4:',Ochered4.queue)
'''
[out]:
очередь 1: [17, 32, 43, 51]
очередь 2: [11, 18, 22, 25, 43]
очередь 3: [27, 33]
очередь 4: [10, 28, 52, 75, 86]
'''
```
2. Реализовать структуру данных «стек» (последний пришел, первый ушел) с помощью класса с возможностью просмотра, добавления и удаления элементов.
```python
class Stek():
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
Stek1=Stek()
Stek1.push(1)
Stek1.push(3)
Stek1.push(10)
Stek1.push(15)
Stek1.push(22)
Stek1.pop()
print('стек 1:',Stek1.stack)
Stek2=Stek()
Stek2.push(2)
Stek2.push(13)
Stek2.push(20)
Stek2.push(35)
Stek2.push(42)
Stek2.push(51)
Stek2.pop()
Stek2.pop()
print('стек 2:',Stek2.stack)
Stek3=Stek()
Stek3.push(3)
Stek3.push(21)
Stek3.push(32)
Stek3.push(45)
Stek3.push(57)
Stek3.push(61)
Stek3.pop()
print('стек 3:',Stek3.stack)
Stek4=Stek()
Stek4.push(4)
Stek4.push(11)
Stek4.push(18)
Stek4.push(21)
Stek4.push(22)
Stek4.push(31)
Stek4.pop()
Stek4.pop()
Stek4.pop()
print('стек 4:',Stek4.stack)
'''
[out]:
стек 1: [1, 3, 10, 15]
стек 2: [2, 13, 20, 35]
стек 3: [3, 21, 32, 45, 57]
стек 4: [4, 11, 18]
'''
```
3. Реализовать иерархию классов, описывающих разные виды объектов одного типа (например, сервоприводов (синхронный/асинхронный/линейный и т.п.). Реализовать минимум 3 уровня иерархии. Реализовать возможность задания характеристик (например, для двигателя это угол поворота, скорость вращения, ускорение и т.п.). Реализовать строковое представление классов «магическими» методами `__str__()` и `__repr__()`, быть готовым пояснить различия этих методов. Перегрузить условные операторы (см. магические методы `__eq__()`, `__ne__()`, `__lt__()`, `__gt__()`, `__le__()`, `__ge__()`) для реализации возможности сравнения экземпляров класса.
``` python
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
 def __str__(self):
     return f'Линейный сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
 def __repr__(self):
     return f'Линейный сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'


class Rotate(Servodrive): 
 def __init__(self,turn_angle,rotation_speed,acceleration,weight) -> None:
  super().__init__(turn_angle,rotation_speed,acceleration,weight)

class Syn(Rotate): 
 def __init__(self,turn_angle,rotation_speed,acceleration,weight) -> None:
  super().__init__(turn_angle,rotation_speed,acceleration,weight)
 def __str__(self):
     return f'Синхронный сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
 def __repr__(self):
     return f'Синхронный сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'


class Asyn(Rotate): 
 def __init__(self,turn_angle,rotation_speed,acceleration,weight) -> None:
  super().__init__(turn_angle,rotation_speed,acceleration,weight)    
 def __str__(self):
     return f'Асинхронный сервопривод имеет максимальный угол вращения {self.angle} градусов,скорость вращения {self.speed} с/60 гр.,обладает ускорением {self.acceleration} м/с2 и весом {self.weight} грамм'
 def __repr__(self):
     return f'Асинхронный сервопривод(\'{self.angle}\',\'{self.speed}\',\'{self.acceleration}\',\'{self.weight}\')'


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
'''
[out]:
Асинхронный сервопривод имеет максимальный угол вращения 170 градусов,скорость вращения 25 с/60 гр.,обладает ускорением 92 м/с2 и весом 70 грамм
Асинхронный сервопривод('170','25','92','70')
Синхронный сервопривод имеет максимальный угол вращения 300 градусов,скорость вращения 15 с/60 гр.,обладает ускорением 48 м/с2 и весом 50 грамм
Синхронный сервопривод('300','15','48','50')
Асинхронный сервопривод имеет максимальный угол вращения 160 градусов,скорость вращения 20 с/60 гр.,обладает ускорением 74 м/с2 и весом 50 грамм
Асинхронный сервопривод('160','20','74','50')
Линейный сервопривод имеет максимальный угол вращения 270 градусов,скорость вращения 25 с/60 гр.,обладает ускорением 56 м/с2 и весом 60 грамм
Линейный сервопривод('270','25','56','60')
'''
```
4. Реализовать упрощенную модель некоего объекта (например, шестизвенного манипулятора с сервоприводами) при помощи иерархии классов. Реализовать функции объекта (например, перемещение манипулятора в пространстве) через перегрузку арифметических операторов (`__add__()` и т.д.).
``` python
class Manipulator:
 def __init__(self,x:float,y:float,z:float):
  self.x=x
  self.y=y
  self.z=z
 def __add__(self,other):
     return Manipulator(self.x + other.x,self.y+other.y,self.z+other.z)
class Link(Manipulator):
 def __init__(self,x,y,z)->None:
  super().__init__(x,y,z)
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

5. Расчет расстояния между точками на сфере по их широте и долготе (взять любые GPS-координаты) при помощи иерархии классов: как минимум, Точка и Сфера (к ней относятся Точки). https://en.wikipedia.org/wiki/Haversine_formula
``` python
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
```
# Практика №3

На основе классов из лабораторной работы №2 (основы ООП) создать набор классов данных, добившись паритета по функциональности — т.е. для, например, Сферы и Точки должен быть также доступен расчет расстояния.

№1(Очередь)
``` python
from dataclasses import dataclass
@dataclass
class Ochered():
  queue=list()
  def enqueue(self,item):
    self.queue.append(item)
  def dequeue(self):
     return self.queue.pop(0)
  def size(self):
     return len(self.queue)
#1 выборка входных данных
Ochered1=Ochered()
Ochered1.enqueue(5)
Ochered1.enqueue(22)
Ochered1.enqueue(44)
Ochered1.enqueue(89)
Ochered1.enqueue(101)
Ochered1.dequeue()
print('очередь:',Ochered1.queue)
'''
[out]:
очередь: [22, 44, 89, 101]
'''
#2 выборка входных данных
Ochered1=Ochered()
Ochered1.enqueue(17)
Ochered1.enqueue(10)
Ochered1.enqueue(43)
Ochered1.enqueue(59)
Ochered1.enqueue(61)
Ochered1.dequeue()
Ochered1.dequeue()
print('очередь:',Ochered1.queue)
'''
[out]:
очередь: [43, 59, 61]
'''
#3 выборка входных данных
Ochered1=Ochered()
Ochered1.enqueue(12)
Ochered1.enqueue(22)
Ochered1.enqueue(43)
Ochered1.enqueue(67)
Ochered1.enqueue(81)
Ochered1.dequeue()
Ochered1.dequeue()
print('очередь:',Ochered1.queue)
'''
[out]:
очередь: [43, 67, 81]
'''
#4 выборка входных данных
Ochered1=Ochered()
Ochered1.enqueue(2)
Ochered1.enqueue(11)
Ochered1.enqueue(23)
Ochered1.enqueue(77)
Ochered1.enqueue(85)
Ochered1.enqueue(92)
Ochered1.dequeue()
print('очередь:',Ochered1.queue)
'''
[out]:
очередь: [11, 23, 77, 85, 92]
'''
```

№2(Стек)
from dataclasses import dataclass
@dataclass
class Stek():
 stack=list()
 def push(self,item):
        self.stack.append(item)
 def pop(self):
        return self.stack.pop()
#1 выборка входных данных
Stek1=Stek()
Stek1.push(4)
Stek1.push(7)
Stek1.push(12)
Stek1.push(15)
Stek1.push(21)
Stek1.pop()
print('стек:',Stek1.stack)
'''
[out]:
стек: [4, 7, 12, 15]
'''
#2 выборка входных данных
Stek1=Stek()
Stek1.push(6)
Stek1.push(9)
Stek1.push(10)
Stek1.push(15)
Stek1.push(23)
Stek1.push(31)
Stek1.pop()
print('стек:',Stek1.stack)
'''
[out]:
стек: [6, 9, 10, 15, 23]
'''
#3 выборка входных данных
Stek1=Stek()
Stek1.push(2)
Stek1.push(7)
Stek1.push(13)
Stek1.push(22)
Stek1.push(33)
Stek1.push(41)
Stek1.pop()
Stek1.pop()
print('стек:',Stek1.stack)
'''
[out]:
стек: [2, 7, 13, 22]
'''
#4 выборка входных данных
Stek1=Stek()
Stek1.push(11)
Stek1.push(20)
Stek1.push(53)
Stek1.push(27)
Stek1.push(38)
Stek1.push(67)
Stek1.pop()
Stek1.pop()
print('стек:',Stek1.stack)
'''
[out]:
стек: [11, 20, 53, 27]
'''
```
№5(Точка и сфера)
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

# Лабораторная работа №3: Элементы функционального программирования в Python

## Блок 1
1. Загрузите список стран из `countries.json`
2. С помощью `map()` создайте новый список, изменив сделав название каждой страны прописным в списке стран.
``` python
import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_2=list(map(lambda x:x.upper(),country_list))
with open('countries_2.json','w') as file:
 json.dump(countries_2,file)
'''
[out]:
["AFGHANISTAN", "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA", "ANTIGUA AND BARBUDA", "ARGENTINA", "ARMENIA", "AUSTRALIA", "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN", "BHUTAN", "BOLIVIA", "BOSNIA AND HERZEGOVINA", "BOTSWANA", "BRAZIL", "BRUNEI", "BULGARIA", "BURKINA FASO", "BURUNDI", "CAMBODIA", "CAMEROON", "CANADA", "CAPE VERDE", "CENTRAL AFRICAN REPUBLIC", "CHAD", "CHILE", "CHINA", "COLOMBI", "COMOROS", "CONGO (BRAZZAVILLE)", "CONGO", "COSTA RICA", "COTE D'IVOIRE", "CROATIA", "CUBA", "CYPRUS", "CZECH REPUBLIC", "DENMARK", "DJIBOUTI", "DOMINICA", "DOMINICAN REPUBLIC", "EAST TIMOR (TIMOR TIMUR)", "ECUADOR", "EGYPT", "EL SALVADOR", "EQUATORIAL GUINEA", "ERITREA", "ESTONIA", "ETHIOPIA", "FIJI", "FINLAND", "FRANCE", "GABON", "GAMBIA, THE", "GEORGIA", "GERMANY", "GHANA", "GREECE", "GRENADA", "GUATEMALA", "GUINEA", "GUINEA-BISSAU", "GUYANA", "HAITI", "HONDURAS", "HUNGARY", "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISRAEL", "ITALY", "JAMAICA", "JAPAN", "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "KOREA, NORTH", "KOREA, SOUTH", "KUWAIT", "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", "LESOTHO", "LIBERIA", "LIBYA", "LIECHTENSTEIN", "LITHUANIA", "LUXEMBOURG", "MACEDONIA", "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES", "MALI", "MALTA", "MARSHALL ISLANDS", "MAURITANIA", "MAURITIUS", "MEXICO", "MICRONESIA", "MOLDOVA", "MONACO", "MONGOLIA", "MOROCCO", "MOZAMBIQUE", "MYANMAR", "NAMIBIA", "NAURU", "NEPAL", "NETHERLANDS", "NEW ZEALAND", "NICARAGUA", "NIGER", "NIGERIA", "NORWAY", "OMAN", "PAKISTAN", "PALAU", "PANAMA", "PAPUA NEW GUINEA", "PARAGUAY", "PERU", "PHILIPPINES", "POLAND", "PORTUGAL", "QATAR", "ROMANIA", "RUSSIA", "RWANDA", "SAINT KITTS AND NEVIS", "SAINT LUCIA", "SAINT VINCENT", "SAMOA", "SAN MARINO", "SAO TOME AND PRINCIPE", "SAUDI ARABIA", "SENEGAL", "SERBIA AND MONTENEGRO", "SEYCHELLES", "SIERRA LEONE", "SINGAPORE", "SLOVAKIA", "SLOVENIA", "SOLOMON ISLANDS", "SOMALIA", "SOUTH AFRICA", "SPAIN", "SRI LANKA", "SUDAN", "SURINAME", "SWAZILAND", "SWEDEN", "SWITZERLAND", "SYRIA", "TAIWAN", "TAJIKISTAN", "TANZANIA", "THAILAND", "TOGO", "TONGA", "TRINIDAD AND TOBAGO", "TUNISIA", "TURKEY", "TURKMENISTAN", "TUVALU", "UGANDA", "UKRAINE", "UNITED ARAB EMIRATES", "UNITED KINGDOM", "UNITED STATES", "URUGUAY", "UZBEKISTAN", "VANUATU", "VATICAN CITY", "VENEZUELA", "VIETNAM", "YEMEN", "ZAMBIA", "ZIMBABWE"]
'''
```
3. С помощью `filter()`, чтобы отфильтровать страны, содержащие `'land'`.
```python
import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_3=list(filter(lambda x:'land' in x,country_list))
with open('countries_3.json','w') as file:
 json.dump(countries_3,file)
'''
[out]:
["Finland", "Iceland", "Ireland", "Marshall Islands", "Netherlands", "New Zealand", "Poland", "Solomon Islands", "Swaziland", "Switzerland", "Thailand"]
'''
```
4. С помощью `filter()`, чтобы отфильтровать страны, содержащие ровно шесть символов.
```python
import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_4=list(filter(lambda x:len(x)==6,country_list))
with open('countries_4.json','w') as file:
 json.dump(countries_4,file)
'''
[out]:
["Angola", "Belize", "Bhutan", "Brazil", "Brunei", "Canada", "Cyprus", "France", "Greece", "Guinea", "Guyana", "Israel", "Jordan", "Kuwait", "Latvia", "Malawi", "Mexico", "Monaco", "Norway", "Panama", "Poland", "Russia", "Rwanda", "Sweden", "Taiwan", "Turkey", "Tuvalu", "Uganda", "Zambia"]
'''
```
5. С помощью `filter()`, чтобы отфильтровать страны, содержащие шесть и более букв в списке стран.
```python
import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_5=list(filter(lambda x:len(x)>=6,country_list))
with open('countries_5.json','w') as file:
 json.dump(countries_5,file)
'''
[out]:
["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Colombi", "Comoros", "Congo (Brazzaville)", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor Timur)", "Ecuador", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Finland", "France", "Gambia, The", "Georgia", "Germany", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Honduras", "Hungary", "Iceland", "Indonesia", "Ireland", "Israel", "Jamaica", "Jordan", "Kazakhstan", "Kiribati", "Korea, North", "Korea, South", "Kuwait", "Kyrgyzstan", "Latvia", "Lebanon", "Lesotho", "Liberia", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Morocco", "Mozambique", "Myanmar", "Namibia", "Netherlands", "New Zealand", "Nicaragua", "Nigeria", "Norway", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Philippines", "Poland", "Portugal", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia and Montenegro", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Sri Lanka", "Suriname", "Swaziland", "Sweden", "Switzerland", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Zambia", "Zimbabwe"]
'''
```
6. С помощью `filter()` для отсеивания стран, начинающихся с буквы `'E'`.
```python
import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_6=list(filter(lambda x:x.find('E')==0,country_list))
with open('countries_6.json','w') as file:
 json.dump(countries_6,file)
'''
[out]:
["East Timor (Timor Timur)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia"]
'''
```
7. С помощью `reduce()` объедините все страны и получите данное предложение на английском языке: Финляндия, Швеция, Дания, Норвегия и Исландия являются странами Северной Европы.
``` python
import json
from functools import reduce
with open('countries.json','r') as file:
 country_list=json.load(file)
Scand=['Финляндия','Швеция','Дания','Норвегия','Исландия']
print(reduce(lambda x,y:x+","+y,Scand)+" являются странами Северной Европы.")
'''
[out]:
Финляндия,Швеция,Дания,Норвегия,Исландия являются странами Северной Европы.
'''
```
9. Используя сначала каррирование, а затем замыкания, объявите функцию `categorize_countries()`, которая возвращает список стран с некоторым общим шаблоном (например, `'land', 'ia', 'island', 'stan'`), который можно менять.
```python
import json
with open('countries.json','r') as file:
 country_list=json.load(file)
#каррирование
def findcountry(x:str,y:str):
    return list(filter(lambda x:y in x,country_list))
categorize_countries=lambda x:lambda y:findcountry(x,y)
countries_9a=categorize_countries(country_list)('ia')
with open('countries_9a.json','w') as file:
 json.dump(countries_9a,file)
#замыкание
def categorize_countries(x:str):
    def findcountry(y:str):
      return list(filter(lambda x:y in x,country_list))
    return findcountry
countries_9b=categorize_countries(country_list)('land')
with open('countries_9b.json','w') as file:
 json.dump(countries_9b,file)
'''
[out]:
["Albania", "Algeria", "Armenia", "Australia", "Austria", "Bolivia", "Bosnia and Herzegovina", "Bulgaria", "Cambodia", "Croatia", "Equatorial Guinea", "Estonia", "Ethiopia", "Gambia, The", "Georgia", "India", "Indonesia", "Latvia", "Liberia", "Lithuania", "Macedonia", "Malaysia", "Mauritania", "Micronesia", "Mongolia", "Namibia", "Nigeria", "Romania", "Russia", "Saint Lucia", "Saudi Arabia", "Serbia and Montenegro", "Slovakia", "Slovenia", "Somalia", "Syria", "Tanzania", "Tunisia", "Zambia"]
["Finland", "Iceland", "Ireland", "Marshall Islands", "Netherlands", "New Zealand", "Poland", "Solomon Islands", "Swaziland", "Switzerland", "Thailand"]
'''
```
10. Используя файл `countries-data.json`, выполните приведенные ниже задания в функциональной парадигме:
    1. Отсортировать страны:
        1. по названию, 
        2. по столице, 
        3. по численности населения
    2. Выявить произвольное число (начать с 10) наиболее распространенных языков и где их используют.
    3. Выявить произвольное число (начать с 10) наиболее населенных стран.
```python
import json
with open ('countries-data.json','r') as file:
    countries_data=json.load(file)    
countries_data.sort(key=lambda x:x.get('name'),reverse=True)#сортировка стран по названию по убыванию
with open('countries_data_sort1.json','w') as file:
    json.dump(countries_data,file)
'''
[out]:
[{"name": "\u0413\u2026land Islands", "capital": "Mariehamn", "languages": ["Swedish"], "population": 28875, "flag": "https://restcountries.eu/data/ala.svg", "currency": "Euro"}, {"name": "Zimbabwe", "capital": "Harare", "languages": ["English", "Shona", "Northern Ndebele"], "population": 14240168, "flag": "https://restcountries.eu/data/zwe.svg", "currency": "Botswana pula"}, {"name": "Zambia", "capital": "Lusaka", "languages": ["English"], "population": 15933883, "flag": "https://restcountries.eu/data/zmb.svg", "currency": "Zambian kwacha"}, {"name": "Yemen", "capital": "Sana'a", "languages": ["Arabic"], "population": 27478000, "flag": "https://restcountries.eu/data/yem.svg", "currency": "Yemeni rial"}, {"name": "Western Sahara", "capital": "El Aai\u0413\u0454n", "languages": ["Spanish"], "population": 510713, "flag": "https://restcountries.eu/data/esh.svg", "currency": "Moroccan dirham"}, {"name": "Wallis and Futuna", "capital": "Mata-Utu", "languages": ["French"], "population": 11750, "flag": "https://restcountries.eu/data/wlf.svg", "currency": "CFP franc"}, {"name": "Virgin Islands (U.S.)", "capital": "Charlotte Amalie", "languages": ["English"], "population": 114743, "flag": "https://restcountries.eu/data/vir.svg", "currency": "United States dollar"}, {"name": "Virgin Islands (British)", "capital": "Road Town", "languages": ["English"], "population": 28514, "flag": "https://restcountries.eu/data/vgb.svg", "currency": "[D]"}, {"name": "Viet Nam", "capital": "Hanoi", "languages": ["Vietnamese"], "population": 92700000, "flag": "https://restcountries.eu/data/vnm.svg", "currency": "Vietnamese \u0414\u2018\u0431\u00bb\u201cng"}, {"name": "Venezuela (Bolivarian Republic of)", "capital": "Caracas", "languages": ["Spanish"], "population": 31028700, "flag": "https://restcountries.eu/data/ven.svg", "currency": "Venezuelan bol\u0413\u00advar"}, {"name": "Vanuatu", "capital": "Port Vila", "languages": ["Bislama", "English", "French"], "population": 277500, "flag": "https://restcountries.eu/data/vut.svg", "currency": "Vanuatu vatu"}, {"name": "Uzbekistan", "capital": "Tashkent", "languages": ["Uzbek", "Russian"], "population": 31576400, "flag": "https://restcountries.eu/data/uzb.svg", "currency": "Uzbekistani so'm"}, {"name": "Uruguay", "capital": "Montevideo", "languages": ["Spanish"], "population": 3480222, "flag": "https://restcountries.eu/data/ury.svg", "currency": "Uruguayan peso"}, {"name": "United States of America", "capital": "Washington, D.C.", "languages": ["English"], "population": 323947000, "flag": "https://restcountries.eu/data/usa.svg", "currency": "United States dollar"}, {"name": "United States Minor Outlying Islands", "capital": "", "languages": ["English"], "population": 300, "flag": "https://restcountries.eu/data/umi.svg", "currency": "United States Dollar"}, {"name": "United Kingdom of Great Britain and Northern Ireland", "capital": "London", "languages": ["English"], "population": 65110000, "flag": "https://restcountries.eu/data/gbr.svg", "currency": "British pound"}, {"name": "United Arab Emirates", "capital": "Abu Dhabi", "languages": ["Arabic"], "population": 9856000, "flag": "https://restcountries.eu/data/are.svg", "currency": "United Arab Emirates dirham"}, {"name": "Ukraine", "capital": "Kiev", "languages": ["Ukrainian"], "population": 42692393, "flag": "https://restcountries.eu/data/ukr.svg", "currency": "Ukrainian hryvnia"}, {"name": "Uganda", "capital": "Kampala", "languages": ["English", "Swahili"], "population": 33860700, "flag": "https://restcountries.eu/data/uga.svg", "currency": "Ugandan shilling"}, {"name": "Tuvalu", "capital": "Funafuti", "languages": ["English"], "population": 10640, "flag": "https://restcountries.eu/data/tuv.svg", "currency": "Australian dollar"}, {"name": "Turks and Caicos Islands", "capital": "Cockburn Town", "languages": ["English"], "population": 31458, "flag": "https://restcountries.eu/data/tca.svg", "currency": "United States dollar"}, {"name": "Turkmenistan", "capital": "Ashgabat", "languages": ["Turkmen", "Russian"], "population": 4751120, "flag": "https://restcountries.eu/data/tkm.svg", "currency": "Turkmenistan manat"}, {"name": "Turkey", "capital": "Ankara", "languages": ["Turkish"], "population": 78741053, "flag": "https://restcountries.eu/data/tur.svg", "currency": "Turkish lira"}, {"name": "Tunisia", "capital": "Tunis", "languages": ["Arabic"], "population": 11154400, "flag": "https://restcountries.eu/data/tun.svg", "currency": "Tunisian dinar"}, {"name": "Trinidad and Tobago", "capital": "Port of Spain", "languages": ["English"], "population": 1349667, "flag": "https://restcountries.eu/data/tto.svg", "currency": "Trinidad and Tobago dollar"}, {"name": "Tonga", "capital": "Nuku'alofa", "languages": ["English", "Tonga (Tonga Islands)"], "population": 103252, "flag": "https://restcountries.eu/data/ton.svg", "currency": "Tongan pa\u041a\u00bbanga"}, {"name": "Tokelau", "capital": "Fakaofo", "languages": ["English"], "population": 1411, "flag": "https://restcountries.eu/data/tkl.svg", "currency": "New Zealand dollar"}, {"name": "Togo", "capital": "Lom\u0413\u00a9", "languages": ["French"], "population": 7143000, "flag": "https://restcountries.eu/data/tgo.svg", "currency": "West African CFA franc"}, {"name": "Timor-Leste", "capital": "Dili", "languages": ["Portuguese"], "population": 1167242, "flag": "https://restcountries.eu/data/tls.svg", "currency": "United States dollar"}, {"name": "Thailand", "capital": "Bangkok", "languages": ["Thai"], "population": 65327652, "flag": "https://restcountries.eu/data/tha.svg", "currency": "Thai baht"}, {"name": "Tanzania, United Republic of", "capital": "Dodoma", "languages": ["Swahili", "English"], "population": 55155000, "flag": "https://restcountries.eu/data/tza.svg", "currency": "Tanzanian shilling"}, {"name": "Tajikistan", "capital": "Dushanbe", "languages": ["Tajik", "Russian"], "population": 8593600, "flag": "https://restcountries.eu/data/tjk.svg", "currency": "Tajikistani somoni"}, {"name": "Taiwan", "capital": "Taipei", "languages": ["Chinese"], "population": 23503349, "flag": "https://restcountries.eu/data/twn.svg", "currency": "New Taiwan dollar"}, {"name": "Syrian Arab Republic", "capital": "Damascus", "languages": ["Arabic"], "population": 18564000, "flag": "https://restcountries.eu/data/syr.svg", "currency": "Syrian pound"}, {"name": "Switzerland", "capital": "Bern", "languages": ["German", "French", "Italian"], "population": 8341600, "flag": "https://restcountries.eu/data/che.svg", "currency": "Swiss franc"}, {"name": "Sweden", "capital": "Stockholm", "languages": ["Swedish"], "population": 9894888, "flag": "https://restcountries.eu/data/swe.svg", "currency": "Swedish krona"}, {"name": "Swaziland", "capital": "Lobamba", "languages": ["English", "Swati"], "population": 1132657, "flag": "https://restcountries.eu/data/swz.svg", "currency": "Swazi lilangeni"}, {"name": "Svalbard and Jan Mayen", "capital": "Longyearbyen", "languages": ["Norwegian"], "population": 2562, "flag": "https://restcountries.eu/data/sjm.svg", "currency": "Norwegian krone"}, {"name": "Suriname", "capital": "Paramaribo", "languages": ["Dutch"], "population": 541638, "flag": "https://restcountries.eu/data/sur.svg", "currency": "Surinamese dollar"}, {"name": "Sudan", "capital": "Khartoum", "languages": ["Arabic", "English"], "population": 39598700, "flag": "https://restcountries.eu/data/sdn.svg", "currency": "Sudanese pound"}, {"name": "Sri Lanka", "capital": "Colombo", "languages": ["Sinhalese", "Tamil"], "population": 20966000, "flag": "https://restcountries.eu/data/lka.svg", "currency": "Sri Lankan rupee"}, {"name": "Spain", "capital": "Madrid", "languages": ["Spanish"], "population": 46438422, "flag": "https://restcountries.eu/data/esp.svg", "currency": "Euro"}, {"name": "South Sudan", "capital": "Juba", "languages": ["English"], "population": 12131000, "flag": "https://restcountries.eu/data/ssd.svg", "currency": "South Sudanese pound"}, {"name": "South Georgia and the South Sandwich Islands", "capital": "King Edward Point", "languages": ["English"], "population": 30, "flag": "https://restcountries.eu/data/sgs.svg", "currency": "British pound"}, {"name": "South Africa", "capital": "Pretoria", "languages": ["Afrikaans", "English", "Southern Ndebele", "Southern Sotho", "Swati", "Tswana", "Tsonga", "Venda", "Xhosa", "Zulu"], "population": 55653654, "flag": "https://restcountries.eu/data/zaf.svg", "currency": "South African rand"}, {"name": "Somalia", "capital": "Mogadishu", "languages": ["Somali", "Arabic"], "population": 11079000, "flag": "https://restcountries.eu/data/som.svg", "currency": "Somali shilling"}, {"name": "Solomon Islands", "capital": "Honiara", "languages": ["English"], "population": 642000, "flag": "https://restcountries.eu/data/slb.svg", "currency": "Solomon Islands dollar"}, {"name": "Slovenia", "capital": "Ljubljana", "languages": ["Slovene"], "population": 2064188, "flag": "https://restcountries.eu/data/svn.svg", "currency": "Euro"}, {"name": "Slovakia", "capital": "Bratislava", "languages": ["Slovak"], "population": 5426252, "flag": "https://restcountries.eu/data/svk.svg", "currency": "Euro"}, {"name": "Sint Maarten (Dutch part)", "capital": "Philipsburg", "languages": ["Dutch", "English"], "population": 38247, "flag": "https://restcountries.eu/data/sxm.svg", "currency": "Netherlands Antillean guilder"}, {"name": "Singapore", "capital": "Singapore", "languages": ["English", "Malay", "Tamil", "Chinese"], "population": 5535000, "flag": "https://restcountries.eu/data/sgp.svg", "currency": "Brunei dollar"}, {"name": "Sierra Leone", "capital": "Freetown", "languages": ["English"], "population": 7075641, "flag": "https://restcountries.eu/data/sle.svg", "currency": "Sierra Leonean leone"}, {"name": "Seychelles", "capital": "Victoria", "languages": ["French", "English"], "population": 91400, "flag": "https://restcountries.eu/data/syc.svg", "currency": "Seychellois rupee"}, {"name": "Serbia", "capital": "Belgrade", "languages": ["Serbian"], "population": 7076372, "flag": "https://restcountries.eu/data/srb.svg", "currency": "Serbian dinar"}, {"name": "Senegal", "capital": "Dakar", "languages": ["French"], "population": 14799859, "flag": "https://restcountries.eu/data/sen.svg", "currency": "West African CFA franc"}, {"name": "Saudi Arabia", "capital": "Riyadh", "languages": ["Arabic"], "population": 32248200, "flag": "https://restcountries.eu/data/sau.svg", "currency": "Saudi riyal"}, {"name": "Sao Tome and Principe", "capital": "S\u0413\u0408o Tom\u0413\u00a9", "languages": ["Portuguese"], "population": 187356, "flag": "https://restcountries.eu/data/stp.svg", "currency": "S\u0413\u0408o Tom\u0413\u00a9 and Pr\u0413\u00adncipe dobra"}, {"name": "San Marino", "capital": "City of San Marino", "languages": ["Italian"], "population": 33005, "flag": "https://restcountries.eu/data/smr.svg", "currency": "Euro"}, {"name": "Samoa", "capital": "Apia", "languages": ["Samoan", "English"], "population": 194899, "flag": "https://restcountries.eu/data/wsm.svg", "currency": "Samoan t\u0414\u0403l\u0414\u0403"}, {"name": "Saint Vincent and the Grenadines", "capital": "Kingstown", "languages": ["English"], "population": 109991, "flag": "https://restcountries.eu/data/vct.svg", "currency": "East Caribbean dollar"}, {"name": "Saint Pierre and Miquelon", "capital": "Saint-Pierre", "languages": ["French"], "population": 6069, "flag": "https://restcountries.eu/data/spm.svg", "currency": "Euro"}, {"name": "Saint Martin (French part)", "capital": "Marigot", "languages": ["English", "French", "Dutch"], "population": 36979, "flag": "https://restcountries.eu/data/maf.svg", "currency": "Euro"}, {"name": "Saint Lucia", "capital": "Castries", "languages": ["English"], "population": 186000, "flag": "https://restcountries.eu/data/lca.svg", "currency": "East Caribbean dollar"}, {"name": "Saint Kitts and Nevis", "capital": "Basseterre", "languages": ["English"], "population": 46204, "flag": "https://restcountries.eu/data/kna.svg", "currency": "East Caribbean dollar"}, {"name": "Saint Helena, Ascension and Tristan da Cunha", "capital": "Jamestown", "languages": ["English"], "population": 4255, "flag": "https://restcountries.eu/data/shn.svg", "currency": "Saint Helena pound"}, {"name": "Saint Barth\u0413\u00a9lemy", "capital": "Gustavia", "languages": ["French"], "population": 9417, "flag": "https://restcountries.eu/data/blm.svg", "currency": "Euro"}, {"name": "R\u0413\u00a9union", "capital": "Saint-Denis", "languages": ["French"], "population": 840974, "flag": "https://restcountries.eu/data/reu.svg", "currency": "Euro"}, {"name": "Rwanda", "capital": "Kigali", "languages": ["Kinyarwanda", "English", "French"], "population": 11553188, "flag": "https://restcountries.eu/data/rwa.svg", "currency": "Rwandan franc"}, {"name": "Russian Federation", "capital": "Moscow", "languages": ["Russian"], "population": 146599183, "flag": "https://restcountries.eu/data/rus.svg", "currency": "Russian ruble"}, {"name": "Romania", "capital": "Bucharest", "languages": ["Romanian"], "population": 19861408, "flag": "https://restcountries.eu/data/rou.svg", "currency": "Romanian leu"}, {"name": "Republic of Kosovo", "capital": "Pristina", "languages": ["Albanian", "Serbian"], "population": 1733842, "flag": "https://restcountries.eu/data/kos.svg", "currency": "Euro"}, {"name": "Qatar", "capital": "Doha", "languages": ["Arabic"], "population": 2587564, "flag": "https://restcountries.eu/data/qat.svg", "currency": "Qatari riyal"}, {"name": "Puerto Rico", "capital": "San Juan", "languages": ["Spanish", "English"], "population": 3474182, "flag": "https://restcountries.eu/data/pri.svg", "currency": "United States dollar"}, {"name": "Portugal", "capital": "Lisbon", "languages": ["Portuguese"], "population": 10374822, "flag": "https://restcountries.eu/data/prt.svg", "currency": "Euro"}, {"name": "Poland", "capital": "Warsaw", "languages": ["Polish"], "population": 38437239, "flag": "https://restcountries.eu/data/pol.svg", "currency": "Polish z\u0415\u201aoty"}, {"name": "Pitcairn", "capital": "Adamstown", "languages": ["English"], "population": 56, "flag": "https://restcountries.eu/data/pcn.svg", "currency": "New Zealand dollar"}, {"name": "Philippines", "capital": "Manila", "languages": ["English"], "population": 103279800, "flag": "https://restcountries.eu/data/phl.svg", "currency": "Philippine peso"}, {"name": "Peru", "capital": "Lima", "languages": ["Spanish"], "population": 31488700, "flag": "https://restcountries.eu/data/per.svg", "currency": "Peruvian sol"}, {"name": "Paraguay", "capital": "Asunci\u0413\u0456n", "languages": ["Spanish", "Guaran\u0413\u00ad"], "population": 6854536, "flag": "https://restcountries.eu/data/pry.svg", "currency": "Paraguayan guaran\u0413\u00ad"}, {"name": "Papua New Guinea", "capital": "Port Moresby", "languages": ["English"], "population": 8083700, "flag": "https://restcountries.eu/data/png.svg", "currency": "Papua New Guinean kina"}, {"name": "Panama", "capital": "Panama City", "languages": ["Spanish"], "population": 3814672, "flag": "https://restcountries.eu/data/pan.svg", "currency": "Panamanian balboa"}, {"name": "Palestine, State of", "capital": "Ramallah", "languages": ["Arabic"], "population": 4682467, "flag": "https://restcountries.eu/data/pse.svg", "currency": "Israeli new sheqel"}, {"name": "Palau", "capital": "Ngerulmud", "languages": ["English"], "population": 17950, "flag": "https://restcountries.eu/data/plw.svg", "currency": "[E]"}, {"name": "Pakistan", "capital": "Islamabad", "languages": ["English", "Urdu"], "population": 194125062, "flag": "https://restcountries.eu/data/pak.svg", "currency": "Pakistani rupee"}, {"name": "Oman", "capital": "Muscat", "languages": ["Arabic"], "population": 4420133, "flag": "https://restcountries.eu/data/omn.svg", "currency": "Omani rial"}, {"name": "Norway", "capital": "Oslo", "languages": ["Norwegian", "Norwegian Bokm\u0413\u0490l", "Norwegian Nynorsk"], "population": 5223256, "flag": "https://restcountries.eu/data/nor.svg", "currency": "Norwegian krone"}, {"name": "Northern Mariana Islands", "capital": "Saipan", "languages": ["English", "Chamorro"], "population": 56940, "flag": "https://restcountries.eu/data/mnp.svg", "currency": "United States dollar"}, {"name": "Norfolk Island", "capital": "Kingston", "languages": ["English"], "population": 2302, "flag": "https://restcountries.eu/data/nfk.svg", "currency": "Australian dollar"}, {"name": "Niue", "capital": "Alofi", "languages": ["English"], "population": 1470, "flag": "https://restcountries.eu/data/niu.svg", "currency": "New Zealand dollar"}, {"name": "Nigeria", "capital": "Abuja", "languages": ["English"], "population": 186988000, "flag": "https://restcountries.eu/data/nga.svg", "currency": "Nigerian naira"}, {"name": "Niger", "capital": "Niamey", "languages": ["French"], "population": 20715000, "flag": "https://restcountries.eu/data/ner.svg", "currency": "West African CFA franc"}, {"name": "Nicaragua", "capital": "Managua", "languages": ["Spanish"], "population": 6262703, "flag": "https://restcountries.eu/data/nic.svg", "currency": "Nicaraguan c\u0413\u0456rdoba"}, {"name": "New Zealand", "capital": "Wellington", "languages": ["English", "M\u0414\u0403ori"], "population": 4697854, "flag": "https://restcountries.eu/data/nzl.svg", "currency": "New Zealand dollar"}, {"name": "New Caledonia", "capital": "Noum\u0413\u00a9a", "languages": ["French"], "population": 268767, "flag": "https://restcountries.eu/data/ncl.svg", "currency": "CFP franc"}, {"name": "Netherlands", "capital": "Amsterdam", "languages": ["Dutch"], "population": 17019800, "flag": "https://restcountries.eu/data/nld.svg", "currency": "Euro"}, {"name": "Nepal", "capital": "Kathmandu", "languages": ["Nepali"], "population": 28431500, "flag": "https://restcountries.eu/data/npl.svg", "currency": "Nepalese rupee"}, {"name": "Nauru", "capital": "Yaren", "languages": ["English", "Nauruan"], "population": 10084, "flag": "https://restcountries.eu/data/nru.svg", "currency": "Australian dollar"}, {"name": "Namibia", "capital": "Windhoek", "languages": ["English", "Afrikaans"], "population": 2324388, "flag": "https://restcountries.eu/data/nam.svg", "currency": "Namibian dollar"}, {"name": "Myanmar", "capital": "Naypyidaw", "languages": ["Burmese"], "population": 51419420, "flag": "https://restcountries.eu/data/mmr.svg", "currency": "Burmese kyat"}, {"name": "Mozambique", "capital": "Maputo", "languages": ["Portuguese"], "population": 26423700, "flag": "https://restcountries.eu/data/moz.svg", "currency": "Mozambican metical"}, {"name": "Morocco", "capital": "Rabat", "languages": ["Arabic"], "population": 33337529, "flag": "https://restcountries.eu/data/mar.svg", "currency": "Moroccan dirham"}, {"name": "Montserrat", "capital": "Plymouth", "languages": ["English"], "population": 4922, "flag": "https://restcountries.eu/data/msr.svg", "currency": "East Caribbean dollar"}, {"name": "Montenegro", "capital": "Podgorica", "languages": ["Serbian", "Bosnian", "Albanian", "Croatian"], "population": 621810, "flag": "https://restcountries.eu/data/mne.svg", "currency": "Euro"}, {"name": "Mongolia", "capital": "Ulan Bator", "languages": ["Mongolian"], "population": 3093100, "flag": "https://restcountries.eu/data/mng.svg", "currency": "Mongolian t\u0413\u00b6gr\u0413\u00b6g"}, {"name": "Monaco", "capital": "Monaco", "languages": ["French"], "population": 38400, "flag": "https://restcountries.eu/data/mco.svg", "currency": "Euro"}, {"name": "Moldova (Republic of)", "capital": "Chi\u0418\u2122in\u0414\u0453u", "languages": ["Romanian"], "population": 3553100, "flag": "https://restcountries.eu/data/mda.svg", "currency": "Moldovan leu"}, {"name": "Micronesia (Federated States of)", "capital": "Palikir", "languages": ["English"], "population": 102800, "flag": "https://restcountries.eu/data/fsm.svg", "currency": "[D]"}, {"name": "Mexico", "capital": "Mexico City", "languages": ["Spanish"], "population": 122273473, "flag": "https://restcountries.eu/data/mex.svg", "currency": "Mexican peso"}, {"name": "Mayotte", "capital": "Mamoudzou", "languages": ["French"], "population": 226915, "flag": "https://restcountries.eu/data/myt.svg", "currency": "Euro"}, {"name": "Mauritius", "capital": "Port Louis", "languages": ["English"], "population": 1262879, "flag": "https://restcountries.eu/data/mus.svg", "currency": "Mauritian rupee"}, {"name": "Mauritania", "capital": "Nouakchott", "languages": ["Arabic"], "population": 3718678, "flag": "https://restcountries.eu/data/mrt.svg", "currency": "Mauritanian ouguiya"}, {"name": "Martinique", "capital": "Fort-de-France", "languages": ["French"], "population": 378243, "flag": "https://restcountries.eu/data/mtq.svg", "currency": "Euro"}, {"name": "Marshall Islands", "capital": "Majuro", "languages": ["English", "Marshallese"], "population": 54880, "flag": "https://restcountries.eu/data/mhl.svg", "currency": "United States dollar"}, {"name": "Malta", "capital": "Valletta", "languages": ["Maltese", "English"], "population": 425384, "flag": "https://restcountries.eu/data/mlt.svg", "currency": "Euro"}, {"name": "Mali", "capital": "Bamako", "languages": ["French"], "population": 18135000, "flag": "https://restcountries.eu/data/mli.svg", "currency": "West African CFA franc"}, {"name": "Maldives", "capital": "Mal\u0413\u00a9", "languages": ["Divehi"], "population": 344023, "flag": "https://restcountries.eu/data/mdv.svg", "currency": "Maldivian rufiyaa"}, {"name": "Malaysia", "capital": "Kuala Lumpur", "languages": ["Malaysian"], "population": 31405416, "flag": "https://restcountries.eu/data/mys.svg", "currency": "Malaysian ringgit"}, {"name": "Malawi", "capital": "Lilongwe", "languages": ["English", "Chichewa"], "population": 16832910, "flag": "https://restcountries.eu/data/mwi.svg", "currency": "Malawian kwacha"}, {"name": "Madagascar", "capital": "Antananarivo", "languages": ["French", "Malagasy"], "population": 22434363, "flag": "https://restcountries.eu/data/mdg.svg", "currency": "Malagasy ariary"}, {"name": "Macedonia (the former Yugoslav Republic of)", "capital": "Skopje", "languages": ["Macedonian"], "population": 2058539, "flag": "https://restcountries.eu/data/mkd.svg", "currency": "Macedonian denar"}, {"name": "Macao", "capital": "", "languages": ["Chinese", "Portuguese"], "population": 649100, "flag": "https://restcountries.eu/data/mac.svg", "currency": "Macanese pataca"}, {"name": "Luxembourg", "capital": "Luxembourg", "languages": ["French", "German", "Luxembourgish"], "population": 576200, "flag": "https://restcountries.eu/data/lux.svg", "currency": "Euro"}, {"name": "Lithuania", "capital": "Vilnius", "languages": ["Lithuanian"], "population": 2872294, "flag": "https://restcountries.eu/data/ltu.svg", "currency": "Euro"}, {"name": "Liechtenstein", "capital": "Vaduz", "languages": ["German"], "population": 37623, "flag": "https://restcountries.eu/data/lie.svg", "currency": "Swiss franc"}, {"name": "Libya", "capital": "Tripoli", "languages": ["Arabic"], "population": 6385000, "flag": "https://restcountries.eu/data/lby.svg", "currency": "Libyan dinar"}, {"name": "Liberia", "capital": "Monrovia", "languages": ["English"], "population": 4615000, "flag": "https://restcountries.eu/data/lbr.svg", "currency": "Liberian dollar"}, {"name": "Lesotho", "capital": "Maseru", "languages": ["English", "Southern Sotho"], "population": 1894194, "flag": "https://restcountries.eu/data/lso.svg", "currency": "Lesotho loti"}, {"name": "Lebanon", "capital": "Beirut", "languages": ["Arabic", "French"], "population": 5988000, "flag": "https://restcountries.eu/data/lbn.svg", "currency": "Lebanese pound"}, {"name": "Latvia", "capital": "Riga", "languages": ["Latvian"], "population": 1961600, "flag": "https://restcountries.eu/data/lva.svg", "currency": "Euro"}, {"name": "Lao People's Democratic Republic", "capital": "Vientiane", "languages": ["Lao"], "population": 6492400, "flag": "https://restcountries.eu/data/lao.svg", "currency": "Lao kip"}, {"name": "Kyrgyzstan", "capital": "Bishkek", "languages": ["Kyrgyz", "Russian"], "population": 6047800, "flag": "https://restcountries.eu/data/kgz.svg", "currency": "Kyrgyzstani som"}, {"name": "Kuwait", "capital": "Kuwait City", "languages": ["Arabic"], "population": 4183658, "flag": "https://restcountries.eu/data/kwt.svg", "currency": "Kuwaiti dinar"}, {"name": "Korea (Republic of)", "capital": "Seoul", "languages": ["Korean"], "population": 50801405, "flag": "https://restcountries.eu/data/kor.svg", "currency": "South Korean won"}, {"name": "Korea (Democratic People's Republic of)", "capital": "Pyongyang", "languages": ["Korean"], "population": 25281000, "flag": "https://restcountries.eu/data/prk.svg", "currency": "North Korean won"}, {"name": "Kiribati", "capital": "South Tarawa", "languages": ["English"], "population": 113400, "flag": "https://restcountries.eu/data/kir.svg", "currency": "Australian dollar"}, {"name": "Kenya", "capital": "Nairobi", "languages": ["English", "Swahili"], "population": 47251000, "flag": "https://restcountries.eu/data/ken.svg", "currency": "Kenyan shilling"}, {"name": "Kazakhstan", "capital": "Astana", "languages": ["Kazakh", "Russian"], "population": 17753200, "flag": "https://restcountries.eu/data/kaz.svg", "currency": "Kazakhstani tenge"}, {"name": "Jordan", "capital": "Amman", "languages": ["Arabic"], "population": 9531712, "flag": "https://restcountries.eu/data/jor.svg", "currency": "Jordanian dinar"}, {"name": "Jersey", "capital": "Saint Helier", "languages": ["English", "French"], "population": 100800, "flag": "https://restcountries.eu/data/jey.svg", "currency": "British pound"}, {"name": "Japan", "capital": "Tokyo", "languages": ["Japanese"], "population": 126960000, "flag": "https://restcountries.eu/data/jpn.svg", "currency": "Japanese yen"}, {"name": "Jamaica", "capital": "Kingston", "languages": ["English"], "population": 2723246, "flag": "https://restcountries.eu/data/jam.svg", "currency": "Jamaican dollar"}, {"name": "Italy", "capital": "Rome", "languages": ["Italian"], "population": 60665551, "flag": "https://restcountries.eu/data/ita.svg", "currency": "Euro"}, {"name": "Israel", "capital": "Jerusalem", "languages": ["Hebrew (modern)", "Arabic"], "population": 8527400, "flag": "https://restcountries.eu/data/isr.svg", "currency": "Israeli new shekel"}, {"name": "Isle of Man", "capital": "Douglas", "languages": ["English", "Manx"], "population": 84497, "flag": "https://restcountries.eu/data/imn.svg", "currency": "British pound"}, {"name": "Ireland", "capital": "Dublin", "languages": ["Irish", "English"], "population": 6378000, "flag": "https://restcountries.eu/data/irl.svg", "currency": "Euro"}, {"name": "Iraq", "capital": "Baghdad", "languages": ["Arabic", "Kurdish"], "population": 37883543, "flag": "https://restcountries.eu/data/irq.svg", "currency": "Iraqi dinar"}, {"name": "Iran (Islamic Republic of)", "capital": "Tehran", "languages": ["Persian (Farsi)"], "population": 79369900, "flag": "https://restcountries.eu/data/irn.svg", "currency": "Iranian rial"}, {"name": "Indonesia", "capital": "Jakarta", "languages": ["Indonesian"], "population": 258705000, "flag": "https://restcountries.eu/data/idn.svg", "currency": "Indonesian rupiah"}, {"name": "India", "capital": "New Delhi", "languages": ["Hindi", "English"], "population": 1295210000, "flag": "https://restcountries.eu/data/ind.svg", "currency": "Indian rupee"}, {"name": "Iceland", "capital": "Reykjav\u0413\u00adk", "languages": ["Icelandic"], "population": 334300, "flag": "https://restcountries.eu/data/isl.svg", "currency": "Icelandic kr\u0413\u0456na"}, {"name": "Hungary", "capital": "Budapest", "languages": ["Hungarian"], "population": 9823000, "flag": "https://restcountries.eu/data/hun.svg", "currency": "Hungarian forint"}, {"name": "Hong Kong", "capital": "City of Victoria", "languages": ["English", "Chinese"], "population": 7324300, "flag": "https://restcountries.eu/data/hkg.svg", "currency": "Hong Kong dollar"}, {"name": "Honduras", "capital": "Tegucigalpa", "languages": ["Spanish"], "population": 8576532, "flag": "https://restcountries.eu/data/hnd.svg", "currency": "Honduran lempira"}, {"name": "Holy See", "capital": "Rome", "languages": ["Latin", "Italian", "French", "German"], "population": 451, "flag": "https://restcountries.eu/data/vat.svg", "currency": "Euro"}, {"name": "Heard Island and McDonald Islands", "capital": "", "languages": ["English"], "population": 0, "flag": "https://restcountries.eu/data/hmd.svg", "currency": "Australian dollar"}, {"name": "Haiti", "capital": "Port-au-Prince", "languages": ["French", "Haitian"], "population": 11078033, "flag": "https://restcountries.eu/data/hti.svg", "currency": "Haitian gourde"}, {"name": "Guyana", "capital": "Georgetown", "languages": ["English"], "population": 746900, "flag": "https://restcountries.eu/data/guy.svg", "currency": "Guyanese dollar"}, {"name": "Guinea-Bissau", "capital": "Bissau", "languages": ["Portuguese"], "population": 1547777, "flag": "https://restcountries.eu/data/gnb.svg", "currency": "West African CFA franc"}, {"name": "Guinea", "capital": "Conakry", "languages": ["French", "Fula"], "population": 12947000, "flag": "https://restcountries.eu/data/gin.svg", "currency": "Guinean franc"}, {"name": "Guernsey", "capital": "St. Peter Port", "languages": ["English", "French"], "population": 62999, "flag": "https://restcountries.eu/data/ggy.svg", "currency": "British pound"}, {"name": "Guatemala", "capital": "Guatemala City", "languages": ["Spanish"], "population": 16176133, "flag": "https://restcountries.eu/data/gtm.svg", "currency": "Guatemalan quetzal"}, {"name": "Guam", "capital": "Hag\u0413\u0490t\u0413\u00b1a", "languages": ["English", "Chamorro", "Spanish"], "population": 184200, "flag": "https://restcountries.eu/data/gum.svg", "currency": "United States dollar"}, {"name": "Guadeloupe", "capital": "Basse-Terre", "languages": ["French"], "population": 400132, "flag": "https://restcountries.eu/data/glp.svg", "currency": "Euro"}, {"name": "Grenada", "capital": "St. George's", "languages": ["English"], "population": 103328, "flag": "https://restcountries.eu/data/grd.svg", "currency": "East Caribbean dollar"}, {"name": "Greenland", "capital": "Nuuk", "languages": ["Kalaallisut"], "population": 55847, "flag": "https://restcountries.eu/data/grl.svg", "currency": "Danish krone"}, {"name": "Greece", "capital": "Athens", "languages": ["Greek (modern)"], "population": 10858018, "flag": "https://restcountries.eu/data/grc.svg", "currency": "Euro"}, {"name": "Gibraltar", "capital": "Gibraltar", "languages": ["English"], "population": 33140, "flag": "https://restcountries.eu/data/gib.svg", "currency": "Gibraltar pound"}, {"name": "Ghana", "capital": "Accra", "languages": ["English"], "population": 27670174, "flag": "https://restcountries.eu/data/gha.svg", "currency": "Ghanaian cedi"}, {"name": "Germany", "capital": "Berlin", "languages": ["German"], "population": 81770900, "flag": "https://restcountries.eu/data/deu.svg", "currency": "Euro"}, {"name": "Georgia", "capital": "Tbilisi", "languages": ["Georgian"], "population": 3720400, "flag": "https://restcountries.eu/data/geo.svg", "currency": "Georgian Lari"}, {"name": "Gambia", "capital": "Banjul", "languages": ["English"], "population": 1882450, "flag": "https://restcountries.eu/data/gmb.svg", "currency": "Gambian dalasi"}, {"name": "Gabon", "capital": "Libreville", "languages": ["French"], "population": 1802278, "flag": "https://restcountries.eu/data/gab.svg", "currency": "Central African CFA franc"}, {"name": "French Southern Territories", "capital": "Port-aux-Fran\u0413\u00a7ais", "languages": ["French"], "population": 140, "flag": "https://restcountries.eu/data/atf.svg", "currency": "Euro"}, {"name": "French Polynesia", "capital": "Papeet\u0414\u201c", "languages": ["French"], "population": 271800, "flag": "https://restcountries.eu/data/pyf.svg", "currency": "CFP franc"}, {"name": "French Guiana", "capital": "Cayenne", "languages": ["French"], "population": 254541, "flag": "https://restcountries.eu/data/guf.svg", "currency": "Euro"}, {"name": "France", "capital": "Paris", "languages": ["French"], "population": 66710000, "flag": "https://restcountries.eu/data/fra.svg", "currency": "Euro"}, {"name": "Finland", "capital": "Helsinki", "languages": ["Finnish", "Swedish"], "population": 5491817, "flag": "https://restcountries.eu/data/fin.svg", "currency": "Euro"}, {"name": "Fiji", "capital": "Suva", "languages": ["English", "Fijian", "Hindi", "Urdu"], "population": 867000, "flag": "https://restcountries.eu/data/fji.svg", "currency": "Fijian dollar"}, {"name": "Faroe Islands", "capital": "T\u0413\u0456rshavn", "languages": ["Faroese"], "population": 49376, "flag": "https://restcountries.eu/data/fro.svg", "currency": "Danish krone"}, {"name": "Falkland Islands (Malvinas)", "capital": "Stanley", "languages": ["English"], "population": 2563, "flag": "https://restcountries.eu/data/flk.svg", "currency": "Falkland Islands pound"}, {"name": "Ethiopia", "capital": "Addis Ababa", "languages": ["Amharic"], "population": 92206005, "flag": "https://restcountries.eu/data/eth.svg", "currency": "Ethiopian birr"}, {"name": "Estonia", "capital": "Tallinn", "languages": ["Estonian"], "population": 1315944, "flag": "https://restcountries.eu/data/est.svg", "currency": "Euro"}, {"name": "Eritrea", "capital": "Asmara", "languages": ["Tigrinya", "Arabic", "English"], "population": 5352000, "flag": "https://restcountries.eu/data/eri.svg", "currency": "Eritrean nakfa"}, {"name": "Equatorial Guinea", "capital": "Malabo", "languages": ["Spanish", "French"], "population": 1222442, "flag": "https://restcountries.eu/data/gnq.svg", "currency": "Central African CFA franc"}, {"name": "El Salvador", "capital": "San Salvador", "languages": ["Spanish"], "population": 6520675, "flag": "https://restcountries.eu/data/slv.svg", "currency": "United States dollar"}, {"name": "Egypt", "capital": "Cairo", "languages": ["Arabic"], "population": 91290000, "flag": "https://restcountries.eu/data/egy.svg", "currency": "Egyptian pound"}, {"name": "Ecuador", "capital": "Quito", "languages": ["Spanish"], "population": 16545799, "flag": "https://restcountries.eu/data/ecu.svg", "currency": "United States dollar"}, {"name": "Dominican Republic", "capital": "Santo Domingo", "languages": ["Spanish"], "population": 10075045, "flag": "https://restcountries.eu/data/dom.svg", "currency": "Dominican peso"}, {"name": "Dominica", "capital": "Roseau", "languages": ["English"], "population": 71293, "flag": "https://restcountries.eu/data/dma.svg", "currency": "East Caribbean dollar"}, {"name": "Djibouti", "capital": "Djibouti", "languages": ["French", "Arabic"], "population": 900000, "flag": "https://restcountries.eu/data/dji.svg", "currency": "Djiboutian franc"}, {"name": "Denmark", "capital": "Copenhagen", "languages": ["Danish"], "population": 5717014, "flag": "https://restcountries.eu/data/dnk.svg", "currency": "Danish krone"}, {"name": "C\u0413\u0491te d'Ivoire", "capital": "Yamoussoukro", "languages": ["French"], "population": 22671331, "flag": "https://restcountries.eu/data/civ.svg", "currency": "West African CFA franc"}, {"name": "Czech Republic", "capital": "Prague", "languages": ["Czech", "Slovak"], "population": 10558524, "flag": "https://restcountries.eu/data/cze.svg", "currency": "Czech koruna"}, {"name": "Cyprus", "capital": "Nicosia", "languages": ["Greek (modern)", "Turkish", "Armenian"], "population": 847000, "flag": "https://restcountries.eu/data/cyp.svg", "currency": "Euro"}, {"name": "Cura\u0413\u00a7ao", "capital": "Willemstad", "languages": ["Dutch", "(Eastern) Punjabi", "English"], "population": 154843, "flag": "https://restcountries.eu/data/cuw.svg", "currency": "Netherlands Antillean guilder"}, {"name": "Cuba", "capital": "Havana", "languages": ["Spanish"], "population": 11239004, "flag": "https://restcountries.eu/data/cub.svg", "currency": "Cuban convertible peso"}, {"name": "Croatia", "capital": "Zagreb", "languages": ["Croatian"], "population": 4190669, "flag": "https://restcountries.eu/data/hrv.svg", "currency": "Croatian kuna"}, {"name": "Costa Rica", "capital": "San Jos\u0413\u00a9", "languages": ["Spanish"], "population": 4890379, "flag": "https://restcountries.eu/data/cri.svg", "currency": "Costa Rican col\u0413\u0456n"}, {"name": "Cook Islands", "capital": "Avarua", "languages": ["English"], "population": 18100, "flag": "https://restcountries.eu/data/cok.svg", "currency": "New Zealand dollar"}, {"name": "Congo (Democratic Republic of the)", "capital": "Kinshasa", "languages": ["French", "Lingala", "Kongo", "Swahili", "Luba-Katanga"], "population": 85026000, "flag": "https://restcountries.eu/data/cod.svg", "currency": "Congolese franc"}, {"name": "Congo", "capital": "Brazzaville", "languages": ["French", "Lingala"], "population": 4741000, "flag": "https://restcountries.eu/data/cog.svg", "currency": "Central African CFA franc"}, {"name": "Comoros", "capital": "Moroni", "languages": ["Arabic", "French"], "population": 806153, "flag": "https://restcountries.eu/data/com.svg", "currency": "Comorian franc"}, {"name": "Colombia", "capital": "Bogot\u0413\u040e", "languages": ["Spanish"], "population": 48759958, "flag": "https://restcountries.eu/data/col.svg", "currency": "Colombian peso"}, {"name": "Cocos (Keeling) Islands", "capital": "West Island", "languages": ["English"], "population": 550, "flag": "https://restcountries.eu/data/cck.svg", "currency": "Australian dollar"}, {"name": "Christmas Island", "capital": "Flying Fish Cove", "languages": ["English"], "population": 2072, "flag": "https://restcountries.eu/data/cxr.svg", "currency": "Australian dollar"}, {"name": "China", "capital": "Beijing", "languages": ["Chinese"], "population": 1377422166, "flag": "https://restcountries.eu/data/chn.svg", "currency": "Chinese yuan"}, {"name": "Chile", "capital": "Santiago", "languages": ["Spanish"], "population": 18191900, "flag": "https://restcountries.eu/data/chl.svg", "currency": "Chilean peso"}, {"name": "Chad", "capital": "N'Djamena", "languages": ["French", "Arabic"], "population": 14497000, "flag": "https://restcountries.eu/data/tcd.svg", "currency": "Central African CFA franc"}, {"name": "Central African Republic", "capital": "Bangui", "languages": ["French", "Sango"], "population": 4998000, "flag": "https://restcountries.eu/data/caf.svg", "currency": "Central African CFA franc"}, {"name": "Cayman Islands", "capital": "George Town", "languages": ["English"], "population": 58238, "flag": "https://restcountries.eu/data/cym.svg", "currency": "Cayman Islands dollar"}, {"name": "Canada", "capital": "Ottawa", "languages": ["English", "French"], "population": 36155487, "flag": "https://restcountries.eu/data/can.svg", "currency": "Canadian dollar"}, {"name": "Cameroon", "capital": "Yaound\u0413\u00a9", "languages": ["English", "French"], "population": 22709892, "flag": "https://restcountries.eu/data/cmr.svg", "currency": "Central African CFA franc"}, {"name": "Cambodia", "capital": "Phnom Penh", "languages": ["Khmer"], "population": 15626444, "flag": "https://restcountries.eu/data/khm.svg", "currency": "Cambodian riel"}, {"name": "Cabo Verde", "capital": "Praia", "languages": ["Portuguese"], "population": 531239, "flag": "https://restcountries.eu/data/cpv.svg", "currency": "Cape Verdean escudo"}, {"name": "Burundi", "capital": "Bujumbura", "languages": ["French", "Kirundi"], "population": 10114505, "flag": "https://restcountries.eu/data/bdi.svg", "currency": "Burundian franc"}, {"name": "Burkina Faso", "capital": "Ouagadougou", "languages": ["French", "Fula"], "population": 19034397, "flag": "https://restcountries.eu/data/bfa.svg", "currency": "West African CFA franc"}, {"name": "Bulgaria", "capital": "Sofia", "languages": ["Bulgarian"], "population": 7153784, "flag": "https://restcountries.eu/data/bgr.svg", "currency": "Bulgarian lev"}, {"name": "Brunei Darussalam", "capital": "Bandar Seri Begawan", "languages": ["Malay"], "population": 411900, "flag": "https://restcountries.eu/data/brn.svg", "currency": "Brunei dollar"}, {"name": "British Indian Ocean Territory", "capital": "Diego Garcia", "languages": ["English"], "population": 3000, "flag": "https://restcountries.eu/data/iot.svg", "currency": "United States dollar"}, {"name": "Brazil", "capital": "Bras\u0413\u00adlia", "languages": ["Portuguese"], "population": 206135893, "flag": "https://restcountries.eu/data/bra.svg", "currency": "Brazilian real"}, {"name": "Bouvet Island", "capital": "", "languages": ["Norwegian", "Norwegian Bokm\u0413\u0490l", "Norwegian Nynorsk"], "population": 0, "flag": "https://restcountries.eu/data/bvt.svg", "currency": "Norwegian krone"}, {"name": "Botswana", "capital": "Gaborone", "languages": ["English", "Tswana"], "population": 2141206, "flag": "https://restcountries.eu/data/bwa.svg", "currency": "Botswana pula"}, {"name": "Bosnia and Herzegovina", "capital": "Sarajevo", "languages": ["Bosnian", "Croatian", "Serbian"], "population": 3531159, "flag": "https://restcountries.eu/data/bih.svg", "currency": "Bosnia and Herzegovina convertible mark"}, {"name": "Bonaire, Sint Eustatius and Saba", "capital": "Kralendijk", "languages": ["Dutch"], "population": 17408, "flag": "https://restcountries.eu/data/bes.svg", "currency": "United States dollar"}, {"name": "Bolivia (Plurinational State of)", "capital": "Sucre", "languages": ["Spanish", "Aymara", "Quechua"], "population": 10985059, "flag": "https://restcountries.eu/data/bol.svg", "currency": "Bolivian boliviano"}, {"name": "Bhutan", "capital": "Thimphu", "languages": ["Dzongkha"], "population": 775620, "flag": "https://restcountries.eu/data/btn.svg", "currency": "Bhutanese ngultrum"}, {"name": "Bermuda", "capital": "Hamilton", "languages": ["English"], "population": 61954, "flag": "https://restcountries.eu/data/bmu.svg", "currency": "Bermudian dollar"}, {"name": "Benin", "capital": "Porto-Novo", "languages": ["French"], "population": 10653654, "flag": "https://restcountries.eu/data/ben.svg", "currency": "West African CFA franc"}, {"name": "Belize", "capital": "Belmopan", "languages": ["English", "Spanish"], "population": 370300, "flag": "https://restcountries.eu/data/blz.svg", "currency": "Belize dollar"}, {"name": "Belgium", "capital": "Brussels", "languages": ["Dutch", "French", "German"], "population": 11319511, "flag": "https://restcountries.eu/data/bel.svg", "currency": "Euro"}, {"name": "Belarus", "capital": "Minsk", "languages": ["Belarusian", "Russian"], "population": 9498700, "flag": "https://restcountries.eu/data/blr.svg", "currency": "New Belarusian ruble"}, {"name": "Barbados", "capital": "Bridgetown", "languages": ["English"], "population": 285000, "flag": "https://restcountries.eu/data/brb.svg", "currency": "Barbadian dollar"}, {"name": "Bangladesh", "capital": "Dhaka", "languages": ["Bengali"], "population": 161006790, "flag": "https://restcountries.eu/data/bgd.svg", "currency": "Bangladeshi taka"}, {"name": "Bahrain", "capital": "Manama", "languages": ["Arabic"], "population": 1404900, "flag": "https://restcountries.eu/data/bhr.svg", "currency": "Bahraini dinar"}, {"name": "Bahamas", "capital": "Nassau", "languages": ["English"], "population": 378040, "flag": "https://restcountries.eu/data/bhs.svg", "currency": "Bahamian dollar"}, {"name": "Azerbaijan", "capital": "Baku", "languages": ["Azerbaijani"], "population": 9730500, "flag": "https://restcountries.eu/data/aze.svg", "currency": "Azerbaijani manat"}, {"name": "Austria", "capital": "Vienna", "languages": ["German"], "population": 8725931, "flag": "https://restcountries.eu/data/aut.svg", "currency": "Euro"}, {"name": "Australia", "capital": "Canberra", "languages": ["English"], "population": 24117360, "flag": "https://restcountries.eu/data/aus.svg", "currency": "Australian dollar"}, {"name": "Aruba", "capital": "Oranjestad", "languages": ["Dutch", "(Eastern) Punjabi"], "population": 107394, "flag": "https://restcountries.eu/data/abw.svg", "currency": "Aruban florin"}, {"name": "Armenia", "capital": "Yerevan", "languages": ["Armenian", "Russian"], "population": 2994400, "flag": "https://restcountries.eu/data/arm.svg", "currency": "Armenian dram"}, {"name": "Argentina", "capital": "Buenos Aires", "languages": ["Spanish", "Guaran\u0413\u00ad"], "population": 43590400, "flag": "https://restcountries.eu/data/arg.svg", "currency": "Argentine peso"}, {"name": "Antigua and Barbuda", "capital": "Saint John's", "languages": ["English"], "population": 86295, "flag": "https://restcountries.eu/data/atg.svg", "currency": "East Caribbean dollar"}, {"name": "Antarctica", "capital": "", "languages": ["English", "Russian"], "population": 1000, "flag": "https://restcountries.eu/data/ata.svg", "currency": "Australian dollar"}, {"name": "Anguilla", "capital": "The Valley", "languages": ["English"], "population": 13452, "flag": "https://restcountries.eu/data/aia.svg", "currency": "East Caribbean dollar"}, {"name": "Angola", "capital": "Luanda", "languages": ["Portuguese"], "population": 25868000, "flag": "https://restcountries.eu/data/ago.svg", "currency": "Angolan kwanza"}, {"name": "Andorra", "capital": "Andorra la Vella", "languages": ["Catalan"], "population": 78014, "flag": "https://restcountries.eu/data/and.svg", "currency": "Euro"}, {"name": "American Samoa", "capital": "Pago Pago", "languages": ["English", "Samoan"], "population": 57100, "flag": "https://restcountries.eu/data/asm.svg", "currency": "United State Dollar"}, {"name": "Algeria", "capital": "Algiers", "languages": ["Arabic"], "population": 40400000, "flag": "https://restcountries.eu/data/dza.svg", "currency": "Algerian dinar"}, {"name": "Albania", "capital": "Tirana", "languages": ["Albanian"], "population": 2886026, "flag": "https://restcountries.eu/data/alb.svg", "currency": "Albanian lek"}, {"name": "Afghanistan", "capital": "Kabul", "languages": ["Pashto", "Uzbek", "Turkmen"], "population": 27657145, "flag": "https://restcountries.eu/data/afg.svg", "currency": "Afghan afghani"}]
'''
import json
with open ('countries-data.json','r') as file:
    countries_data=json.load(file)    
countries_data.sort(key=lambda x:x.get('capital'))#сортировка стран по столице
with open('countries_data_sort2.json','w') as file:
    json.dump(countries_data,file)
'''
[out]:	
[{"name": "Antarctica", "capital": "", "languages": ["English", "Russian"], "population": 1000, "flag": "https://restcountries.eu/data/ata.svg", "currency": "Australian dollar"}, {"name": "Bouvet Island", "capital": "", "languages": ["Norwegian", "Norwegian Bokm\u0413\u0490l", "Norwegian Nynorsk"], "population": 0, "flag": "https://restcountries.eu/data/bvt.svg", "currency": "Norwegian krone"}, {"name": "United States Minor Outlying Islands", "capital": "", "languages": ["English"], "population": 300, "flag": "https://restcountries.eu/data/umi.svg", "currency": "United States Dollar"}, {"name": "Heard Island and McDonald Islands", "capital": "", "languages": ["English"], "population": 0, "flag": "https://restcountries.eu/data/hmd.svg", "currency": "Australian dollar"}, {"name": "Macao", "capital": "", "languages": ["Chinese", "Portuguese"], "population": 649100, "flag": "https://restcountries.eu/data/mac.svg", "currency": "Macanese pataca"}, {"name": "United Arab Emirates", "capital": "Abu Dhabi", "languages": ["Arabic"], "population": 9856000, "flag": "https://restcountries.eu/data/are.svg", "currency": "United Arab Emirates dirham"}, {"name": "Nigeria", "capital": "Abuja", "languages": ["English"], "population": 186988000, "flag": "https://restcountries.eu/data/nga.svg", "currency": "Nigerian naira"}, {"name": "Ghana", "capital": "Accra", "languages": ["English"], "population": 27670174, "flag": "https://restcountries.eu/data/gha.svg", "currency": "Ghanaian cedi"}, {"name": "Pitcairn", "capital": "Adamstown", "languages": ["English"], "population": 56, "flag": "https://restcountries.eu/data/pcn.svg", "currency": "New Zealand dollar"}, {"name": "Ethiopia", "capital": "Addis Ababa", "languages": ["Amharic"], "population": 92206005, "flag": "https://restcountries.eu/data/eth.svg", "currency": "Ethiopian birr"}, {"name": "Algeria", "capital": "Algiers", "languages": ["Arabic"], "population": 40400000, "flag": "https://restcountries.eu/data/dza.svg", "currency": "Algerian dinar"}, {"name": "Niue", "capital": "Alofi", "languages": ["English"], "population": 1470, "flag": "https://restcountries.eu/data/niu.svg", "currency": "New Zealand dollar"}, {"name": "Jordan", "capital": "Amman", "languages": ["Arabic"], "population": 9531712, "flag": "https://restcountries.eu/data/jor.svg", "currency": "Jordanian dinar"}, {"name": "Netherlands", "capital": "Amsterdam", "languages": ["Dutch"], "population": 17019800, "flag": "https://restcountries.eu/data/nld.svg", "currency": "Euro"}, {"name": "Andorra", "capital": "Andorra la Vella", "languages": ["Catalan"], "population": 78014, "flag": "https://restcountries.eu/data/and.svg", "currency": "Euro"}, {"name": "Turkey", "capital": "Ankara", "languages": ["Turkish"], "population": 78741053, "flag": "https://restcountries.eu/data/tur.svg", "currency": "Turkish lira"}, {"name": "Madagascar", "capital": "Antananarivo", "languages": ["French", "Malagasy"], "population": 22434363, "flag": "https://restcountries.eu/data/mdg.svg", "currency": "Malagasy ariary"}, {"name": "Samoa", "capital": "Apia", "languages": ["Samoan", "English"], "population": 194899, "flag": "https://restcountries.eu/data/wsm.svg", "currency": "Samoan t\u0414\u0403l\u0414\u0403"}, {"name": "Turkmenistan", "capital": "Ashgabat", "languages": ["Turkmen", "Russian"], "population": 4751120, "flag": "https://restcountries.eu/data/tkm.svg", "currency": "Turkmenistan manat"}, {"name": "Eritrea", "capital": "Asmara", "languages": ["Tigrinya", "Arabic", "English"], "population": 5352000, "flag": "https://restcountries.eu/data/eri.svg", "currency": "Eritrean nakfa"}, {"name": "Kazakhstan", "capital": "Astana", "languages": ["Kazakh", "Russian"], "population": 17753200, "flag": "https://restcountries.eu/data/kaz.svg", "currency": "Kazakhstani tenge"}, {"name": "Paraguay", "capital": "Asunci\u0413\u0456n", "languages": ["Spanish", "Guaran\u0413\u00ad"], "population": 6854536, "flag": "https://restcountries.eu/data/pry.svg", "currency": "Paraguayan guaran\u0413\u00ad"}, {"name": "Greece", "capital": "Athens", "languages": ["Greek (modern)"], "population": 10858018, "flag": "https://restcountries.eu/data/grc.svg", "currency": "Euro"}, {"name": "Cook Islands", "capital": "Avarua", "languages": ["English"], "population": 18100, "flag": "https://restcountries.eu/data/cok.svg", "currency": "New Zealand dollar"}, {"name": "Iraq", "capital": "Baghdad", "languages": ["Arabic", "Kurdish"], "population": 37883543, "flag": "https://restcountries.eu/data/irq.svg", "currency": "Iraqi dinar"}, {"name": "Azerbaijan", "capital": "Baku", "languages": ["Azerbaijani"], "population": 9730500, "flag": "https://restcountries.eu/data/aze.svg", "currency": "Azerbaijani manat"}, {"name": "Mali", "capital": "Bamako", "languages": ["French"], "population": 18135000, "flag": "https://restcountries.eu/data/mli.svg", "currency": "West African CFA franc"}, {"name": "Brunei Darussalam", "capital": "Bandar Seri Begawan", "languages": ["Malay"], "population": 411900, "flag": "https://restcountries.eu/data/brn.svg", "currency": "Brunei dollar"}, {"name": "Thailand", "capital": "Bangkok", "languages": ["Thai"], "population": 65327652, "flag": "https://restcountries.eu/data/tha.svg", "currency": "Thai baht"}, {"name": "Central African Republic", "capital": "Bangui", "languages": ["French", "Sango"], "population": 4998000, "flag": "https://restcountries.eu/data/caf.svg", "currency": "Central African CFA franc"}, {"name": "Gambia", "capital": "Banjul", "languages": ["English"], "population": 1882450, "flag": "https://restcountries.eu/data/gmb.svg", "currency": "Gambian dalasi"}, {"name": "Guadeloupe", "capital": "Basse-Terre", "languages": ["French"], "population": 400132, "flag": "https://restcountries.eu/data/glp.svg", "currency": "Euro"}, {"name": "Saint Kitts and Nevis", "capital": "Basseterre", "languages": ["English"], "population": 46204, "flag": "https://restcountries.eu/data/kna.svg", "currency": "East Caribbean dollar"}, {"name": "China", "capital": "Beijing", "languages": ["Chinese"], "population": 1377422166, "flag": "https://restcountries.eu/data/chn.svg", "currency": "Chinese yuan"}, {"name": "Lebanon", "capital": "Beirut", "languages": ["Arabic", "French"], "population": 5988000, "flag": "https://restcountries.eu/data/lbn.svg", "currency": "Lebanese pound"}, {"name": "Serbia", "capital": "Belgrade", "languages": ["Serbian"], "population": 7076372, "flag": "https://restcountries.eu/data/srb.svg", "currency": "Serbian dinar"}, {"name": "Belize", "capital": "Belmopan", "languages": ["English", "Spanish"], "population": 370300, "flag": "https://restcountries.eu/data/blz.svg", "currency": "Belize dollar"}, {"name": "Germany", "capital": "Berlin", "languages": ["German"], "population": 81770900, "flag": "https://restcountries.eu/data/deu.svg", "currency": "Euro"}, {"name": "Switzerland", "capital": "Bern", "languages": ["German", "French", "Italian"], "population": 8341600, "flag": "https://restcountries.eu/data/che.svg", "currency": "Swiss franc"}, {"name": "Kyrgyzstan", "capital": "Bishkek", "languages": ["Kyrgyz", "Russian"], "population": 6047800, "flag": "https://restcountries.eu/data/kgz.svg", "currency": "Kyrgyzstani som"}, {"name": "Guinea-Bissau", "capital": "Bissau", "languages": ["Portuguese"], "population": 1547777, "flag": "https://restcountries.eu/data/gnb.svg", "currency": "West African CFA franc"}, {"name": "Colombia", "capital": "Bogot\u0413\u040e", "languages": ["Spanish"], "population": 48759958, "flag": "https://restcountries.eu/data/col.svg", "currency": "Colombian peso"}, {"name": "Brazil", "capital": "Bras\u0413\u00adlia", "languages": ["Portuguese"], "population": 206135893, "flag": "https://restcountries.eu/data/bra.svg", "currency": "Brazilian real"}, {"name": "Slovakia", "capital": "Bratislava", "languages": ["Slovak"], "population": 5426252, "flag": "https://restcountries.eu/data/svk.svg", "currency": "Euro"}, {"name": "Congo", "capital": "Brazzaville", "languages": ["French", "Lingala"], "population": 4741000, "flag": "https://restcountries.eu/data/cog.svg", "currency": "Central African CFA franc"}, {"name": "Barbados", "capital": "Bridgetown", "languages": ["English"], "population": 285000, "flag": "https://restcountries.eu/data/brb.svg", "currency": "Barbadian dollar"}, {"name": "Belgium", "capital": "Brussels", "languages": ["Dutch", "French", "German"], "population": 11319511, "flag": "https://restcountries.eu/data/bel.svg", "currency": "Euro"}, {"name": "Romania", "capital": "Bucharest", "languages": ["Romanian"], "population": 19861408, "flag": "https://restcountries.eu/data/rou.svg", "currency": "Romanian leu"}, {"name": "Hungary", "capital": "Budapest", "languages": ["Hungarian"], "population": 9823000, "flag": "https://restcountries.eu/data/hun.svg", "currency": "Hungarian forint"}, {"name": "Argentina", "capital": "Buenos Aires", "languages": ["Spanish", "Guaran\u0413\u00ad"], "population": 43590400, "flag": "https://restcountries.eu/data/arg.svg", "currency": "Argentine peso"}, {"name": "Burundi", "capital": "Bujumbura", "languages": ["French", "Kirundi"], "population": 10114505, "flag": "https://restcountries.eu/data/bdi.svg", "currency": "Burundian franc"}, {"name": "Egypt", "capital": "Cairo", "languages": ["Arabic"], "population": 91290000, "flag": "https://restcountries.eu/data/egy.svg", "currency": "Egyptian pound"}, {"name": "Australia", "capital": "Canberra", "languages": ["English"], "population": 24117360, "flag": "https://restcountries.eu/data/aus.svg", "currency": "Australian dollar"}, {"name": "Venezuela (Bolivarian Republic of)", "capital": "Caracas", "languages": ["Spanish"], "population": 31028700, "flag": "https://restcountries.eu/data/ven.svg", "currency": "Venezuelan bol\u0413\u00advar"}, {"name": "Saint Lucia", "capital": "Castries", "languages": ["English"], "population": 186000, "flag": "https://restcountries.eu/data/lca.svg", "currency": "East Caribbean dollar"}, {"name": "French Guiana", "capital": "Cayenne", "languages": ["French"], "population": 254541, "flag": "https://restcountries.eu/data/guf.svg", "currency": "Euro"}, {"name": "Virgin Islands (U.S.)", "capital": "Charlotte Amalie", "languages": ["English"], "population": 114743, "flag": "https://restcountries.eu/data/vir.svg", "currency": "United States dollar"}, {"name": "Moldova (Republic of)", "capital": "Chi\u0418\u2122in\u0414\u0453u", "languages": ["Romanian"], "population": 3553100, "flag": "https://restcountries.eu/data/mda.svg", "currency": "Moldovan leu"}, {"name": "San Marino", "capital": "City of San Marino", "languages": ["Italian"], "population": 33005, "flag": "https://restcountries.eu/data/smr.svg", "currency": "Euro"}, {"name": "Hong Kong", "capital": "City of Victoria", "languages": ["English", "Chinese"], "population": 7324300, "flag": "https://restcountries.eu/data/hkg.svg", "currency": "Hong Kong dollar"}, {"name": "Turks and Caicos Islands", "capital": "Cockburn Town", "languages": ["English"], "population": 31458, "flag": "https://restcountries.eu/data/tca.svg", "currency": "United States dollar"}, {"name": "Sri Lanka", "capital": "Colombo", "languages": ["Sinhalese", "Tamil"], "population": 20966000, "flag": "https://restcountries.eu/data/lka.svg", "currency": "Sri Lankan rupee"}, {"name": "Guinea", "capital": "Conakry", "languages": ["French", "Fula"], "population": 12947000, "flag": "https://restcountries.eu/data/gin.svg", "currency": "Guinean franc"}, {"name": "Denmark", "capital": "Copenhagen", "languages": ["Danish"], "population": 5717014, "flag": "https://restcountries.eu/data/dnk.svg", "currency": "Danish krone"}, {"name": "Senegal", "capital": "Dakar", "languages": ["French"], "population": 14799859, "flag": "https://restcountries.eu/data/sen.svg", "currency": "West African CFA franc"}, {"name": "Syrian Arab Republic", "capital": "Damascus", "languages": ["Arabic"], "population": 18564000, "flag": "https://restcountries.eu/data/syr.svg", "currency": "Syrian pound"}, {"name": "Bangladesh", "capital": "Dhaka", "languages": ["Bengali"], "population": 161006790, "flag": "https://restcountries.eu/data/bgd.svg", "currency": "Bangladeshi taka"}, {"name": "British Indian Ocean Territory", "capital": "Diego Garcia", "languages": ["English"], "population": 3000, "flag": "https://restcountries.eu/data/iot.svg", "currency": "United States dollar"}, {"name": "Timor-Leste", "capital": "Dili", "languages": ["Portuguese"], "population": 1167242, "flag": "https://restcountries.eu/data/tls.svg", "currency": "United States dollar"}, {"name": "Djibouti", "capital": "Djibouti", "languages": ["French", "Arabic"], "population": 900000, "flag": "https://restcountries.eu/data/dji.svg", "currency": "Djiboutian franc"}, {"name": "Tanzania, United Republic of", "capital": "Dodoma", "languages": ["Swahili", "English"], "population": 55155000, "flag": "https://restcountries.eu/data/tza.svg", "currency": "Tanzanian shilling"}, {"name": "Qatar", "capital": "Doha", "languages": ["Arabic"], "population": 2587564, "flag": "https://restcountries.eu/data/qat.svg", "currency": "Qatari riyal"}, {"name": "Isle of Man", "capital": "Douglas", "languages": ["English", "Manx"], "population": 84497, "flag": "https://restcountries.eu/data/imn.svg", "currency": "British pound"}, {"name": "Ireland", "capital": "Dublin", "languages": ["Irish", "English"], "population": 6378000, "flag": "https://restcountries.eu/data/irl.svg", "currency": "Euro"}, {"name": "Tajikistan", "capital": "Dushanbe", "languages": ["Tajik", "Russian"], "population": 8593600, "flag": "https://restcountries.eu/data/tjk.svg", "currency": "Tajikistani somoni"}, {"name": "Western Sahara", "capital": "El Aai\u0413\u0454n", "languages": ["Spanish"], "population": 510713, "flag": "https://restcountries.eu/data/esh.svg", "currency": "Moroccan dirham"}, {"name": "Tokelau", "capital": "Fakaofo", "languages": ["English"], "population": 1411, "flag": "https://restcountries.eu/data/tkl.svg", "currency": "New Zealand dollar"}, {"name": "Christmas Island", "capital": "Flying Fish Cove", "languages": ["English"], "population": 2072, "flag": "https://restcountries.eu/data/cxr.svg", "currency": "Australian dollar"}, {"name": "Martinique", "capital": "Fort-de-France", "languages": ["French"], "population": 378243, "flag": "https://restcountries.eu/data/mtq.svg", "currency": "Euro"}, {"name": "Sierra Leone", "capital": "Freetown", "languages": ["English"], "population": 7075641, "flag": "https://restcountries.eu/data/sle.svg", "currency": "Sierra Leonean leone"}, {"name": "Tuvalu", "capital": "Funafuti", "languages": ["English"], "population": 10640, "flag": "https://restcountries.eu/data/tuv.svg", "currency": "Australian dollar"}, {"name": "Botswana", "capital": "Gaborone", "languages": ["English", "Tswana"], "population": 2141206, "flag": "https://restcountries.eu/data/bwa.svg", "currency": "Botswana pula"}, {"name": "Cayman Islands", "capital": "George Town", "languages": ["English"], "population": 58238, "flag": "https://restcountries.eu/data/cym.svg", "currency": "Cayman Islands dollar"}, {"name": "Guyana", "capital": "Georgetown", "languages": ["English"], "population": 746900, "flag": "https://restcountries.eu/data/guy.svg", "currency": "Guyanese dollar"}, {"name": "Gibraltar", "capital": "Gibraltar", "languages": ["English"], "population": 33140, "flag": "https://restcountries.eu/data/gib.svg", "currency": "Gibraltar pound"}, {"name": "Guatemala", "capital": "Guatemala City", "languages": ["Spanish"], "population": 16176133, "flag": "https://restcountries.eu/data/gtm.svg", "currency": "Guatemalan quetzal"}, {"name": "Saint Barth\u0413\u00a9lemy", "capital": "Gustavia", "languages": ["French"], "population": 9417, "flag": "https://restcountries.eu/data/blm.svg", "currency": "Euro"}, {"name": "Guam", "capital": "Hag\u0413\u0490t\u0413\u00b1a", "languages": ["English", "Chamorro", "Spanish"], "population": 184200, "flag": "https://restcountries.eu/data/gum.svg", "currency": "United States dollar"}, {"name": "Bermuda", "capital": "Hamilton", "languages": ["English"], "population": 61954, "flag": "https://restcountries.eu/data/bmu.svg", "currency": "Bermudian dollar"}, {"name": "Viet Nam", "capital": "Hanoi", "languages": ["Vietnamese"], "population": 92700000, "flag": "https://restcountries.eu/data/vnm.svg", "currency": "Vietnamese \u0414\u2018\u0431\u00bb\u201cng"}, {"name": "Zimbabwe", "capital": "Harare", "languages": ["English", "Shona", "Northern Ndebele"], "population": 14240168, "flag": "https://restcountries.eu/data/zwe.svg", "currency": "Botswana pula"}, {"name": "Cuba", "capital": "Havana", "languages": ["Spanish"], "population": 11239004, "flag": "https://restcountries.eu/data/cub.svg", "currency": "Cuban convertible peso"}, {"name": "Finland", "capital": "Helsinki", "languages": ["Finnish", "Swedish"], "population": 5491817, "flag": "https://restcountries.eu/data/fin.svg", "currency": "Euro"}, {"name": "Solomon Islands", "capital": "Honiara", "languages": ["English"], "population": 642000, "flag": "https://restcountries.eu/data/slb.svg", "currency": "Solomon Islands dollar"}, {"name": "Pakistan", "capital": "Islamabad", "languages": ["English", "Urdu"], "population": 194125062, "flag": "https://restcountries.eu/data/pak.svg", "currency": "Pakistani rupee"}, {"name": "Indonesia", "capital": "Jakarta", "languages": ["Indonesian"], "population": 258705000, "flag": "https://restcountries.eu/data/idn.svg", "currency": "Indonesian rupiah"}, {"name": "Saint Helena, Ascension and Tristan da Cunha", "capital": "Jamestown", "languages": ["English"], "population": 4255, "flag": "https://restcountries.eu/data/shn.svg", "currency": "Saint Helena pound"}, {"name": "Israel", "capital": "Jerusalem", "languages": ["Hebrew (modern)", "Arabic"], "population": 8527400, "flag": "https://restcountries.eu/data/isr.svg", "currency": "Israeli new shekel"}, {"name": "South Sudan", "capital": "Juba", "languages": ["English"], "population": 12131000, "flag": "https://restcountries.eu/data/ssd.svg", "currency": "South Sudanese pound"}, {"name": "Afghanistan", "capital": "Kabul", "languages": ["Pashto", "Uzbek", "Turkmen"], "population": 27657145, "flag": "https://restcountries.eu/data/afg.svg", "currency": "Afghan afghani"}, {"name": "Uganda", "capital": "Kampala", "languages": ["English", "Swahili"], "population": 33860700, "flag": "https://restcountries.eu/data/uga.svg", "currency": "Ugandan shilling"}, {"name": "Nepal", "capital": "Kathmandu", "languages": ["Nepali"], "population": 28431500, "flag": "https://restcountries.eu/data/npl.svg", "currency": "Nepalese rupee"}, {"name": "Sudan", "capital": "Khartoum", "languages": ["Arabic", "English"], "population": 39598700, "flag": "https://restcountries.eu/data/sdn.svg", "currency": "Sudanese pound"}, {"name": "Ukraine", "capital": "Kiev", "languages": ["Ukrainian"], "population": 42692393, "flag": "https://restcountries.eu/data/ukr.svg", "currency": "Ukrainian hryvnia"}, {"name": "Rwanda", "capital": "Kigali", "languages": ["Kinyarwanda", "English", "French"], "population": 11553188, "flag": "https://restcountries.eu/data/rwa.svg", "currency": "Rwandan franc"}, {"name": "South Georgia and the South Sandwich Islands", "capital": "King Edward Point", "languages": ["English"], "population": 30, "flag": "https://restcountries.eu/data/sgs.svg", "currency": "British pound"}, {"name": "Jamaica", "capital": "Kingston", "languages": ["English"], "population": 2723246, "flag": "https://restcountries.eu/data/jam.svg", "currency": "Jamaican dollar"}, {"name": "Norfolk Island", "capital": "Kingston", "languages": ["English"], "population": 2302, "flag": "https://restcountries.eu/data/nfk.svg", "currency": "Australian dollar"}, {"name": "Saint Vincent and the Grenadines", "capital": "Kingstown", "languages": ["English"], "population": 109991, "flag": "https://restcountries.eu/data/vct.svg", "currency": "East Caribbean dollar"}, {"name": "Congo (Democratic Republic of the)", "capital": "Kinshasa", "languages": ["French", "Lingala", "Kongo", "Swahili", "Luba-Katanga"], "population": 85026000, "flag": "https://restcountries.eu/data/cod.svg", "currency": "Congolese franc"}, {"name": "Bonaire, Sint Eustatius and Saba", "capital": "Kralendijk", "languages": ["Dutch"], "population": 17408, "flag": "https://restcountries.eu/data/bes.svg", "currency": "United States dollar"}, {"name": "Malaysia", "capital": "Kuala Lumpur", "languages": ["Malaysian"], "population": 31405416, "flag": "https://restcountries.eu/data/mys.svg", "currency": "Malaysian ringgit"}, {"name": "Kuwait", "capital": "Kuwait City", "languages": ["Arabic"], "population": 4183658, "flag": "https://restcountries.eu/data/kwt.svg", "currency": "Kuwaiti dinar"}, {"name": "Gabon", "capital": "Libreville", "languages": ["French"], "population": 1802278, "flag": "https://restcountries.eu/data/gab.svg", "currency": "Central African CFA franc"}, {"name": "Malawi", "capital": "Lilongwe", "languages": ["English", "Chichewa"], "population": 16832910, "flag": "https://restcountries.eu/data/mwi.svg", "currency": "Malawian kwacha"}, {"name": "Peru", "capital": "Lima", "languages": ["Spanish"], "population": 31488700, "flag": "https://restcountries.eu/data/per.svg", "currency": "Peruvian sol"}, {"name": "Portugal", "capital": "Lisbon", "languages": ["Portuguese"], "population": 10374822, "flag": "https://restcountries.eu/data/prt.svg", "currency": "Euro"}, {"name": "Slovenia", "capital": "Ljubljana", "languages": ["Slovene"], "population": 2064188, "flag": "https://restcountries.eu/data/svn.svg", "currency": "Euro"}, {"name": "Swaziland", "capital": "Lobamba", "languages": ["English", "Swati"], "population": 1132657, "flag": "https://restcountries.eu/data/swz.svg", "currency": "Swazi lilangeni"}, {"name": "Togo", "capital": "Lom\u0413\u00a9", "languages": ["French"], "population": 7143000, "flag": "https://restcountries.eu/data/tgo.svg", "currency": "West African CFA franc"}, {"name": "United Kingdom of Great Britain and Northern Ireland", "capital": "London", "languages": ["English"], "population": 65110000, "flag": "https://restcountries.eu/data/gbr.svg", "currency": "British pound"}, {"name": "Svalbard and Jan Mayen", "capital": "Longyearbyen", "languages": ["Norwegian"], "population": 2562, "flag": "https://restcountries.eu/data/sjm.svg", "currency": "Norwegian krone"}, {"name": "Angola", "capital": "Luanda", "languages": ["Portuguese"], "population": 25868000, "flag": "https://restcountries.eu/data/ago.svg", "currency": "Angolan kwanza"}, {"name": "Zambia", "capital": "Lusaka", "languages": ["English"], "population": 15933883, "flag": "https://restcountries.eu/data/zmb.svg", "currency": "Zambian kwacha"}, {"name": "Luxembourg", "capital": "Luxembourg", "languages": ["French", "German", "Luxembourgish"], "population": 576200, "flag": "https://restcountries.eu/data/lux.svg", "currency": "Euro"}, {"name": "Spain", "capital": "Madrid", "languages": ["Spanish"], "population": 46438422, "flag": "https://restcountries.eu/data/esp.svg", "currency": "Euro"}, {"name": "Marshall Islands", "capital": "Majuro", "languages": ["English", "Marshallese"], "population": 54880, "flag": "https://restcountries.eu/data/mhl.svg", "currency": "United States dollar"}, {"name": "Equatorial Guinea", "capital": "Malabo", "languages": ["Spanish", "French"], "population": 1222442, "flag": "https://restcountries.eu/data/gnq.svg", "currency": "Central African CFA franc"}, {"name": "Maldives", "capital": "Mal\u0413\u00a9", "languages": ["Divehi"], "population": 344023, "flag": "https://restcountries.eu/data/mdv.svg", "currency": "Maldivian rufiyaa"}, {"name": "Mayotte", "capital": "Mamoudzou", "languages": ["French"], "population": 226915, "flag": "https://restcountries.eu/data/myt.svg", "currency": "Euro"}, {"name": "Nicaragua", "capital": "Managua", "languages": ["Spanish"], "population": 6262703, "flag": "https://restcountries.eu/data/nic.svg", "currency": "Nicaraguan c\u0413\u0456rdoba"}, {"name": "Bahrain", "capital": "Manama", "languages": ["Arabic"], "population": 1404900, "flag": "https://restcountries.eu/data/bhr.svg", "currency": "Bahraini dinar"}, {"name": "Philippines", "capital": "Manila", "languages": ["English"], "population": 103279800, "flag": "https://restcountries.eu/data/phl.svg", "currency": "Philippine peso"}, {"name": "Mozambique", "capital": "Maputo", "languages": ["Portuguese"], "population": 26423700, "flag": "https://restcountries.eu/data/moz.svg", "currency": "Mozambican metical"}, {"name": "\u0413\u2026land Islands", "capital": "Mariehamn", "languages": ["Swedish"], "population": 28875, "flag": "https://restcountries.eu/data/ala.svg", "currency": "Euro"}, {"name": "Saint Martin (French part)", "capital": "Marigot", "languages": ["English", "French", "Dutch"], "population": 36979, "flag": "https://restcountries.eu/data/maf.svg", "currency": "Euro"}, {"name": "Lesotho", "capital": "Maseru", "languages": ["English", "Southern Sotho"], "population": 1894194, "flag": "https://restcountries.eu/data/lso.svg", "currency": "Lesotho loti"}, {"name": "Wallis and Futuna", "capital": "Mata-Utu", "languages": ["French"], "population": 11750, "flag": "https://restcountries.eu/data/wlf.svg", "currency": "CFP franc"}, {"name": "Mexico", "capital": "Mexico City", "languages": ["Spanish"], "population": 122273473, "flag": "https://restcountries.eu/data/mex.svg", "currency": "Mexican peso"}, {"name": "Belarus", "capital": "Minsk", "languages": ["Belarusian", "Russian"], "population": 9498700, "flag": "https://restcountries.eu/data/blr.svg", "currency": "New Belarusian ruble"}, {"name": "Somalia", "capital": "Mogadishu", "languages": ["Somali", "Arabic"], "population": 11079000, "flag": "https://restcountries.eu/data/som.svg", "currency": "Somali shilling"}, {"name": "Monaco", "capital": "Monaco", "languages": ["French"], "population": 38400, "flag": "https://restcountries.eu/data/mco.svg", "currency": "Euro"}, {"name": "Liberia", "capital": "Monrovia", "languages": ["English"], "population": 4615000, "flag": "https://restcountries.eu/data/lbr.svg", "currency": "Liberian dollar"}, {"name": "Uruguay", "capital": "Montevideo", "languages": ["Spanish"], "population": 3480222, "flag": "https://restcountries.eu/data/ury.svg", "currency": "Uruguayan peso"}, {"name": "Comoros", "capital": "Moroni", "languages": ["Arabic", "French"], "population": 806153, "flag": "https://restcountries.eu/data/com.svg", "currency": "Comorian franc"}, {"name": "Russian Federation", "capital": "Moscow", "languages": ["Russian"], "population": 146599183, "flag": "https://restcountries.eu/data/rus.svg", "currency": "Russian ruble"}, {"name": "Oman", "capital": "Muscat", "languages": ["Arabic"], "population": 4420133, "flag": "https://restcountries.eu/data/omn.svg", "currency": "Omani rial"}, {"name": "Chad", "capital": "N'Djamena", "languages": ["French", "Arabic"], "population": 14497000, "flag": "https://restcountries.eu/data/tcd.svg", "currency": "Central African CFA franc"}, {"name": "Kenya", "capital": "Nairobi", "languages": ["English", "Swahili"], "population": 47251000, "flag": "https://restcountries.eu/data/ken.svg", "currency": "Kenyan shilling"}, {"name": "Bahamas", "capital": "Nassau", "languages": ["English"], "population": 378040, "flag": "https://restcountries.eu/data/bhs.svg", "currency": "Bahamian dollar"}, {"name": "Myanmar", "capital": "Naypyidaw", "languages": ["Burmese"], "population": 51419420, "flag": "https://restcountries.eu/data/mmr.svg", "currency": "Burmese kyat"}, {"name": "India", "capital": "New Delhi", "languages": ["Hindi", "English"], "population": 1295210000, "flag": "https://restcountries.eu/data/ind.svg", "currency": "Indian rupee"}, {"name": "Palau", "capital": "Ngerulmud", "languages": ["English"], "population": 17950, "flag": "https://restcountries.eu/data/plw.svg", "currency": "[E]"}, {"name": "Niger", "capital": "Niamey", "languages": ["French"], "population": 20715000, "flag": "https://restcountries.eu/data/ner.svg", "currency": "West African CFA franc"}, {"name": "Cyprus", "capital": "Nicosia", "languages": ["Greek (modern)", "Turkish", "Armenian"], "population": 847000, "flag": "https://restcountries.eu/data/cyp.svg", "currency": "Euro"}, {"name": "Mauritania", "capital": "Nouakchott", "languages": ["Arabic"], "population": 3718678, "flag": "https://restcountries.eu/data/mrt.svg", "currency": "Mauritanian ouguiya"}, {"name": "New Caledonia", "capital": "Noum\u0413\u00a9a", "languages": ["French"], "population": 268767, "flag": "https://restcountries.eu/data/ncl.svg", "currency": "CFP franc"}, {"name": "Tonga", "capital": "Nuku'alofa", "languages": ["English", "Tonga (Tonga Islands)"], "population": 103252, "flag": "https://restcountries.eu/data/ton.svg", "currency": "Tongan pa\u041a\u00bbanga"}, {"name": "Greenland", "capital": "Nuuk", "languages": ["Kalaallisut"], "population": 55847, "flag": "https://restcountries.eu/data/grl.svg", "currency": "Danish krone"}, {"name": "Aruba", "capital": "Oranjestad", "languages": ["Dutch", "(Eastern) Punjabi"], "population": 107394, "flag": "https://restcountries.eu/data/abw.svg", "currency": "Aruban florin"}, {"name": "Norway", "capital": "Oslo", "languages": ["Norwegian", "Norwegian Bokm\u0413\u0490l", "Norwegian Nynorsk"], "population": 5223256, "flag": "https://restcountries.eu/data/nor.svg", "currency": "Norwegian krone"}, {"name": "Canada", "capital": "Ottawa", "languages": ["English", "French"], "population": 36155487, "flag": "https://restcountries.eu/data/can.svg", "currency": "Canadian dollar"}, {"name": "Burkina Faso", "capital": "Ouagadougou", "languages": ["French", "Fula"], "population": 19034397, "flag": "https://restcountries.eu/data/bfa.svg", "currency": "West African CFA franc"}, {"name": "American Samoa", "capital": "Pago Pago", "languages": ["English", "Samoan"], "population": 57100, "flag": "https://restcountries.eu/data/asm.svg", "currency": "United State Dollar"}, {"name": "Micronesia (Federated States of)", "capital": "Palikir", "languages": ["English"], "population": 102800, "flag": "https://restcountries.eu/data/fsm.svg", "currency": "[D]"}, {"name": "Panama", "capital": "Panama City", "languages": ["Spanish"], "population": 3814672, "flag": "https://restcountries.eu/data/pan.svg", "currency": "Panamanian balboa"}, {"name": "French Polynesia", "capital": "Papeet\u0414\u201c", "languages": ["French"], "population": 271800, "flag": "https://restcountries.eu/data/pyf.svg", "currency": "CFP franc"}, {"name": "Suriname", "capital": "Paramaribo", "languages": ["Dutch"], "population": 541638, "flag": "https://restcountries.eu/data/sur.svg", "currency": "Surinamese dollar"}, {"name": "France", "capital": "Paris", "languages": ["French"], "population": 66710000, "flag": "https://restcountries.eu/data/fra.svg", "currency": "Euro"}, {"name": "Sint Maarten (Dutch part)", "capital": "Philipsburg", "languages": ["Dutch", "English"], "population": 38247, "flag": "https://restcountries.eu/data/sxm.svg", "currency": "Netherlands Antillean guilder"}, {"name": "Cambodia", "capital": "Phnom Penh", "languages": ["Khmer"], "population": 15626444, "flag": "https://restcountries.eu/data/khm.svg", "currency": "Cambodian riel"}, {"name": "Montserrat", "capital": "Plymouth", "languages": ["English"], "population": 4922, "flag": "https://restcountries.eu/data/msr.svg", "currency": "East Caribbean dollar"}, {"name": "Montenegro", "capital": "Podgorica", "languages": ["Serbian", "Bosnian", "Albanian", "Croatian"], "population": 621810, "flag": "https://restcountries.eu/data/mne.svg", "currency": "Euro"}, {"name": "Mauritius", "capital": "Port Louis", "languages": ["English"], "population": 1262879, "flag": "https://restcountries.eu/data/mus.svg", "currency": "Mauritian rupee"}, {"name": "Papua New Guinea", "capital": "Port Moresby", "languages": ["English"], "population": 8083700, "flag": "https://restcountries.eu/data/png.svg", "currency": "Papua New Guinean kina"}, {"name": "Vanuatu", "capital": "Port Vila", "languages": ["Bislama", "English", "French"], "population": 277500, "flag": "https://restcountries.eu/data/vut.svg", "currency": "Vanuatu vatu"}, {"name": "Trinidad and Tobago", "capital": "Port of Spain", "languages": ["English"], "population": 1349667, "flag": "https://restcountries.eu/data/tto.svg", "currency": "Trinidad and Tobago dollar"}, {"name": "Haiti", "capital": "Port-au-Prince", "languages": ["French", "Haitian"], "population": 11078033, "flag": "https://restcountries.eu/data/hti.svg", "currency": "Haitian gourde"}, {"name": "French Southern Territories", "capital": "Port-aux-Fran\u0413\u00a7ais", "languages": ["French"], "population": 140, "flag": "https://restcountries.eu/data/atf.svg", "currency": "Euro"}, {"name": "Benin", "capital": "Porto-Novo", "languages": ["French"], "population": 10653654, "flag": "https://restcountries.eu/data/ben.svg", "currency": "West African CFA franc"}, {"name": "Czech Republic", "capital": "Prague", "languages": ["Czech", "Slovak"], "population": 10558524, "flag": "https://restcountries.eu/data/cze.svg", "currency": "Czech koruna"}, {"name": "Cabo Verde", "capital": "Praia", "languages": ["Portuguese"], "population": 531239, "flag": "https://restcountries.eu/data/cpv.svg", "currency": "Cape Verdean escudo"}, {"name": "South Africa", "capital": "Pretoria", "languages": ["Afrikaans", "English", "Southern Ndebele", "Southern Sotho", "Swati", "Tswana", "Tsonga", "Venda", "Xhosa", "Zulu"], "population": 55653654, "flag": "https://restcountries.eu/data/zaf.svg", "currency": "South African rand"}, {"name": "Republic of Kosovo", "capital": "Pristina", "languages": ["Albanian", "Serbian"], "population": 1733842, "flag": "https://restcountries.eu/data/kos.svg", "currency": "Euro"}, {"name": "Korea (Democratic People's Republic of)", "capital": "Pyongyang", "languages": ["Korean"], "population": 25281000, "flag": "https://restcountries.eu/data/prk.svg", "currency": "North Korean won"}, {"name": "Ecuador", "capital": "Quito", "languages": ["Spanish"], "population": 16545799, "flag": "https://restcountries.eu/data/ecu.svg", "currency": "United States dollar"}, {"name": "Morocco", "capital": "Rabat", "languages": ["Arabic"], "population": 33337529, "flag": "https://restcountries.eu/data/mar.svg", "currency": "Moroccan dirham"}, {"name": "Palestine, State of", "capital": "Ramallah", "languages": ["Arabic"], "population": 4682467, "flag": "https://restcountries.eu/data/pse.svg", "currency": "Israeli new sheqel"}, {"name": "Iceland", "capital": "Reykjav\u0413\u00adk", "languages": ["Icelandic"], "population": 334300, "flag": "https://restcountries.eu/data/isl.svg", "currency": "Icelandic kr\u0413\u0456na"}, {"name": "Latvia", "capital": "Riga", "languages": ["Latvian"], "population": 1961600, "flag": "https://restcountries.eu/data/lva.svg", "currency": "Euro"}, {"name": "Saudi Arabia", "capital": "Riyadh", "languages": ["Arabic"], "population": 32248200, "flag": "https://restcountries.eu/data/sau.svg", "currency": "Saudi riyal"}, {"name": "Virgin Islands (British)", "capital": "Road Town", "languages": ["English"], "population": 28514, "flag": "https://restcountries.eu/data/vgb.svg", "currency": "[D]"}, {"name": "Holy See", "capital": "Rome", "languages": ["Latin", "Italian", "French", "German"], "population": 451, "flag": "https://restcountries.eu/data/vat.svg", "currency": "Euro"}, {"name": "Italy", "capital": "Rome", "languages": ["Italian"], "population": 60665551, "flag": "https://restcountries.eu/data/ita.svg", "currency": "Euro"}, {"name": "Dominica", "capital": "Roseau", "languages": ["English"], "population": 71293, "flag": "https://restcountries.eu/data/dma.svg", "currency": "East Caribbean dollar"}, {"name": "Jersey", "capital": "Saint Helier", "languages": ["English", "French"], "population": 100800, "flag": "https://restcountries.eu/data/jey.svg", "currency": "British pound"}, {"name": "Antigua and Barbuda", "capital": "Saint John's", "languages": ["English"], "population": 86295, "flag": "https://restcountries.eu/data/atg.svg", "currency": "East Caribbean dollar"}, {"name": "R\u0413\u00a9union", "capital": "Saint-Denis", "languages": ["French"], "population": 840974, "flag": "https://restcountries.eu/data/reu.svg", "currency": "Euro"}, {"name": "Saint Pierre and Miquelon", "capital": "Saint-Pierre", "languages": ["French"], "population": 6069, "flag": "https://restcountries.eu/data/spm.svg", "currency": "Euro"}, {"name": "Northern Mariana Islands", "capital": "Saipan", "languages": ["English", "Chamorro"], "population": 56940, "flag": "https://restcountries.eu/data/mnp.svg", "currency": "United States dollar"}, {"name": "Costa Rica", "capital": "San Jos\u0413\u00a9", "languages": ["Spanish"], "population": 4890379, "flag": "https://restcountries.eu/data/cri.svg", "currency": "Costa Rican col\u0413\u0456n"}, {"name": "Puerto Rico", "capital": "San Juan", "languages": ["Spanish", "English"], "population": 3474182, "flag": "https://restcountries.eu/data/pri.svg", "currency": "United States dollar"}, {"name": "El Salvador", "capital": "San Salvador", "languages": ["Spanish"], "population": 6520675, "flag": "https://restcountries.eu/data/slv.svg", "currency": "United States dollar"}, {"name": "Yemen", "capital": "Sana'a", "languages": ["Arabic"], "population": 27478000, "flag": "https://restcountries.eu/data/yem.svg", "currency": "Yemeni rial"}, {"name": "Chile", "capital": "Santiago", "languages": ["Spanish"], "population": 18191900, "flag": "https://restcountries.eu/data/chl.svg", "currency": "Chilean peso"}, {"name": "Dominican Republic", "capital": "Santo Domingo", "languages": ["Spanish"], "population": 10075045, "flag": "https://restcountries.eu/data/dom.svg", "currency": "Dominican peso"}, {"name": "Bosnia and Herzegovina", "capital": "Sarajevo", "languages": ["Bosnian", "Croatian", "Serbian"], "population": 3531159, "flag": "https://restcountries.eu/data/bih.svg", "currency": "Bosnia and Herzegovina convertible mark"}, {"name": "Korea (Republic of)", "capital": "Seoul", "languages": ["Korean"], "population": 50801405, "flag": "https://restcountries.eu/data/kor.svg", "currency": "South Korean won"}, {"name": "Singapore", "capital": "Singapore", "languages": ["English", "Malay", "Tamil", "Chinese"], "population": 5535000, "flag": "https://restcountries.eu/data/sgp.svg", "currency": "Brunei dollar"}, {"name": "Macedonia (the former Yugoslav Republic of)", "capital": "Skopje", "languages": ["Macedonian"], "population": 2058539, "flag": "https://restcountries.eu/data/mkd.svg", "currency": "Macedonian denar"}, {"name": "Bulgaria", "capital": "Sofia", "languages": ["Bulgarian"], "population": 7153784, "flag": "https://restcountries.eu/data/bgr.svg", "currency": "Bulgarian lev"}, {"name": "Kiribati", "capital": "South Tarawa", "languages": ["English"], "population": 113400, "flag": "https://restcountries.eu/data/kir.svg", "currency": "Australian dollar"}, {"name": "Grenada", "capital": "St. George's", "languages": ["English"], "population": 103328, "flag": "https://restcountries.eu/data/grd.svg", "currency": "East Caribbean dollar"}, {"name": "Guernsey", "capital": "St. Peter Port", "languages": ["English", "French"], "population": 62999, "flag": "https://restcountries.eu/data/ggy.svg", "currency": "British pound"}, {"name": "Falkland Islands (Malvinas)", "capital": "Stanley", "languages": ["English"], "population": 2563, "flag": "https://restcountries.eu/data/flk.svg", "currency": "Falkland Islands pound"}, {"name": "Sweden", "capital": "Stockholm", "languages": ["Swedish"], "population": 9894888, "flag": "https://restcountries.eu/data/swe.svg", "currency": "Swedish krona"}, {"name": "Bolivia (Plurinational State of)", "capital": "Sucre", "languages": ["Spanish", "Aymara", "Quechua"], "population": 10985059, "flag": "https://restcountries.eu/data/bol.svg", "currency": "Bolivian boliviano"}, {"name": "Fiji", "capital": "Suva", "languages": ["English", "Fijian", "Hindi", "Urdu"], "population": 867000, "flag": "https://restcountries.eu/data/fji.svg", "currency": "Fijian dollar"}, {"name": "Sao Tome and Principe", "capital": "S\u0413\u0408o Tom\u0413\u00a9", "languages": ["Portuguese"], "population": 187356, "flag": "https://restcountries.eu/data/stp.svg", "currency": "S\u0413\u0408o Tom\u0413\u00a9 and Pr\u0413\u00adncipe dobra"}, {"name": "Taiwan", "capital": "Taipei", "languages": ["Chinese"], "population": 23503349, "flag": "https://restcountries.eu/data/twn.svg", "currency": "New Taiwan dollar"}, {"name": "Estonia", "capital": "Tallinn", "languages": ["Estonian"], "population": 1315944, "flag": "https://restcountries.eu/data/est.svg", "currency": "Euro"}, {"name": "Uzbekistan", "capital": "Tashkent", "languages": ["Uzbek", "Russian"], "population": 31576400, "flag": "https://restcountries.eu/data/uzb.svg", "currency": "Uzbekistani so'm"}, {"name": "Georgia", "capital": "Tbilisi", "languages": ["Georgian"], "population": 3720400, "flag": "https://restcountries.eu/data/geo.svg", "currency": "Georgian Lari"}, {"name": "Honduras", "capital": "Tegucigalpa", "languages": ["Spanish"], "population": 8576532, "flag": "https://restcountries.eu/data/hnd.svg", "currency": "Honduran lempira"}, {"name": "Iran (Islamic Republic of)", "capital": "Tehran", "languages": ["Persian (Farsi)"], "population": 79369900, "flag": "https://restcountries.eu/data/irn.svg", "currency": "Iranian rial"}, {"name": "Anguilla", "capital": "The Valley", "languages": ["English"], "population": 13452, "flag": "https://restcountries.eu/data/aia.svg", "currency": "East Caribbean dollar"}, {"name": "Bhutan", "capital": "Thimphu", "languages": ["Dzongkha"], "population": 775620, "flag": "https://restcountries.eu/data/btn.svg", "currency": "Bhutanese ngultrum"}, {"name": "Albania", "capital": "Tirana", "languages": ["Albanian"], "population": 2886026, "flag": "https://restcountries.eu/data/alb.svg", "currency": "Albanian lek"}, {"name": "Japan", "capital": "Tokyo", "languages": ["Japanese"], "population": 126960000, "flag": "https://restcountries.eu/data/jpn.svg", "currency": "Japanese yen"}, {"name": "Libya", "capital": "Tripoli", "languages": ["Arabic"], "population": 6385000, "flag": "https://restcountries.eu/data/lby.svg", "currency": "Libyan dinar"}, {"name": "Tunisia", "capital": "Tunis", "languages": ["Arabic"], "population": 11154400, "flag": "https://restcountries.eu/data/tun.svg", "currency": "Tunisian dinar"}, {"name": "Faroe Islands", "capital": "T\u0413\u0456rshavn", "languages": ["Faroese"], "population": 49376, "flag": "https://restcountries.eu/data/fro.svg", "currency": "Danish krone"}, {"name": "Mongolia", "capital": "Ulan Bator", "languages": ["Mongolian"], "population": 3093100, "flag": "https://restcountries.eu/data/mng.svg", "currency": "Mongolian t\u0413\u00b6gr\u0413\u00b6g"}, {"name": "Liechtenstein", "capital": "Vaduz", "languages": ["German"], "population": 37623, "flag": "https://restcountries.eu/data/lie.svg", "currency": "Swiss franc"}, {"name": "Malta", "capital": "Valletta", "languages": ["Maltese", "English"], "population": 425384, "flag": "https://restcountries.eu/data/mlt.svg", "currency": "Euro"}, {"name": "Seychelles", "capital": "Victoria", "languages": ["French", "English"], "population": 91400, "flag": "https://restcountries.eu/data/syc.svg", "currency": "Seychellois rupee"}, {"name": "Austria", "capital": "Vienna", "languages": ["German"], "population": 8725931, "flag": "https://restcountries.eu/data/aut.svg", "currency": "Euro"}, {"name": "Lao People's Democratic Republic", "capital": "Vientiane", "languages": ["Lao"], "population": 6492400, "flag": "https://restcountries.eu/data/lao.svg", "currency": "Lao kip"}, {"name": "Lithuania", "capital": "Vilnius", "languages": ["Lithuanian"], "population": 2872294, "flag": "https://restcountries.eu/data/ltu.svg", "currency": "Euro"}, {"name": "Poland", "capital": "Warsaw", "languages": ["Polish"], "population": 38437239, "flag": "https://restcountries.eu/data/pol.svg", "currency": "Polish z\u0415\u201aoty"}, {"name": "United States of America", "capital": "Washington, D.C.", "languages": ["English"], "population": 323947000, "flag": "https://restcountries.eu/data/usa.svg", "currency": "United States dollar"}, {"name": "New Zealand", "capital": "Wellington", "languages": ["English", "M\u0414\u0403ori"], "population": 4697854, "flag": "https://restcountries.eu/data/nzl.svg", "currency": "New Zealand dollar"}, {"name": "Cocos (Keeling) Islands", "capital": "West Island", "languages": ["English"], "population": 550, "flag": "https://restcountries.eu/data/cck.svg", "currency": "Australian dollar"}, {"name": "Cura\u0413\u00a7ao", "capital": "Willemstad", "languages": ["Dutch", "(Eastern) Punjabi", "English"], "population": 154843, "flag": "https://restcountries.eu/data/cuw.svg", "currency": "Netherlands Antillean guilder"}, {"name": "Namibia", "capital": "Windhoek", "languages": ["English", "Afrikaans"], "population": 2324388, "flag": "https://restcountries.eu/data/nam.svg", "currency": "Namibian dollar"}, {"name": "C\u0413\u0491te d'Ivoire", "capital": "Yamoussoukro", "languages": ["French"], "population": 22671331, "flag": "https://restcountries.eu/data/civ.svg", "currency": "West African CFA franc"}, {"name": "Cameroon", "capital": "Yaound\u0413\u00a9", "languages": ["English", "French"], "population": 22709892, "flag": "https://restcountries.eu/data/cmr.svg", "currency": "Central African CFA franc"}, {"name": "Nauru", "capital": "Yaren", "languages": ["English", "Nauruan"], "population": 10084, "flag": "https://restcountries.eu/data/nru.svg", "currency": "Australian dollar"}, {"name": "Armenia", "capital": "Yerevan", "languages": ["Armenian", "Russian"], "population": 2994400, "flag": "https://restcountries.eu/data/arm.svg", "currency": "Armenian dram"}, {"name": "Croatia", "capital": "Zagreb", "languages": ["Croatian"], "population": 4190669, "flag": "https://restcountries.eu/data/hrv.svg", "currency": "Croatian kuna"}]
'''
import json
with open ('countries-data.json','r') as file:
    countries_data=json.load(file)    
countries_data.sort(key=lambda x:x.get('population'),reverse=True)#сортировка стран по населению
with open('countries_data_sort3.json','w') as file:
    json.dump(countries_data,file)
'''
[out]:
[{"name": "China", "capital": "Beijing", "languages": ["Chinese"], "population": 1377422166, "flag": "https://restcountries.eu/data/chn.svg", "currency": "Chinese yuan"}, {"name": "India", "capital": "New Delhi", "languages": ["Hindi", "English"], "population": 1295210000, "flag": "https://restcountries.eu/data/ind.svg", "currency": "Indian rupee"}, {"name": "United States of America", "capital": "Washington, D.C.", "languages": ["English"], "population": 323947000, "flag": "https://restcountries.eu/data/usa.svg", "currency": "United States dollar"}, {"name": "Indonesia", "capital": "Jakarta", "languages": ["Indonesian"], "population": 258705000, "flag": "https://restcountries.eu/data/idn.svg", "currency": "Indonesian rupiah"}, {"name": "Brazil", "capital": "Bras\u0413\u00adlia", "languages": ["Portuguese"], "population": 206135893, "flag": "https://restcountries.eu/data/bra.svg", "currency": "Brazilian real"}, {"name": "Pakistan", "capital": "Islamabad", "languages": ["English", "Urdu"], "population": 194125062, "flag": "https://restcountries.eu/data/pak.svg", "currency": "Pakistani rupee"}, {"name": "Nigeria", "capital": "Abuja", "languages": ["English"], "population": 186988000, "flag": "https://restcountries.eu/data/nga.svg", "currency": "Nigerian naira"}, {"name": "Bangladesh", "capital": "Dhaka", "languages": ["Bengali"], "population": 161006790, "flag": "https://restcountries.eu/data/bgd.svg", "currency": "Bangladeshi taka"}, {"name": "Russian Federation", "capital": "Moscow", "languages": ["Russian"], "population": 146599183, "flag": "https://restcountries.eu/data/rus.svg", "currency": "Russian ruble"}, {"name": "Japan", "capital": "Tokyo", "languages": ["Japanese"], "population": 126960000, "flag": "https://restcountries.eu/data/jpn.svg", "currency": "Japanese yen"}, {"name": "Mexico", "capital": "Mexico City", "languages": ["Spanish"], "population": 122273473, "flag": "https://restcountries.eu/data/mex.svg", "currency": "Mexican peso"}, {"name": "Philippines", "capital": "Manila", "languages": ["English"], "population": 103279800, "flag": "https://restcountries.eu/data/phl.svg", "currency": "Philippine peso"}, {"name": "Viet Nam", "capital": "Hanoi", "languages": ["Vietnamese"], "population": 92700000, "flag": "https://restcountries.eu/data/vnm.svg", "currency": "Vietnamese \u0414\u2018\u0431\u00bb\u201cng"}, {"name": "Ethiopia", "capital": "Addis Ababa", "languages": ["Amharic"], "population": 92206005, "flag": "https://restcountries.eu/data/eth.svg", "currency": "Ethiopian birr"}, {"name": "Egypt", "capital": "Cairo", "languages": ["Arabic"], "population": 91290000, "flag": "https://restcountries.eu/data/egy.svg", "currency": "Egyptian pound"}, {"name": "Congo (Democratic Republic of the)", "capital": "Kinshasa", "languages": ["French", "Lingala", "Kongo", "Swahili", "Luba-Katanga"], "population": 85026000, "flag": "https://restcountries.eu/data/cod.svg", "currency": "Congolese franc"}, {"name": "Germany", "capital": "Berlin", "languages": ["German"], "population": 81770900, "flag": "https://restcountries.eu/data/deu.svg", "currency": "Euro"}, {"name": "Iran (Islamic Republic of)", "capital": "Tehran", "languages": ["Persian (Farsi)"], "population": 79369900, "flag": "https://restcountries.eu/data/irn.svg", "currency": "Iranian rial"}, {"name": "Turkey", "capital": "Ankara", "languages": ["Turkish"], "population": 78741053, "flag": "https://restcountries.eu/data/tur.svg", "currency": "Turkish lira"}, {"name": "France", "capital": "Paris", "languages": ["French"], "population": 66710000, "flag": "https://restcountries.eu/data/fra.svg", "currency": "Euro"}, {"name": "Thailand", "capital": "Bangkok", "languages": ["Thai"], "population": 65327652, "flag": "https://restcountries.eu/data/tha.svg", "currency": "Thai baht"}, {"name": "United Kingdom of Great Britain and Northern Ireland", "capital": "London", "languages": ["English"], "population": 65110000, "flag": "https://restcountries.eu/data/gbr.svg", "currency": "British pound"}, {"name": "Italy", "capital": "Rome", "languages": ["Italian"], "population": 60665551, "flag": "https://restcountries.eu/data/ita.svg", "currency": "Euro"}, {"name": "South Africa", "capital": "Pretoria", "languages": ["Afrikaans", "English", "Southern Ndebele", "Southern Sotho", "Swati", "Tswana", "Tsonga", "Venda", "Xhosa", "Zulu"], "population": 55653654, "flag": "https://restcountries.eu/data/zaf.svg", "currency": "South African rand"}, {"name": "Tanzania, United Republic of", "capital": "Dodoma", "languages": ["Swahili", "English"], "population": 55155000, "flag": "https://restcountries.eu/data/tza.svg", "currency": "Tanzanian shilling"}, {"name": "Myanmar", "capital": "Naypyidaw", "languages": ["Burmese"], "population": 51419420, "flag": "https://restcountries.eu/data/mmr.svg", "currency": "Burmese kyat"}, {"name": "Korea (Republic of)", "capital": "Seoul", "languages": ["Korean"], "population": 50801405, "flag": "https://restcountries.eu/data/kor.svg", "currency": "South Korean won"}, {"name": "Colombia", "capital": "Bogot\u0413\u040e", "languages": ["Spanish"], "population": 48759958, "flag": "https://restcountries.eu/data/col.svg", "currency": "Colombian peso"}, {"name": "Kenya", "capital": "Nairobi", "languages": ["English", "Swahili"], "population": 47251000, "flag": "https://restcountries.eu/data/ken.svg", "currency": "Kenyan shilling"}, {"name": "Spain", "capital": "Madrid", "languages": ["Spanish"], "population": 46438422, "flag": "https://restcountries.eu/data/esp.svg", "currency": "Euro"}, {"name": "Argentina", "capital": "Buenos Aires", "languages": ["Spanish", "Guaran\u0413\u00ad"], "population": 43590400, "flag": "https://restcountries.eu/data/arg.svg", "currency": "Argentine peso"}, {"name": "Ukraine", "capital": "Kiev", "languages": ["Ukrainian"], "population": 42692393, "flag": "https://restcountries.eu/data/ukr.svg", "currency": "Ukrainian hryvnia"}, {"name": "Algeria", "capital": "Algiers", "languages": ["Arabic"], "population": 40400000, "flag": "https://restcountries.eu/data/dza.svg", "currency": "Algerian dinar"}, {"name": "Sudan", "capital": "Khartoum", "languages": ["Arabic", "English"], "population": 39598700, "flag": "https://restcountries.eu/data/sdn.svg", "currency": "Sudanese pound"}, {"name": "Poland", "capital": "Warsaw", "languages": ["Polish"], "population": 38437239, "flag": "https://restcountries.eu/data/pol.svg", "currency": "Polish z\u0415\u201aoty"}, {"name": "Iraq", "capital": "Baghdad", "languages": ["Arabic", "Kurdish"], "population": 37883543, "flag": "https://restcountries.eu/data/irq.svg", "currency": "Iraqi dinar"}, {"name": "Canada", "capital": "Ottawa", "languages": ["English", "French"], "population": 36155487, "flag": "https://restcountries.eu/data/can.svg", "currency": "Canadian dollar"}, {"name": "Uganda", "capital": "Kampala", "languages": ["English", "Swahili"], "population": 33860700, "flag": "https://restcountries.eu/data/uga.svg", "currency": "Ugandan shilling"}, {"name": "Morocco", "capital": "Rabat", "languages": ["Arabic"], "population": 33337529, "flag": "https://restcountries.eu/data/mar.svg", "currency": "Moroccan dirham"}, {"name": "Saudi Arabia", "capital": "Riyadh", "languages": ["Arabic"], "population": 32248200, "flag": "https://restcountries.eu/data/sau.svg", "currency": "Saudi riyal"}, {"name": "Uzbekistan", "capital": "Tashkent", "languages": ["Uzbek", "Russian"], "population": 31576400, "flag": "https://restcountries.eu/data/uzb.svg", "currency": "Uzbekistani so'm"}, {"name": "Peru", "capital": "Lima", "languages": ["Spanish"], "population": 31488700, "flag": "https://restcountries.eu/data/per.svg", "currency": "Peruvian sol"}, {"name": "Malaysia", "capital": "Kuala Lumpur", "languages": ["Malaysian"], "population": 31405416, "flag": "https://restcountries.eu/data/mys.svg", "currency": "Malaysian ringgit"}, {"name": "Venezuela (Bolivarian Republic of)", "capital": "Caracas", "languages": ["Spanish"], "population": 31028700, "flag": "https://restcountries.eu/data/ven.svg", "currency": "Venezuelan bol\u0413\u00advar"}, {"name": "Nepal", "capital": "Kathmandu", "languages": ["Nepali"], "population": 28431500, "flag": "https://restcountries.eu/data/npl.svg", "currency": "Nepalese rupee"}, {"name": "Ghana", "capital": "Accra", "languages": ["English"], "population": 27670174, "flag": "https://restcountries.eu/data/gha.svg", "currency": "Ghanaian cedi"}, {"name": "Afghanistan", "capital": "Kabul", "languages": ["Pashto", "Uzbek", "Turkmen"], "population": 27657145, "flag": "https://restcountries.eu/data/afg.svg", "currency": "Afghan afghani"}, {"name": "Yemen", "capital": "Sana'a", "languages": ["Arabic"], "population": 27478000, "flag": "https://restcountries.eu/data/yem.svg", "currency": "Yemeni rial"}, {"name": "Mozambique", "capital": "Maputo", "languages": ["Portuguese"], "population": 26423700, "flag": "https://restcountries.eu/data/moz.svg", "currency": "Mozambican metical"}, {"name": "Angola", "capital": "Luanda", "languages": ["Portuguese"], "population": 25868000, "flag": "https://restcountries.eu/data/ago.svg", "currency": "Angolan kwanza"}, {"name": "Korea (Democratic People's Republic of)", "capital": "Pyongyang", "languages": ["Korean"], "population": 25281000, "flag": "https://restcountries.eu/data/prk.svg", "currency": "North Korean won"}, {"name": "Australia", "capital": "Canberra", "languages": ["English"], "population": 24117360, "flag": "https://restcountries.eu/data/aus.svg", "currency": "Australian dollar"}, {"name": "Taiwan", "capital": "Taipei", "languages": ["Chinese"], "population": 23503349, "flag": "https://restcountries.eu/data/twn.svg", "currency": "New Taiwan dollar"}, {"name": "Cameroon", "capital": "Yaound\u0413\u00a9", "languages": ["English", "French"], "population": 22709892, "flag": "https://restcountries.eu/data/cmr.svg", "currency": "Central African CFA franc"}, {"name": "C\u0413\u0491te d'Ivoire", "capital": "Yamoussoukro", "languages": ["French"], "population": 22671331, "flag": "https://restcountries.eu/data/civ.svg", "currency": "West African CFA franc"}, {"name": "Madagascar", "capital": "Antananarivo", "languages": ["French", "Malagasy"], "population": 22434363, "flag": "https://restcountries.eu/data/mdg.svg", "currency": "Malagasy ariary"}, {"name": "Sri Lanka", "capital": "Colombo", "languages": ["Sinhalese", "Tamil"], "population": 20966000, "flag": "https://restcountries.eu/data/lka.svg", "currency": "Sri Lankan rupee"}, {"name": "Niger", "capital": "Niamey", "languages": ["French"], "population": 20715000, "flag": "https://restcountries.eu/data/ner.svg", "currency": "West African CFA franc"}, {"name": "Romania", "capital": "Bucharest", "languages": ["Romanian"], "population": 19861408, "flag": "https://restcountries.eu/data/rou.svg", "currency": "Romanian leu"}, {"name": "Burkina Faso", "capital": "Ouagadougou", "languages": ["French", "Fula"], "population": 19034397, "flag": "https://restcountries.eu/data/bfa.svg", "currency": "West African CFA franc"}, {"name": "Syrian Arab Republic", "capital": "Damascus", "languages": ["Arabic"], "population": 18564000, "flag": "https://restcountries.eu/data/syr.svg", "currency": "Syrian pound"}, {"name": "Chile", "capital": "Santiago", "languages": ["Spanish"], "population": 18191900, "flag": "https://restcountries.eu/data/chl.svg", "currency": "Chilean peso"}, {"name": "Mali", "capital": "Bamako", "languages": ["French"], "population": 18135000, "flag": "https://restcountries.eu/data/mli.svg", "currency": "West African CFA franc"}, {"name": "Kazakhstan", "capital": "Astana", "languages": ["Kazakh", "Russian"], "population": 17753200, "flag": "https://restcountries.eu/data/kaz.svg", "currency": "Kazakhstani tenge"}, {"name": "Netherlands", "capital": "Amsterdam", "languages": ["Dutch"], "population": 17019800, "flag": "https://restcountries.eu/data/nld.svg", "currency": "Euro"}, {"name": "Malawi", "capital": "Lilongwe", "languages": ["English", "Chichewa"], "population": 16832910, "flag": "https://restcountries.eu/data/mwi.svg", "currency": "Malawian kwacha"}, {"name": "Ecuador", "capital": "Quito", "languages": ["Spanish"], "population": 16545799, "flag": "https://restcountries.eu/data/ecu.svg", "currency": "United States dollar"}, {"name": "Guatemala", "capital": "Guatemala City", "languages": ["Spanish"], "population": 16176133, "flag": "https://restcountries.eu/data/gtm.svg", "currency": "Guatemalan quetzal"}, {"name": "Zambia", "capital": "Lusaka", "languages": ["English"], "population": 15933883, "flag": "https://restcountries.eu/data/zmb.svg", "currency": "Zambian kwacha"}, {"name": "Cambodia", "capital": "Phnom Penh", "languages": ["Khmer"], "population": 15626444, "flag": "https://restcountries.eu/data/khm.svg", "currency": "Cambodian riel"}, {"name": "Senegal", "capital": "Dakar", "languages": ["French"], "population": 14799859, "flag": "https://restcountries.eu/data/sen.svg", "currency": "West African CFA franc"}, {"name": "Chad", "capital": "N'Djamena", "languages": ["French", "Arabic"], "population": 14497000, "flag": "https://restcountries.eu/data/tcd.svg", "currency": "Central African CFA franc"}, {"name": "Zimbabwe", "capital": "Harare", "languages": ["English", "Shona", "Northern Ndebele"], "population": 14240168, "flag": "https://restcountries.eu/data/zwe.svg", "currency": "Botswana pula"}, {"name": "Guinea", "capital": "Conakry", "languages": ["French", "Fula"], "population": 12947000, "flag": "https://restcountries.eu/data/gin.svg", "currency": "Guinean franc"}, {"name": "South Sudan", "capital": "Juba", "languages": ["English"], "population": 12131000, "flag": "https://restcountries.eu/data/ssd.svg", "currency": "South Sudanese pound"}, {"name": "Rwanda", "capital": "Kigali", "languages": ["Kinyarwanda", "English", "French"], "population": 11553188, "flag": "https://restcountries.eu/data/rwa.svg", "currency": "Rwandan franc"}, {"name": "Belgium", "capital": "Brussels", "languages": ["Dutch", "French", "German"], "population": 11319511, "flag": "https://restcountries.eu/data/bel.svg", "currency": "Euro"}, {"name": "Cuba", "capital": "Havana", "languages": ["Spanish"], "population": 11239004, "flag": "https://restcountries.eu/data/cub.svg", "currency": "Cuban convertible peso"}, {"name": "Tunisia", "capital": "Tunis", "languages": ["Arabic"], "population": 11154400, "flag": "https://restcountries.eu/data/tun.svg", "currency": "Tunisian dinar"}, {"name": "Somalia", "capital": "Mogadishu", "languages": ["Somali", "Arabic"], "population": 11079000, "flag": "https://restcountries.eu/data/som.svg", "currency": "Somali shilling"}, {"name": "Haiti", "capital": "Port-au-Prince", "languages": ["French", "Haitian"], "population": 11078033, "flag": "https://restcountries.eu/data/hti.svg", "currency": "Haitian gourde"}, {"name": "Bolivia (Plurinational State of)", "capital": "Sucre", "languages": ["Spanish", "Aymara", "Quechua"], "population": 10985059, "flag": "https://restcountries.eu/data/bol.svg", "currency": "Bolivian boliviano"}, {"name": "Greece", "capital": "Athens", "languages": ["Greek (modern)"], "population": 10858018, "flag": "https://restcountries.eu/data/grc.svg", "currency": "Euro"}, {"name": "Benin", "capital": "Porto-Novo", "languages": ["French"], "population": 10653654, "flag": "https://restcountries.eu/data/ben.svg", "currency": "West African CFA franc"}, {"name": "Czech Republic", "capital": "Prague", "languages": ["Czech", "Slovak"], "population": 10558524, "flag": "https://restcountries.eu/data/cze.svg", "currency": "Czech koruna"}, {"name": "Portugal", "capital": "Lisbon", "languages": ["Portuguese"], "population": 10374822, "flag": "https://restcountries.eu/data/prt.svg", "currency": "Euro"}, {"name": "Burundi", "capital": "Bujumbura", "languages": ["French", "Kirundi"], "population": 10114505, "flag": "https://restcountries.eu/data/bdi.svg", "currency": "Burundian franc"}, {"name": "Dominican Republic", "capital": "Santo Domingo", "languages": ["Spanish"], "population": 10075045, "flag": "https://restcountries.eu/data/dom.svg", "currency": "Dominican peso"}, {"name": "Sweden", "capital": "Stockholm", "languages": ["Swedish"], "population": 9894888, "flag": "https://restcountries.eu/data/swe.svg", "currency": "Swedish krona"}, {"name": "United Arab Emirates", "capital": "Abu Dhabi", "languages": ["Arabic"], "population": 9856000, "flag": "https://restcountries.eu/data/are.svg", "currency": "United Arab Emirates dirham"}, {"name": "Hungary", "capital": "Budapest", "languages": ["Hungarian"], "population": 9823000, "flag": "https://restcountries.eu/data/hun.svg", "currency": "Hungarian forint"}, {"name": "Azerbaijan", "capital": "Baku", "languages": ["Azerbaijani"], "population": 9730500, "flag": "https://restcountries.eu/data/aze.svg", "currency": "Azerbaijani manat"}, {"name": "Jordan", "capital": "Amman", "languages": ["Arabic"], "population": 9531712, "flag": "https://restcountries.eu/data/jor.svg", "currency": "Jordanian dinar"}, {"name": "Belarus", "capital": "Minsk", "languages": ["Belarusian", "Russian"], "population": 9498700, "flag": "https://restcountries.eu/data/blr.svg", "currency": "New Belarusian ruble"}, {"name": "Austria", "capital": "Vienna", "languages": ["German"], "population": 8725931, "flag": "https://restcountries.eu/data/aut.svg", "currency": "Euro"}, {"name": "Tajikistan", "capital": "Dushanbe", "languages": ["Tajik", "Russian"], "population": 8593600, "flag": "https://restcountries.eu/data/tjk.svg", "currency": "Tajikistani somoni"}, {"name": "Honduras", "capital": "Tegucigalpa", "languages": ["Spanish"], "population": 8576532, "flag": "https://restcountries.eu/data/hnd.svg", "currency": "Honduran lempira"}, {"name": "Israel", "capital": "Jerusalem", "languages": ["Hebrew (modern)", "Arabic"], "population": 8527400, "flag": "https://restcountries.eu/data/isr.svg", "currency": "Israeli new shekel"}, {"name": "Switzerland", "capital": "Bern", "languages": ["German", "French", "Italian"], "population": 8341600, "flag": "https://restcountries.eu/data/che.svg", "currency": "Swiss franc"}, {"name": "Papua New Guinea", "capital": "Port Moresby", "languages": ["English"], "population": 8083700, "flag": "https://restcountries.eu/data/png.svg", "currency": "Papua New Guinean kina"}, {"name": "Hong Kong", "capital": "City of Victoria", "languages": ["English", "Chinese"], "population": 7324300, "flag": "https://restcountries.eu/data/hkg.svg", "currency": "Hong Kong dollar"}, {"name": "Bulgaria", "capital": "Sofia", "languages": ["Bulgarian"], "population": 7153784, "flag": "https://restcountries.eu/data/bgr.svg", "currency": "Bulgarian lev"}, {"name": "Togo", "capital": "Lom\u0413\u00a9", "languages": ["French"], "population": 7143000, "flag": "https://restcountries.eu/data/tgo.svg", "currency": "West African CFA franc"}, {"name": "Serbia", "capital": "Belgrade", "languages": ["Serbian"], "population": 7076372, "flag": "https://restcountries.eu/data/srb.svg", "currency": "Serbian dinar"}, {"name": "Sierra Leone", "capital": "Freetown", "languages": ["English"], "population": 7075641, "flag": "https://restcountries.eu/data/sle.svg", "currency": "Sierra Leonean leone"}, {"name": "Paraguay", "capital": "Asunci\u0413\u0456n", "languages": ["Spanish", "Guaran\u0413\u00ad"], "population": 6854536, "flag": "https://restcountries.eu/data/pry.svg", "currency": "Paraguayan guaran\u0413\u00ad"}, {"name": "El Salvador", "capital": "San Salvador", "languages": ["Spanish"], "population": 6520675, "flag": "https://restcountries.eu/data/slv.svg", "currency": "United States dollar"}, {"name": "Lao People's Democratic Republic", "capital": "Vientiane", "languages": ["Lao"], "population": 6492400, "flag": "https://restcountries.eu/data/lao.svg", "currency": "Lao kip"}, {"name": "Libya", "capital": "Tripoli", "languages": ["Arabic"], "population": 6385000, "flag": "https://restcountries.eu/data/lby.svg", "currency": "Libyan dinar"}, {"name": "Ireland", "capital": "Dublin", "languages": ["Irish", "English"], "population": 6378000, "flag": "https://restcountries.eu/data/irl.svg", "currency": "Euro"}, {"name": "Nicaragua", "capital": "Managua", "languages": ["Spanish"], "population": 6262703, "flag": "https://restcountries.eu/data/nic.svg", "currency": "Nicaraguan c\u0413\u0456rdoba"}, {"name": "Kyrgyzstan", "capital": "Bishkek", "languages": ["Kyrgyz", "Russian"], "population": 6047800, "flag": "https://restcountries.eu/data/kgz.svg", "currency": "Kyrgyzstani som"}, {"name": "Lebanon", "capital": "Beirut", "languages": ["Arabic", "French"], "population": 5988000, "flag": "https://restcountries.eu/data/lbn.svg", "currency": "Lebanese pound"}, {"name": "Denmark", "capital": "Copenhagen", "languages": ["Danish"], "population": 5717014, "flag": "https://restcountries.eu/data/dnk.svg", "currency": "Danish krone"}, {"name": "Singapore", "capital": "Singapore", "languages": ["English", "Malay", "Tamil", "Chinese"], "population": 5535000, "flag": "https://restcountries.eu/data/sgp.svg", "currency": "Brunei dollar"}, {"name": "Finland", "capital": "Helsinki", "languages": ["Finnish", "Swedish"], "population": 5491817, "flag": "https://restcountries.eu/data/fin.svg", "currency": "Euro"}, {"name": "Slovakia", "capital": "Bratislava", "languages": ["Slovak"], "population": 5426252, "flag": "https://restcountries.eu/data/svk.svg", "currency": "Euro"}, {"name": "Eritrea", "capital": "Asmara", "languages": ["Tigrinya", "Arabic", "English"], "population": 5352000, "flag": "https://restcountries.eu/data/eri.svg", "currency": "Eritrean nakfa"}, {"name": "Norway", "capital": "Oslo", "languages": ["Norwegian", "Norwegian Bokm\u0413\u0490l", "Norwegian Nynorsk"], "population": 5223256, "flag": "https://restcountries.eu/data/nor.svg", "currency": "Norwegian krone"}, {"name": "Central African Republic", "capital": "Bangui", "languages": ["French", "Sango"], "population": 4998000, "flag": "https://restcountries.eu/data/caf.svg", "currency": "Central African CFA franc"}, {"name": "Costa Rica", "capital": "San Jos\u0413\u00a9", "languages": ["Spanish"], "population": 4890379, "flag": "https://restcountries.eu/data/cri.svg", "currency": "Costa Rican col\u0413\u0456n"}, {"name": "Turkmenistan", "capital": "Ashgabat", "languages": ["Turkmen", "Russian"], "population": 4751120, "flag": "https://restcountries.eu/data/tkm.svg", "currency": "Turkmenistan manat"}, {"name": "Congo", "capital": "Brazzaville", "languages": ["French", "Lingala"], "population": 4741000, "flag": "https://restcountries.eu/data/cog.svg", "currency": "Central African CFA franc"}, {"name": "New Zealand", "capital": "Wellington", "languages": ["English", "M\u0414\u0403ori"], "population": 4697854, "flag": "https://restcountries.eu/data/nzl.svg", "currency": "New Zealand dollar"}, {"name": "Palestine, State of", "capital": "Ramallah", "languages": ["Arabic"], "population": 4682467, "flag": "https://restcountries.eu/data/pse.svg", "currency": "Israeli new sheqel"}, {"name": "Liberia", "capital": "Monrovia", "languages": ["English"], "population": 4615000, "flag": "https://restcountries.eu/data/lbr.svg", "currency": "Liberian dollar"}, {"name": "Oman", "capital": "Muscat", "languages": ["Arabic"], "population": 4420133, "flag": "https://restcountries.eu/data/omn.svg", "currency": "Omani rial"}, {"name": "Croatia", "capital": "Zagreb", "languages": ["Croatian"], "population": 4190669, "flag": "https://restcountries.eu/data/hrv.svg", "currency": "Croatian kuna"}, {"name": "Kuwait", "capital": "Kuwait City", "languages": ["Arabic"], "population": 4183658, "flag": "https://restcountries.eu/data/kwt.svg", "currency": "Kuwaiti dinar"}, {"name": "Panama", "capital": "Panama City", "languages": ["Spanish"], "population": 3814672, "flag": "https://restcountries.eu/data/pan.svg", "currency": "Panamanian balboa"}, {"name": "Georgia", "capital": "Tbilisi", "languages": ["Georgian"], "population": 3720400, "flag": "https://restcountries.eu/data/geo.svg", "currency": "Georgian Lari"}, {"name": "Mauritania", "capital": "Nouakchott", "languages": ["Arabic"], "population": 3718678, "flag": "https://restcountries.eu/data/mrt.svg", "currency": "Mauritanian ouguiya"}, {"name": "Moldova (Republic of)", "capital": "Chi\u0418\u2122in\u0414\u0453u", "languages": ["Romanian"], "population": 3553100, "flag": "https://restcountries.eu/data/mda.svg", "currency": "Moldovan leu"}, {"name": "Bosnia and Herzegovina", "capital": "Sarajevo", "languages": ["Bosnian", "Croatian", "Serbian"], "population": 3531159, "flag": "https://restcountries.eu/data/bih.svg", "currency": "Bosnia and Herzegovina convertible mark"}, {"name": "Uruguay", "capital": "Montevideo", "languages": ["Spanish"], "population": 3480222, "flag": "https://restcountries.eu/data/ury.svg", "currency": "Uruguayan peso"}, {"name": "Puerto Rico", "capital": "San Juan", "languages": ["Spanish", "English"], "population": 3474182, "flag": "https://restcountries.eu/data/pri.svg", "currency": "United States dollar"}, {"name": "Mongolia", "capital": "Ulan Bator", "languages": ["Mongolian"], "population": 3093100, "flag": "https://restcountries.eu/data/mng.svg", "currency": "Mongolian t\u0413\u00b6gr\u0413\u00b6g"}, {"name": "Armenia", "capital": "Yerevan", "languages": ["Armenian", "Russian"], "population": 2994400, "flag": "https://restcountries.eu/data/arm.svg", "currency": "Armenian dram"}, {"name": "Albania", "capital": "Tirana", "languages": ["Albanian"], "population": 2886026, "flag": "https://restcountries.eu/data/alb.svg", "currency": "Albanian lek"}, {"name": "Lithuania", "capital": "Vilnius", "languages": ["Lithuanian"], "population": 2872294, "flag": "https://restcountries.eu/data/ltu.svg", "currency": "Euro"}, {"name": "Jamaica", "capital": "Kingston", "languages": ["English"], "population": 2723246, "flag": "https://restcountries.eu/data/jam.svg", "currency": "Jamaican dollar"}, {"name": "Qatar", "capital": "Doha", "languages": ["Arabic"], "population": 2587564, "flag": "https://restcountries.eu/data/qat.svg", "currency": "Qatari riyal"}, {"name": "Namibia", "capital": "Windhoek", "languages": ["English", "Afrikaans"], "population": 2324388, "flag": "https://restcountries.eu/data/nam.svg", "currency": "Namibian dollar"}, {"name": "Botswana", "capital": "Gaborone", "languages": ["English", "Tswana"], "population": 2141206, "flag": "https://restcountries.eu/data/bwa.svg", "currency": "Botswana pula"}, {"name": "Slovenia", "capital": "Ljubljana", "languages": ["Slovene"], "population": 2064188, "flag": "https://restcountries.eu/data/svn.svg", "currency": "Euro"}, {"name": "Macedonia (the former Yugoslav Republic of)", "capital": "Skopje", "languages": ["Macedonian"], "population": 2058539, "flag": "https://restcountries.eu/data/mkd.svg", "currency": "Macedonian denar"}, {"name": "Latvia", "capital": "Riga", "languages": ["Latvian"], "population": 1961600, "flag": "https://restcountries.eu/data/lva.svg", "currency": "Euro"}, {"name": "Lesotho", "capital": "Maseru", "languages": ["English", "Southern Sotho"], "population": 1894194, "flag": "https://restcountries.eu/data/lso.svg", "currency": "Lesotho loti"}, {"name": "Gambia", "capital": "Banjul", "languages": ["English"], "population": 1882450, "flag": "https://restcountries.eu/data/gmb.svg", "currency": "Gambian dalasi"}, {"name": "Gabon", "capital": "Libreville", "languages": ["French"], "population": 1802278, "flag": "https://restcountries.eu/data/gab.svg", "currency": "Central African CFA franc"}, {"name": "Republic of Kosovo", "capital": "Pristina", "languages": ["Albanian", "Serbian"], "population": 1733842, "flag": "https://restcountries.eu/data/kos.svg", "currency": "Euro"}, {"name": "Guinea-Bissau", "capital": "Bissau", "languages": ["Portuguese"], "population": 1547777, "flag": "https://restcountries.eu/data/gnb.svg", "currency": "West African CFA franc"}, {"name": "Bahrain", "capital": "Manama", "languages": ["Arabic"], "population": 1404900, "flag": "https://restcountries.eu/data/bhr.svg", "currency": "Bahraini dinar"}, {"name": "Trinidad and Tobago", "capital": "Port of Spain", "languages": ["English"], "population": 1349667, "flag": "https://restcountries.eu/data/tto.svg", "currency": "Trinidad and Tobago dollar"}, {"name": "Estonia", "capital": "Tallinn", "languages": ["Estonian"], "population": 1315944, "flag": "https://restcountries.eu/data/est.svg", "currency": "Euro"}, {"name": "Mauritius", "capital": "Port Louis", "languages": ["English"], "population": 1262879, "flag": "https://restcountries.eu/data/mus.svg", "currency": "Mauritian rupee"}, {"name": "Equatorial Guinea", "capital": "Malabo", "languages": ["Spanish", "French"], "population": 1222442, "flag": "https://restcountries.eu/data/gnq.svg", "currency": "Central African CFA franc"}, {"name": "Timor-Leste", "capital": "Dili", "languages": ["Portuguese"], "population": 1167242, "flag": "https://restcountries.eu/data/tls.svg", "currency": "United States dollar"}, {"name": "Swaziland", "capital": "Lobamba", "languages": ["English", "Swati"], "population": 1132657, "flag": "https://restcountries.eu/data/swz.svg", "currency": "Swazi lilangeni"}, {"name": "Djibouti", "capital": "Djibouti", "languages": ["French", "Arabic"], "population": 900000, "flag": "https://restcountries.eu/data/dji.svg", "currency": "Djiboutian franc"}, {"name": "Fiji", "capital": "Suva", "languages": ["English", "Fijian", "Hindi", "Urdu"], "population": 867000, "flag": "https://restcountries.eu/data/fji.svg", "currency": "Fijian dollar"}, {"name": "Cyprus", "capital": "Nicosia", "languages": ["Greek (modern)", "Turkish", "Armenian"], "population": 847000, "flag": "https://restcountries.eu/data/cyp.svg", "currency": "Euro"}, {"name": "R\u0413\u00a9union", "capital": "Saint-Denis", "languages": ["French"], "population": 840974, "flag": "https://restcountries.eu/data/reu.svg", "currency": "Euro"}, {"name": "Comoros", "capital": "Moroni", "languages": ["Arabic", "French"], "population": 806153, "flag": "https://restcountries.eu/data/com.svg", "currency": "Comorian franc"}, {"name": "Bhutan", "capital": "Thimphu", "languages": ["Dzongkha"], "population": 775620, "flag": "https://restcountries.eu/data/btn.svg", "currency": "Bhutanese ngultrum"}, {"name": "Guyana", "capital": "Georgetown", "languages": ["English"], "population": 746900, "flag": "https://restcountries.eu/data/guy.svg", "currency": "Guyanese dollar"}, {"name": "Macao", "capital": "", "languages": ["Chinese", "Portuguese"], "population": 649100, "flag": "https://restcountries.eu/data/mac.svg", "currency": "Macanese pataca"}, {"name": "Solomon Islands", "capital": "Honiara", "languages": ["English"], "population": 642000, "flag": "https://restcountries.eu/data/slb.svg", "currency": "Solomon Islands dollar"}, {"name": "Montenegro", "capital": "Podgorica", "languages": ["Serbian", "Bosnian", "Albanian", "Croatian"], "population": 621810, "flag": "https://restcountries.eu/data/mne.svg", "currency": "Euro"}, {"name": "Luxembourg", "capital": "Luxembourg", "languages": ["French", "German", "Luxembourgish"], "population": 576200, "flag": "https://restcountries.eu/data/lux.svg", "currency": "Euro"}, {"name": "Suriname", "capital": "Paramaribo", "languages": ["Dutch"], "population": 541638, "flag": "https://restcountries.eu/data/sur.svg", "currency": "Surinamese dollar"}, {"name": "Cabo Verde", "capital": "Praia", "languages": ["Portuguese"], "population": 531239, "flag": "https://restcountries.eu/data/cpv.svg", "currency": "Cape Verdean escudo"}, {"name": "Western Sahara", "capital": "El Aai\u0413\u0454n", "languages": ["Spanish"], "population": 510713, "flag": "https://restcountries.eu/data/esh.svg", "currency": "Moroccan dirham"}, {"name": "Malta", "capital": "Valletta", "languages": ["Maltese", "English"], "population": 425384, "flag": "https://restcountries.eu/data/mlt.svg", "currency": "Euro"}, {"name": "Brunei Darussalam", "capital": "Bandar Seri Begawan", "languages": ["Malay"], "population": 411900, "flag": "https://restcountries.eu/data/brn.svg", "currency": "Brunei dollar"}, {"name": "Guadeloupe", "capital": "Basse-Terre", "languages": ["French"], "population": 400132, "flag": "https://restcountries.eu/data/glp.svg", "currency": "Euro"}, {"name": "Martinique", "capital": "Fort-de-France", "languages": ["French"], "population": 378243, "flag": "https://restcountries.eu/data/mtq.svg", "currency": "Euro"}, {"name": "Bahamas", "capital": "Nassau", "languages": ["English"], "population": 378040, "flag": "https://restcountries.eu/data/bhs.svg", "currency": "Bahamian dollar"}, {"name": "Belize", "capital": "Belmopan", "languages": ["English", "Spanish"], "population": 370300, "flag": "https://restcountries.eu/data/blz.svg", "currency": "Belize dollar"}, {"name": "Maldives", "capital": "Mal\u0413\u00a9", "languages": ["Divehi"], "population": 344023, "flag": "https://restcountries.eu/data/mdv.svg", "currency": "Maldivian rufiyaa"}, {"name": "Iceland", "capital": "Reykjav\u0413\u00adk", "languages": ["Icelandic"], "population": 334300, "flag": "https://restcountries.eu/data/isl.svg", "currency": "Icelandic kr\u0413\u0456na"}, {"name": "Barbados", "capital": "Bridgetown", "languages": ["English"], "population": 285000, "flag": "https://restcountries.eu/data/brb.svg", "currency": "Barbadian dollar"}, {"name": "Vanuatu", "capital": "Port Vila", "languages": ["Bislama", "English", "French"], "population": 277500, "flag": "https://restcountries.eu/data/vut.svg", "currency": "Vanuatu vatu"}, {"name": "French Polynesia", "capital": "Papeet\u0414\u201c", "languages": ["French"], "population": 271800, "flag": "https://restcountries.eu/data/pyf.svg", "currency": "CFP franc"}, {"name": "New Caledonia", "capital": "Noum\u0413\u00a9a", "languages": ["French"], "population": 268767, "flag": "https://restcountries.eu/data/ncl.svg", "currency": "CFP franc"}, {"name": "French Guiana", "capital": "Cayenne", "languages": ["French"], "population": 254541, "flag": "https://restcountries.eu/data/guf.svg", "currency": "Euro"}, {"name": "Mayotte", "capital": "Mamoudzou", "languages": ["French"], "population": 226915, "flag": "https://restcountries.eu/data/myt.svg", "currency": "Euro"}, {"name": "Samoa", "capital": "Apia", "languages": ["Samoan", "English"], "population": 194899, "flag": "https://restcountries.eu/data/wsm.svg", "currency": "Samoan t\u0414\u0403l\u0414\u0403"}, {"name": "Sao Tome and Principe", "capital": "S\u0413\u0408o Tom\u0413\u00a9", "languages": ["Portuguese"], "population": 187356, "flag": "https://restcountries.eu/data/stp.svg", "currency": "S\u0413\u0408o Tom\u0413\u00a9 and Pr\u0413\u00adncipe dobra"}, {"name": "Saint Lucia", "capital": "Castries", "languages": ["English"], "population": 186000, "flag": "https://restcountries.eu/data/lca.svg", "currency": "East Caribbean dollar"}, {"name": "Guam", "capital": "Hag\u0413\u0490t\u0413\u00b1a", "languages": ["English", "Chamorro", "Spanish"], "population": 184200, "flag": "https://restcountries.eu/data/gum.svg", "currency": "United States dollar"}, {"name": "Cura\u0413\u00a7ao", "capital": "Willemstad", "languages": ["Dutch", "(Eastern) Punjabi", "English"], "population": 154843, "flag": "https://restcountries.eu/data/cuw.svg", "currency": "Netherlands Antillean guilder"}, {"name": "Virgin Islands (U.S.)", "capital": "Charlotte Amalie", "languages": ["English"], "population": 114743, "flag": "https://restcountries.eu/data/vir.svg", "currency": "United States dollar"}, {"name": "Kiribati", "capital": "South Tarawa", "languages": ["English"], "population": 113400, "flag": "https://restcountries.eu/data/kir.svg", "currency": "Australian dollar"}, {"name": "Saint Vincent and the Grenadines", "capital": "Kingstown", "languages": ["English"], "population": 109991, "flag": "https://restcountries.eu/data/vct.svg", "currency": "East Caribbean dollar"}, {"name": "Aruba", "capital": "Oranjestad", "languages": ["Dutch", "(Eastern) Punjabi"], "population": 107394, "flag": "https://restcountries.eu/data/abw.svg", "currency": "Aruban florin"}, {"name": "Grenada", "capital": "St. George's", "languages": ["English"], "population": 103328, "flag": "https://restcountries.eu/data/grd.svg", "currency": "East Caribbean dollar"}, {"name": "Tonga", "capital": "Nuku'alofa", "languages": ["English", "Tonga (Tonga Islands)"], "population": 103252, "flag": "https://restcountries.eu/data/ton.svg", "currency": "Tongan pa\u041a\u00bbanga"}, {"name": "Micronesia (Federated States of)", "capital": "Palikir", "languages": ["English"], "population": 102800, "flag": "https://restcountries.eu/data/fsm.svg", "currency": "[D]"}, {"name": "Jersey", "capital": "Saint Helier", "languages": ["English", "French"], "population": 100800, "flag": "https://restcountries.eu/data/jey.svg", "currency": "British pound"}, {"name": "Seychelles", "capital": "Victoria", "languages": ["French", "English"], "population": 91400, "flag": "https://restcountries.eu/data/syc.svg", "currency": "Seychellois rupee"}, {"name": "Antigua and Barbuda", "capital": "Saint John's", "languages": ["English"], "population": 86295, "flag": "https://restcountries.eu/data/atg.svg", "currency": "East Caribbean dollar"}, {"name": "Isle of Man", "capital": "Douglas", "languages": ["English", "Manx"], "population": 84497, "flag": "https://restcountries.eu/data/imn.svg", "currency": "British pound"}, {"name": "Andorra", "capital": "Andorra la Vella", "languages": ["Catalan"], "population": 78014, "flag": "https://restcountries.eu/data/and.svg", "currency": "Euro"}, {"name": "Dominica", "capital": "Roseau", "languages": ["English"], "population": 71293, "flag": "https://restcountries.eu/data/dma.svg", "currency": "East Caribbean dollar"}, {"name": "Guernsey", "capital": "St. Peter Port", "languages": ["English", "French"], "population": 62999, "flag": "https://restcountries.eu/data/ggy.svg", "currency": "British pound"}, {"name": "Bermuda", "capital": "Hamilton", "languages": ["English"], "population": 61954, "flag": "https://restcountries.eu/data/bmu.svg", "currency": "Bermudian dollar"}, {"name": "Cayman Islands", "capital": "George Town", "languages": ["English"], "population": 58238, "flag": "https://restcountries.eu/data/cym.svg", "currency": "Cayman Islands dollar"}, {"name": "American Samoa", "capital": "Pago Pago", "languages": ["English", "Samoan"], "population": 57100, "flag": "https://restcountries.eu/data/asm.svg", "currency": "United State Dollar"}, {"name": "Northern Mariana Islands", "capital": "Saipan", "languages": ["English", "Chamorro"], "population": 56940, "flag": "https://restcountries.eu/data/mnp.svg", "currency": "United States dollar"}, {"name": "Greenland", "capital": "Nuuk", "languages": ["Kalaallisut"], "population": 55847, "flag": "https://restcountries.eu/data/grl.svg", "currency": "Danish krone"}, {"name": "Marshall Islands", "capital": "Majuro", "languages": ["English", "Marshallese"], "population": 54880, "flag": "https://restcountries.eu/data/mhl.svg", "currency": "United States dollar"}, {"name": "Faroe Islands", "capital": "T\u0413\u0456rshavn", "languages": ["Faroese"], "population": 49376, "flag": "https://restcountries.eu/data/fro.svg", "currency": "Danish krone"}, {"name": "Saint Kitts and Nevis", "capital": "Basseterre", "languages": ["English"], "population": 46204, "flag": "https://restcountries.eu/data/kna.svg", "currency": "East Caribbean dollar"}, {"name": "Monaco", "capital": "Monaco", "languages": ["French"], "population": 38400, "flag": "https://restcountries.eu/data/mco.svg", "currency": "Euro"}, {"name": "Sint Maarten (Dutch part)", "capital": "Philipsburg", "languages": ["Dutch", "English"], "population": 38247, "flag": "https://restcountries.eu/data/sxm.svg", "currency": "Netherlands Antillean guilder"}, {"name": "Liechtenstein", "capital": "Vaduz", "languages": ["German"], "population": 37623, "flag": "https://restcountries.eu/data/lie.svg", "currency": "Swiss franc"}, {"name": "Saint Martin (French part)", "capital": "Marigot", "languages": ["English", "French", "Dutch"], "population": 36979, "flag": "https://restcountries.eu/data/maf.svg", "currency": "Euro"}, {"name": "Gibraltar", "capital": "Gibraltar", "languages": ["English"], "population": 33140, "flag": "https://restcountries.eu/data/gib.svg", "currency": "Gibraltar pound"}, {"name": "San Marino", "capital": "City of San Marino", "languages": ["Italian"], "population": 33005, "flag": "https://restcountries.eu/data/smr.svg", "currency": "Euro"}, {"name": "Turks and Caicos Islands", "capital": "Cockburn Town", "languages": ["English"], "population": 31458, "flag": "https://restcountries.eu/data/tca.svg", "currency": "United States dollar"}, {"name": "\u0413\u2026land Islands", "capital": "Mariehamn", "languages": ["Swedish"], "population": 28875, "flag": "https://restcountries.eu/data/ala.svg", "currency": "Euro"}, {"name": "Virgin Islands (British)", "capital": "Road Town", "languages": ["English"], "population": 28514, "flag": "https://restcountries.eu/data/vgb.svg", "currency": "[D]"}, {"name": "Cook Islands", "capital": "Avarua", "languages": ["English"], "population": 18100, "flag": "https://restcountries.eu/data/cok.svg", "currency": "New Zealand dollar"}, {"name": "Palau", "capital": "Ngerulmud", "languages": ["English"], "population": 17950, "flag": "https://restcountries.eu/data/plw.svg", "currency": "[E]"}, {"name": "Bonaire, Sint Eustatius and Saba", "capital": "Kralendijk", "languages": ["Dutch"], "population": 17408, "flag": "https://restcountries.eu/data/bes.svg", "currency": "United States dollar"}, {"name": "Anguilla", "capital": "The Valley", "languages": ["English"], "population": 13452, "flag": "https://restcountries.eu/data/aia.svg", "currency": "East Caribbean dollar"}, {"name": "Wallis and Futuna", "capital": "Mata-Utu", "languages": ["French"], "population": 11750, "flag": "https://restcountries.eu/data/wlf.svg", "currency": "CFP franc"}, {"name": "Tuvalu", "capital": "Funafuti", "languages": ["English"], "population": 10640, "flag": "https://restcountries.eu/data/tuv.svg", "currency": "Australian dollar"}, {"name": "Nauru", "capital": "Yaren", "languages": ["English", "Nauruan"], "population": 10084, "flag": "https://restcountries.eu/data/nru.svg", "currency": "Australian dollar"}, {"name": "Saint Barth\u0413\u00a9lemy", "capital": "Gustavia", "languages": ["French"], "population": 9417, "flag": "https://restcountries.eu/data/blm.svg", "currency": "Euro"}, {"name": "Saint Pierre and Miquelon", "capital": "Saint-Pierre", "languages": ["French"], "population": 6069, "flag": "https://restcountries.eu/data/spm.svg", "currency": "Euro"}, {"name": "Montserrat", "capital": "Plymouth", "languages": ["English"], "population": 4922, "flag": "https://restcountries.eu/data/msr.svg", "currency": "East Caribbean dollar"}, {"name": "Saint Helena, Ascension and Tristan da Cunha", "capital": "Jamestown", "languages": ["English"], "population": 4255, "flag": "https://restcountries.eu/data/shn.svg", "currency": "Saint Helena pound"}, {"name": "British Indian Ocean Territory", "capital": "Diego Garcia", "languages": ["English"], "population": 3000, "flag": "https://restcountries.eu/data/iot.svg", "currency": "United States dollar"}, {"name": "Falkland Islands (Malvinas)", "capital": "Stanley", "languages": ["English"], "population": 2563, "flag": "https://restcountries.eu/data/flk.svg", "currency": "Falkland Islands pound"}, {"name": "Svalbard and Jan Mayen", "capital": "Longyearbyen", "languages": ["Norwegian"], "population": 2562, "flag": "https://restcountries.eu/data/sjm.svg", "currency": "Norwegian krone"}, {"name": "Norfolk Island", "capital": "Kingston", "languages": ["English"], "population": 2302, "flag": "https://restcountries.eu/data/nfk.svg", "currency": "Australian dollar"}, {"name": "Christmas Island", "capital": "Flying Fish Cove", "languages": ["English"], "population": 2072, "flag": "https://restcountries.eu/data/cxr.svg", "currency": "Australian dollar"}, {"name": "Niue", "capital": "Alofi", "languages": ["English"], "population": 1470, "flag": "https://restcountries.eu/data/niu.svg", "currency": "New Zealand dollar"}, {"name": "Tokelau", "capital": "Fakaofo", "languages": ["English"], "population": 1411, "flag": "https://restcountries.eu/data/tkl.svg", "currency": "New Zealand dollar"}, {"name": "Antarctica", "capital": "", "languages": ["English", "Russian"], "population": 1000, "flag": "https://restcountries.eu/data/ata.svg", "currency": "Australian dollar"}, {"name": "Cocos (Keeling) Islands", "capital": "West Island", "languages": ["English"], "population": 550, "flag": "https://restcountries.eu/data/cck.svg", "currency": "Australian dollar"}, {"name": "Holy See", "capital": "Rome", "languages": ["Latin", "Italian", "French", "German"], "population": 451, "flag": "https://restcountries.eu/data/vat.svg", "currency": "Euro"}, {"name": "United States Minor Outlying Islands", "capital": "", "languages": ["English"], "population": 300, "flag": "https://restcountries.eu/data/umi.svg", "currency": "United States Dollar"}, {"name": "French Southern Territories", "capital": "Port-aux-Fran\u0413\u00a7ais", "languages": ["French"], "population": 140, "flag": "https://restcountries.eu/data/atf.svg", "currency": "Euro"}, {"name": "Pitcairn", "capital": "Adamstown", "languages": ["English"], "population": 56, "flag": "https://restcountries.eu/data/pcn.svg", "currency": "New Zealand dollar"}, {"name": "South Georgia and the South Sandwich Islands", "capital": "King Edward Point", "languages": ["English"], "population": 30, "flag": "https://restcountries.eu/data/sgs.svg", "currency": "British pound"}, {"name": "Bouvet Island", "capital": "", "languages": ["Norwegian", "Norwegian Bokm\u0413\u0490l", "Norwegian Nynorsk"], "population": 0, "flag": "https://restcountries.eu/data/bvt.svg", "currency": "Norwegian krone"}, {"name": "Heard Island and McDonald Islands", "capital": "", "languages": ["English"], "population": 0, "flag": "https://restcountries.eu/data/hmd.svg", "currency": "Australian dollar"}]
'''

## Блок 2
1. Сгенерировать список из 50 числовых элементов. Используя списковые включения, вычислить 4, 5 и 6 степени каждого элемента.
 from random import randint
list_orig=[]
for i in range(50):
  list_orig.append(randint(1,250))
print('Список чисел:',list_orig)
list_four=[x**4 for x in list_orig]
list_five=[x**5 for x in list_orig]
list_six=[x**6 for x in list_orig]
print('Список чисел в четвертой степени:',list_four)
print('Список чисел в пятой степени:',list_five)
print('Список чисел в шестой степени:',list_six)
'''
#1 выборка входных данных
[out]:
Список чисел: [88, 186, 192, 190, 33, 195, 128, 117, 53, 26, 135, 215, 20, 237, 129, 76, 13, 106, 189, 120, 130, 77, 126, 248, 205, 81, 12, 43, 6, 73, 238, 75, 238, 39, 106, 77, 27, 88, 106, 209, 230, 157, 103, 194, 5, 95, 108, 156, 250, 95]
Список чисел в четвертой степени: [59969536, 1196883216, 1358954496, 1303210000, 1185921, 1445900625, 268435456, 187388721, 7890481, 456976, 332150625, 2136750625, 160000, 3154956561, 276922881, 33362176, 28561, 126247696, 1275989841, 207360000, 285610000, 35153041, 252047376, 3782742016, 1766100625, 43046721, 20736, 3418801, 1296, 28398241, 3208542736, 31640625, 3208542736, 2313441, 126247696, 35153041, 531441, 59969536, 126247696, 1908029761, 2798410000, 607573201, 112550881, 1416468496, 625, 81450625, 136048896, 592240896, 3906250000, 81450625]
Список чисел в пятой степени: [5277319168, 222620278176, 260919263232, 247609900000, 39135393, 281950621875, 34359738368, 21924480357, 418195493, 11881376, 44840334375, 459401384375, 3200000, 747724704957, 35723051649, 2535525376, 371293, 13382255776, 241162079949, 24883200000, 37129300000, 2706784157, 31757969376, 938120019968, 362050628125, 3486784401, 248832, 147008443, 7776, 2073071593, 763633171168, 2373046875, 763633171168, 90224199, 13382255776, 2706784157, 14348907, 5277319168, 13382255776, 398778220049, 643634300000, 95388992557, 11592740743, 274794888224, 3125, 7737809375, 14693280768, 92389579776, 976562500000, 7737809375]
Список чисел в шестой степени: [464404086784, 41407371740736, 50096498540544, 47045881000000, 1291467969, 54980371265625, 4398046511104, 2565164201769, 22164361129, 308915776, 6053445140625, 98771297640625, 64000000, 177210755074809, 4608273662721, 192699928576, 4826809, 1418519112256, 45579633110361, 2985984000000, 4826809000000, 208422380089, 4001504141376, 232653764952064, 74220378765625, 282429536481, 2985984, 6321363049, 46656, 151334226289, 181744694737984, 177978515625, 181744694737984, 3518743761, 1418519112256, 208422380089, 387420489, 464404086784, 1418519112256, 83344647990241, 148035889000000, 14976071831449, 1194052296529, 53310208315456, 15625, 735091890625, 1586874322944, 14412774445056, 244140625000000, 735091890625]
#2 выборка входных данных
Список чисел: [100, 114, 242, 144, 20, 59, 153, 240, 54, 94, 117, 173, 216, 203, 75, 175, 104, 20, 131, 50, 137, 66, 185, 4, 106, 83, 214, 186, 139, 125, 216, 159, 233, 240, 249, 3, 51, 156, 14, 65, 186, 128, 167, 215, 123, 6, 15, 174, 39, 201]
Список чисел в четвертой степени: [100000000, 168896016, 3429742096, 429981696, 160000, 12117361, 547981281, 3317760000, 8503056, 78074896, 187388721, 895745041, 2176782336, 1698181681, 31640625, 937890625, 116985856, 160000, 294499921, 6250000, 352275361, 18974736, 1171350625, 256, 126247696, 47458321, 2097273616, 1196883216, 373301041, 244140625, 2176782336, 639128961, 2947295521, 3317760000, 3844124001, 81, 6765201, 592240896, 38416, 17850625, 1196883216, 268435456, 777796321, 2136750625, 228886641, 1296, 50625, 916636176, 2313441, 1632240801]
Список чисел в пятой степени: [10000000000, 19254145824, 829997587232, 61917364224, 3200000, 714924299, 83841135993, 796262400000, 459165024, 7339040224, 21924480357, 154963892093, 470184984576, 344730881243, 2373046875, 164130859375, 12166529024, 3200000, 38579489651, 312500000, 48261724457, 1252332576, 216699865625, 1024, 13382255776, 3939040643, 448816553824, 222620278176, 51888844699, 30517578125, 470184984576, 101621504799, 686719856393, 796262400000, 957186876249, 243, 345025251, 92389579776, 537824, 1160290625, 222620278176, 34359738368, 129891985607, 459401384375, 28153056843, 7776, 759375, 159494694624, 90224199, 328080401001]
Список чисел в шестой степени: [1000000000000, 2194972623936, 200859416110144, 8916100448256, 64000000, 42180533641, 12827693806929, 191102976000000, 24794911296, 689869781056, 2565164201769, 26808753332089, 101559956668416, 69980368892329, 177978515625, 28722900390625, 1265319018496, 64000000, 5053913144281, 15625000000, 6611856250609, 82653950016, 40089475140625, 4096, 1418519112256, 326940373369, 96046742518336, 41407371740736, 7212549413161, 3814697265625, 101559956668416, 16157819263041, 160005726539569, 191102976000000, 238339532186001, 729, 17596287801, 14412774445056, 7529536, 75418890625, 41407371740736, 4398046511104, 21691961596369, 98771297640625, 3462825991689, 46656, 11390625, 27752076864576, 3518743761, 65944160601201]
#3 выборка входных данных
Список чисел: [154, 99, 150, 50, 10, 185, 39, 149, 45, 148, 132, 80, 240, 175, 202, 237, 62, 15, 66, 50, 107, 26, 107, 185, 26, 105, 72, 236, 20, 9, 212, 7, 169, 146, 150, 35, 245, 137, 188, 194, 35, 167, 249, 62, 49, 217, 23, 107, 111, 161]
Список чисел в четвертой степени: [562448656, 96059601, 506250000, 6250000, 10000, 1171350625, 2313441, 492884401, 4100625, 479785216, 303595776, 40960000, 3317760000, 937890625, 1664966416, 3154956561, 14776336, 50625, 18974736, 6250000, 131079601, 456976, 131079601, 1171350625, 456976, 121550625, 26873856, 3102044416, 160000, 6561, 2019963136, 2401, 815730721, 454371856, 506250000, 1500625, 3603000625, 352275361, 1249198336, 1416468496, 1500625, 777796321, 3844124001, 14776336, 5764801, 2217373921, 279841, 131079601, 151807041, 671898241]
Список чисел в пятой степени: [86617093024, 9509900499, 75937500000, 312500000, 100000, 216699865625, 90224199, 73439775749, 184528125, 71008211968, 40074642432, 3276800000, 796262400000, 164130859375, 336323216032, 747724704957, 916132832, 759375, 1252332576, 312500000, 14025517307, 11881376, 14025517307, 216699865625, 11881376, 12762815625, 1934917632, 732082482176, 3200000, 59049, 428232184832, 16807, 137858491849, 66338290976, 75937500000, 52521875, 882735153125, 48261724457, 234849287168, 274794888224, 52521875, 129891985607, 957186876249, 916132832, 282475249, 481170140857, 6436343, 14025517307, 16850581551, 108175616801]
Список чисел в шестой степени: [13339032325696, 941480149401, 11390625000000, 15625000000, 1000000, 40089475140625, 3518743761, 10942526586601, 8303765625, 10509215371264, 5289852801024, 262144000000, 191102976000000, 28722900390625, 67937289638464, 177210755074809, 56800235584, 11390625, 82653950016, 15625000000, 1500730351849, 308915776, 1500730351849, 40089475140625, 308915776, 1340095640625, 139314069504, 172771465793536, 64000000, 531441, 90785223184384, 117649, 23298085122481, 9685390482496, 11390625000000, 1838265625, 216270112515625, 6611856250609, 44151665987584, 53310208315456, 1838265625, 21691961596369, 238339532186001, 56800235584, 13841287201, 104413920565969, 148035889, 1500730351849, 1870414552161, 17416274304961]
#4 выборка входных данных
Список чисел: [182, 191, 132, 99, 144, 25, 241, 158, 23, 16, 146, 152, 89, 182, 118, 52, 96, 69, 161, 137, 114, 111, 88, 72, 236, 229, 81, 28, 128, 144, 131, 116, 127, 120, 189, 230, 73, 171, 235, 98, 90, 31, 244, 164, 133, 233, 180, 147, 209, 90]
Список чисел в четвертой степени: [1097199376, 1330863361, 303595776, 96059601, 429981696, 390625, 3373402561, 623201296, 279841, 65536, 454371856, 533794816, 62742241, 1097199376, 193877776, 7311616, 84934656, 22667121, 671898241, 352275361, 168896016, 151807041, 59969536, 26873856, 3102044416, 2750058481, 43046721, 614656, 268435456, 429981696, 294499921, 181063936, 260144641, 207360000, 1275989841, 2798410000, 28398241, 855036081, 3049800625, 92236816, 65610000, 923521, 3544535296, 723394816, 312900721, 2947295521, 1049760000, 466948881, 1908029761, 65610000]
Список чисел в пятой степени: [199690286432, 254194901951, 40074642432, 9509900499, 61917364224, 9765625, 812990017201, 98465804768, 6436343, 1048576, 66338290976, 81136812032, 5584059449, 199690286432, 22877577568, 380204032, 8153726976, 1564031349, 108175616801, 48261724457, 19254145824, 16850581551, 5277319168, 1934917632, 732082482176, 629763392149, 3486784401, 17210368, 34359738368, 61917364224, 38579489651, 21003416576, 33038369407, 24883200000, 241162079949, 643634300000, 2073071593, 146211169851, 716703146875, 9039207968, 5904900000, 28629151, 864866612224, 118636749824, 41615795893, 686719856393, 188956800000, 68641485507, 398778220049, 5904900000]
Список чисел в шестой степени: [36343632130624, 48551226272641, 5289852801024, 941480149401, 8916100448256, 244140625, 195930594145441, 15557597153344, 148035889, 16777216, 9685390482496, 12332795428864, 496981290961, 36343632130624, 2699554153024, 19770609664, 782757789696, 107918163081, 17416274304961, 6611856250609, 2194972623936, 1870414552161, 464404086784, 139314069504, 172771465793536, 144215816802121, 282429536481, 481890304, 4398046511104, 8916100448256, 5053913144281, 2436396322816, 4195872914689, 2985984000000, 45579633110361, 148035889000000, 151334226289, 25002110044521, 168425239515625, 885842380864, 531441000000, 887503681, 211027453382656, 19456426971136, 5534900853769, 160005726539569, 34012224000000, 10090298369529, 83344647990241, 531441000000]
'''
```
2. Сгенерировать матрицу в виде списка списков (например, `[ [1, 2], [3, 4], [5, 6], [7, 8], [1, 2], [3, 4], [5, 6], [7,8] ]`). Используя списковые включения, транспонировать матрицу ([https://ru.wikipedia.org/wiki/Транспонированная_матрица)](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0))
``` python
from random import randint
import numpy as np
matrix_1=[]
matrix_1=np.random.randint(0,20,(5,2))
print('Матрица:',matrix_1)
def transpose_matrix(matrix: list[list]) -> list[list]:
    transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix
matrix_t=transpose_matrix(matrix_1)
print('Транспонированная матрица:',matrix_t)
'''
[out]:
#1 выборка входных данных
Матрица: [[12  0]
 [ 5  7]
 [ 4  3]
 [13 11]
 [ 9 11]]
Транспонированная матрица: [[12, 5, 4, 13, 9], [0, 7, 3, 11, 11]]
#2 выборка входных данных
Матрица: [[12 13]
 [ 5 13]
 [ 3 12]
 [13  2]
 [12  5]]
Транспонированная матрица: [[12, 5, 3, 13, 12], [13, 13, 12, 2, 5]]
#3 выборка входных данных
Матрица: [[ 8 14]
 [16 16]
 [ 5 12]
 [16  5]
 [15 18]]
Транспонированная матрица: [[8, 16, 5, 16, 15], [14, 16, 12, 5, 18]]
#4 выборка входных данных
Матрица: [[18  9]
 [ 7  6]
 [ 8  1]
 [ 8 14]
 [16 12]]
Транспонированная матрица: [[18, 7, 8, 8, 16], [9, 6, 1, 14, 12]]
'''
```
3. Взять полный диапазон числовых элементов от -9999 до 9999. Используя анонимную функцию и функцию `filter()`, вывести список, содержащий все элементы, которые без остатка делятся на 36.
``` python
list_1=list(range(-9999,9999))#полный диапазон числовых элементов
list_2=list(filter(lambda x:x%36==0,list_1))
print('список с элементами,которые без остатка делятся на 36:',list_2)
'''
[out]:
список с элементами,которые без остатка делятся на 36: [-9972, -9936, -9900, -9864, -9828, -9792, -9756, -9720, -9684, -9648, -9612, -9576, -9540, -9504, -9468, -9432, -9396, -9360, -9324, -9288, -9252, -9216, -9180, -9144, -9108, -9072, -9036, -9000, -8964, -8928, -8892, -8856, -8820, -8784, -8748, -8712, -8676, -8640, -8604, -8568, -8532, -8496, -8460, -8424, -8388, -8352, -8316, -8280, -8244, -8208, -8172, -8136, -8100, -8064, -8028, -7992, -7956, -7920, -7884, -7848, -7812, -7776, -7740, -7704, -7668, -7632, -7596, -7560, -7524, -7488, -7452, -7416, -7380, -7344, -7308, -7272, -7236, -7200, -7164, -7128, -7092, -7056, -7020, -6984, -6948, -6912, -6876, -6840, -6804, -6768, -6732, -6696, -6660, -6624, -6588, -6552, -6516, -6480, -6444, -6408, -6372, -6336, -6300, -6264, -6228, -6192, -6156, -6120, -6084, -6048, -6012, -5976, -5940, -5904, -5868, -5832, -5796, -5760, -5724, -5688, -5652, -5616, -5580, -5544, -5508, -5472, -5436, -5400, -5364, -5328, -5292, -5256, -5220, -5184, -5148, -5112, -5076, -5040, -5004, -4968, -4932, -4896, -4860, -4824, -4788, -4752, -4716, -4680, -4644, -4608, -4572, -4536, -4500, -4464, -4428, -4392, -4356, -4320, -4284, -4248, -4212, -4176, -4140, -4104, -4068, -4032, -3996, -3960, -3924, -3888, -3852, -3816, -3780, -3744, -3708, -3672, -3636, -3600, -3564, -3528, -3492, -3456, -3420, -3384, -3348, -3312, -3276, -3240, -3204, -3168, -3132, -3096, -3060, -3024, -2988, -2952, -2916, -2880, -2844, -2808, -2772, -2736, -2700, -2664, -2628, -2592, -2556, -2520, -2484, -2448, -2412, -2376, -2340, -2304, -2268, -2232, -2196, -2160, -2124, -2088, -2052, -2016, -1980, -1944, -1908, -1872, -1836, -1800, -1764, -1728, -1692, -1656, -1620, -1584, -1548, -1512, -1476, -1440, -1404, -1368, -1332, -1296, -1260, -1224, -1188, -1152, -1116, -1080, -1044, -1008, -972, -936, -900, -864, -828, -792, -756, -720, -684, -648, -612, -576, -540, -504, -468, -432, -396, -360, -324, -288, -252, -216, -180, -144, -108, -72, -36, 0, 36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396, 432, 468, 504, 540, 576, 612, 648, 684, 720, 756, 792, 828, 864, 900, 936, 972, 1008, 1044, 1080, 1116, 1152, 1188, 1224, 1260, 1296, 1332, 1368, 1404, 1440, 1476, 1512, 1548, 1584, 1620, 1656, 1692, 1728, 1764, 1800, 1836, 1872, 1908, 1944, 1980, 2016, 2052, 2088, 2124, 2160, 2196, 2232, 2268, 2304, 2340, 2376, 2412, 2448, 2484, 2520, 2556, 2592, 2628, 2664, 2700, 2736, 2772, 2808, 2844, 2880, 2916, 2952, 2988, 3024, 3060, 3096, 3132, 3168, 3204, 3240, 3276, 3312, 3348, 3384, 3420, 3456, 3492, 3528, 3564, 3600, 3636, 3672, 3708, 3744, 3780, 3816, 3852, 3888, 3924, 3960, 3996, 4032, 4068, 4104, 4140, 4176, 4212, 4248, 4284, 4320, 4356, 4392, 4428, 4464, 4500, 4536, 4572, 4608, 4644, 4680, 4716, 4752, 4788, 4824, 4860, 4896, 4932, 4968, 5004, 5040, 5076, 5112, 5148, 5184, 5220, 5256, 5292, 5328, 5364, 5400, 5436, 5472, 5508, 5544, 5580, 5616, 5652, 5688, 5724, 5760, 5796, 5832, 5868, 5904, 5940, 5976, 6012, 6048, 6084, 6120, 6156, 6192, 6228, 6264, 6300, 6336, 6372, 6408, 6444, 6480, 6516, 6552, 6588, 6624, 6660, 6696, 6732, 6768, 6804, 6840, 6876, 6912, 6948, 6984, 7020, 7056, 7092, 7128, 7164, 7200, 7236, 7272, 7308, 7344, 7380, 7416, 7452, 7488, 7524, 7560, 7596, 7632, 7668, 7704, 7740, 7776, 7812, 7848, 7884, 7920, 7956, 7992, 8028, 8064, 8100, 8136, 8172, 8208, 8244, 8280, 8316, 8352, 8388, 8424, 8460, 8496, 8532, 8568, 8604, 8640, 8676, 8712, 8748, 8784, 8820, 8856, 8892, 8928, 8964, 9000, 9036, 9072, 9108, 9144, 9180, 9216, 9252, 9288, 9324, 9360, 9396, 9432, 9468, 9504, 9540, 9576, 9612, 9648, 9684, 9720, 9756, 9792, 9828, 9864, 9900, 9936, 9972]
'''
```
4. Используя `map()` и анонимные функции (а также любые вспомогательные методы `str`), написать функцию редактирования заголовков в англоязычном стиле (`Каждое Слово Длиной Более 3 Букв Должно Быть с Большой Буквы`), принимающую на вход исходную строку, возвращающую отредактированную строку.
``` python
def englishtext(title):
    words=title.split()
    filter__=map(lambda word:word.capitalize() if len(word) > 3 else word.lower(),words)
    result=' '.join(filter__)
    return result
list_1='понедельник начинается в субботу'
list_2=englishtext(list_1)
print(list_2)
'''
[out]:
Понедельник Начинается в Субботу
'''
```
6. Используя частичное выполнение функции, заменить указанную функцию с 4 аргументами на функцию с 1 аргументом так, чтобы результат был равен:
    1. 60
    2. 120
    3. 180
``` python
from functools import partial
def foo(a:int,b:int,c:int,d:int) -> int:
    return a*4+b*3+c*2+d

par=partial(foo,2,4,20)

print(par(0))
print(par(60))
print(par(120))
```
7. Используя 2 генератора и `sum()`, вернуть сумму квадратов первых 10, 20, 30, 40 и 50 чисел Фибоначчи.
``` python
fib_number=[0,1]

def fibonacci_number(n):
    while len(fib_number)< n:
        fib_number.append(fib_number[-1]+fib_number[-2])
    return fib_number[:n]

def fibonacci_square(n):
    fib_number=fibonacci_number(n)
    return (x**2 for x in fib_number)

print(sum(fibonacci_square(10)))
print(sum(fibonacci_square(20)))
print(sum(fibonacci_square(30)))
print(sum(fibonacci_square(40)))
print(sum(fibonacci_square(50)))
```
	


# Лабораторная работа №4. Научные вычисления на Python
Собрать веб-интерфейс: вывести визуализацию модели, организовать пользовательский интерфейс при помощи HTML-форм. Пользователь вводит температуру, сведения о влажности и иные параметры модели, получает ощущаемую температуру. Можно брать любой фреймворк, например, Flask.
``` python
from flask import Flask, render_template,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import requests

app=Flask(__name__)

@app.route('/')
def home():
  file_path = "/Users/ALFA/Documents/IPR/weatherHistory.csv"
  data=pd.read_csv(file_path)

  x=data[['Temperature (C)','Humidity','Wind Speed (km/h)']]
  y=data['Apparent Temperature (C)']
  x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.3)

  model=linear_model.LinearRegression()
  model.fit(x_train,y_train)

  y_pred=model.predict(x_test)

  mse=mean_squared_error(y_test,y_pred)

  data_visual=x_test.copy()
  data_visual['Predicted Apparent Temperature (C)']=y_pred

  plt.switch_backend('agg')
  sns.pairplot(data_visual,x_vars=['Temperature (C)','Humidity','Wind Speed (km/h)'],y_vars=['Predicted Apparent Temperature (C)'],kind='reg',plot_kws={'line_kws':{'color':'red'}})
  plt.savefig('static/output.png')

  return render_template('index.html',mse=mse)

@app.route('/predict',methods=['POST'])    
def predict():

  file_path = "/Users/ALFA/Documents/IPR/weatherHistory.csv"
  data=pd.read_csv(file_path)

  x=data[['Temperature (C)','Humidity','Wind Speed (km/h)']]
  y=data['Apparent Temperature (C)']
  x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.3)

  model=linear_model.LinearRegression()
  model.fit(x_train,y_train)

  temperature=float(request.form.get('temperature'))
  humidity=float(request.form.get('humidity'))
  windspeed=float(request.form.get('windspeed'))

  prediction=model.predict([[temperature,humidity,windspeed]])

  return render_template('index.html',prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)
```

``` html
<!DOCTYPE html>
<html>
<body>
    <h1>Mean squared error: {{ mse }}</h1>
    <img src="{{ url_for('static', filename='output.png') }}" alt="output image">
<h2>Predict Apparent Temperature</h2>

<form action="/predict" method="post">
    <label for="temperature">Temperature (C):</label><br>
    <input type="number" step="any" id="temperature" name="temperature" value=""><br>
    <label for="humidity">Humidity:</label><br>
    <input type="number" step="any" id="humidity" name="humidity" value=""><br>
    <label for="windspeed">Wind Speed (km/h):</label><br>
    <input type="number" step="any" id="windspeed" name="windspeed" value=""><br><br>
    <input type="submit" value="Predict">
</form> 

{% if prediction %}
  <h2>Predicted Apparent Temperature: {{ prediction }}</h2>
{% endif %}

</body>
</html>
```
    


# Лабораторная работа №5. Применение Python для автоматизированного 3D-моделирования и анимации
Фигура A
``` python
import bpy
import math

if __name__ == '__main__':
    mat = bpy.data.materials.get('Material')
    cubes = list()
    scene = bpy.context.scene
    frame_num = 0

for i in range(-50, 51):
    bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
    bpy.context.active_object.data.materials.append(mat)
    base = 15 - (i**2)*0.05            
    bpy.ops.transform.resize(value=(base, base, 0.5))            
    cubes.append(bpy.context.active_object)
```

Фигура B
``` python
import bpy
import math

if __name__ == '__main__':
    mat = bpy.data.materials.get('Material')
    cubes = list()
    scene = bpy.context.scene
    frame_num = 0

for i in range(-55, 55):
    bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
    bpy.context.active_object.data.materials.append(mat)
    base = 150 - (i**2)*0.05
    bpy.ops.transform.resize(value=(base, base, 0.5))
    bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)
    cubes.append(bpy.context.active_object)

for cube in cubes:
    scene.frame_set(frame_num)
    cube.keyframe_insert(data_path="rotation_euler", index=-1)
    frame_num += 1
    scene.frame_set(frame_num)
    cube.rotation_euler[2] = 0
    cube.keyframe_insert(data_path="rotation_euler", index=-1)
```

Фигура C
``python
import bpy
import math

if __name__ == '__main__':
    mat = bpy.data.materials.get('Material')
    cubes = list()
    scene = bpy.context.scene
    frame_num = 0

for i in range(0, 51):
    bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
    bpy.context.active_object.data.materials.append(mat)
    base = i + ( i**2)*0.05
    bpy.ops.transform.resize(value=(base, base, 0.5))
    bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)        
    cubes.append(bpy.context.active_object)
```

Фигура D
``` python
import bpy
import math

if __name__ == '__main__':
    mat = bpy.data.materials.get('Material')
    cubes = list()
    scene = bpy.context.scene
    frame_num = 0

for i in range(0, 51):
    bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0, 0, i*.25))
    bpy.context.active_object.data.materials.append(mat)
    base = i + ( i**2)*0.05
    bpy.ops.transform.resize(value=(base, base, 0.5))
    bpy.context.active_object.rotation_euler[2] = math.degrees(i*25)       
    cubes.append(bpy.context.active_object)

for cube in cubes:
    scene.frame_set(frame_num)
    cube.keyframe_insert(data_path="rotation_euler", index=-1)
    frame_num += 1
    scene.frame_set(frame_num)
    cube.rotation_euler[2] = 0
    cube.keyframe_insert(data_path="rotation_euler", index=-1)
```