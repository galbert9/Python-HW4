# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
import random
list = [random.randint(1, 10) for x in range(10)]
# вызов метода randint для генерации случайных чисел
#  в  указанном деапазоне
print(list)

list2 = []
flag = True
for i in list:
    if i not in list2:
        list2.append(i)
    else:
        flag = False 
print(list2)