import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_3=list(filter(lambda x:'land' in x,country_list))
with open('countries_3.json','w') as file:
 json.dump(countries_3,file)
