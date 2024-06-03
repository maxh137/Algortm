import json
with open ('countries-data.json','r') as file:
    countries_data=json.load(file)    
countries_data.sort(key=lambda x:x.get('capital'))#сортировка стран по столице
with open('countries_data_sort2.json','w') as file:
    json.dump(countries_data,file)
