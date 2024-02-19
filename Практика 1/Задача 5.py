dicty_1=dict({'letter':7,'building':12,'crayon':2,'book':4,'white':3,'red':6,'green':1,'light':9,'ball':6,'black':2})
print(dicty_1)
dicty_2=dict({'milk':11,'notebook':3,'green':1,'book':4,'apple':6,'glasses':10,'watch':5})
print(dicty_2)
a=dicty_1.values()
b=dicty_2.values()
c=set(a).intersection(b)
print(c)
dicty_3=dict({})
for k,v in dicty_1.items():
 if v in c:
     dicty_3[k]=v
for k,v in dicty_2.items():
 if v in c:
     dicty_3[k]=v
print(dicty_3)


