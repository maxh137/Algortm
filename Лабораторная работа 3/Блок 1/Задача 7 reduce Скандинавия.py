import json
from functools import reduce
with open('countries.json','r') as file:
 country_list=json.load(file)
Scand=['Финляндия','Швеция','Дания','Норвегия','Исландия']
print(reduce(lambda x,y:x+","+y,Scand)+" являются странами Северной Европы.")

