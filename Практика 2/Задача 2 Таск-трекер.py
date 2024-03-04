import json
with open('task.json','r') as file:
 task_d=json.load(file)
task_tracker_data=json.loads(task_d)
print(task_tracker_data)
print('Введите описание задачи и степень ее выполнения')
a=json.dumps({input():input()})
new_task=json.loads(a)
task_tracker_data.update(new_task)
print(task_tracker_data)
task_tracker_json_string=json.dumps(task_tracker_data)
with open('task.json','w') as file:
 json.dump(task_tracker_json_string,file)

