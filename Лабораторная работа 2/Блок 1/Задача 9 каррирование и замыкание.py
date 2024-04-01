import json
with open('countries.json','r') as file:
 country_list=json.load(file)
#каррирование
def findcountry(x:str,y:str):
    return list(filter(lambda x:y in x,country_list))
categorize_countries=lambda x:lambda y:findcountry(x,y)
countries_9a=categorize_countries(country_list)('ia')
with open('countries_9a.json','w') as file:
 json.dump(countries_9a,file)
#замыкание
def categorize_countries(x:str):
    def findcountry(y:str):
      return list(filter(lambda x:y in x,country_list))
    return findcountry
countries_9b=categorize_countries(country_list)('land')
with open('countries_9b.json','w') as file:
 json.dump(countries_9b,file)

