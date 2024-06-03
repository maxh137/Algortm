from random import randint
list_orig=[]
for i in range(50):
  list_orig.append(randint(1,250))
print('Список чисел:',list_orig)
list_four=[x**4 for x in list_orig]
list_five=[x**5 for x in list_orig]
list_six=[x**6 for x in list_orig]
print('Список чисел в четвертой степени:',list_four)
print('Список чисел в пятой степени:',list_five)
print('Список чисел в шестой степени:',list_six)
