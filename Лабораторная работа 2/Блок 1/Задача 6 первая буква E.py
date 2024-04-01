import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_6=list(filter(lambda x:x.find('E')==0,country_list))
with open('countries_6.json','w') as file:
 json.dump(countries_6,file)
