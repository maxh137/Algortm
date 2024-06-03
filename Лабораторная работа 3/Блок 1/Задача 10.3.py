import json
with open ('countries-data.json','r') as file:
    countries_data=json.load(file)    
countries_data.sort(key=lambda x:x.get('population'),reverse=True)#сортировка стран по населению
with open('countries_data_sort3.json','w') as file:
    json.dump(countries_data,file)
