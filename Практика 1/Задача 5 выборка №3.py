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


