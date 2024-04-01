import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_4=list(filter(lambda x:len(x)==6,country_list))
with open('countries_4.json','w') as file:
 json.dump(countries_4,file)
