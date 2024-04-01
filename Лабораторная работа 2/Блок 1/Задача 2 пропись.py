import json
with open('countries.json','r') as file:
 country_list=json.load(file)
countries_2=list(map(lambda x:x.upper(),country_list))
with open('countries_2.json','w') as file:
 json.dump(countries_2,file)
