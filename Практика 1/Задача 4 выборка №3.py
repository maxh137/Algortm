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

