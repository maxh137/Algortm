import json
with open ('countries-data.json','r') as file:
    countries_data=json.load(file)    
countries_data.sort(key=lambda x:x.get('population'),reverse=True)#сортировка стран по населению
top_ten_countries_population=countries_data[:10]
with open('countries_data_sort5.json','w') as file:
    json.dump(top_ten_countries_population,file)
