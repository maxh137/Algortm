import json
with open('airport.json','r') as file:
 airport_d=json.load(file)
airport_json_string=json.dumps(airport_d)
airport_data=json.loads(airport_d)
print('Введите название аэропорта:')
a=airport_data.get(input())
print('Код аэропорта:',a)
