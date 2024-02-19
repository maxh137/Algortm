from random import randint
list_1=[]
for i in range(15):
  list_1.append(randint(1,1000))
print(list_1)
list_2=[]
for i in range(15):
  list_2.append(randint(1,1000))
print(list_2)
list_3=list_1[1::2]+list_2[::2]
print(list_3)
