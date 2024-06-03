import json
with open ('countries-data.json','r') as file:
    countries_data=json.load(file)    
countries_data.sort(key=lambda x:x.get('name'),reverse=True)#сортировка стран по названию по убыванию
with open('countries_data_sort1.json','w') as file:
    json.dump(countries_data,file)
