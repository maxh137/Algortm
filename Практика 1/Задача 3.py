from random import randint
list_1=[]
for i in range(20):
  list_1.append(randint(1,10))
print(list_1)
list_1=list(set(list_1))
print(list_1)
