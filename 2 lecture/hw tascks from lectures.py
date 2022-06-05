import numpy as np

# TASK: создать двумерный/трехмерный массив
a2 = np.zeros((2,2))
a3 = np.zeros((3,3,3))
print(a2)
print('\n',a3)

# Задание: написать функции выводящие минимум для массива, сумму
def minimum(array):
  res = array[0]
  for el in array:
    if res > el:
      res = el
  return res

def summ(array):
  res = 0
  for el in array:
    res += el
  return res

print(minimum(np.array([1,2,3,4,5,6,7,8,9,-1])))
print(summ(np.arange(101)))

#CP numpy

# 0. Создать нулевой вектор с 5 значений на 5 позиции 5
# Ваш код здесь
a = np.array([0 for i in range(4)]+[5])
a

# 1. Создать матрицу 3*3 со значениями от 0 до 8
# Ваш код здесь
a = np.diag([0, 4, 8])
for i in range(3):
  for j in range(3):
      a[i, j] = i*3+j
a

# 2. Найти индексы не нулевых элементов в массиве [1,2,0,0,4,0]
# Ваш код здесь
a = np.array([1,2,0,0,4,0])
for i in range(len(a)):
  if a[i] != 0:
    print(i, end = " ")
	
# 3. Матрица 3*3*3 с рандомными значениями
# Ваш код здесь
np.random.random((3,3,3))

# 4. Матриа 10 на 10, найти минимумы и максимумы
# Ваш код здесь
a = np.random.random((10,10))
max_el = a[0, 0]
min_el = a[0, 0]

for i in a:
  for el in i:
    if min_el > el:
      min_el = el
    if max_el < el:
      max_el = el
print(min_el, max_el)