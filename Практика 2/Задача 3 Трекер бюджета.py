import json
budget_d="""
{
	"Изначальный бюджет":"50000",
	"Покупка 1":"-4500",
	"Покупка 2":"-2700"
}
"""
budget_tracker_data=json.loads(budget_d)
with open('budget.json','w') as file:
 json.dump(budget_d,file)
print(budget_tracker_data)
print('Введите описание дохода\расхода и введите сумму дохода\расхода')
a=json.dumps({input():input()})
new_oper=json.loads(a)
budget_tracker_data.update(new_oper)
print(budget_tracker_data)
budget_json_string=json.dumps(budget_tracker_data)
with open('task.json','w') as file:
 json.dump(budget_json_string,file)
