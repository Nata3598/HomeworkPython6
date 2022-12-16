# Задание №1. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_in = [2, 3, 4, 5, 6]
list_out = []

len_count = len(list_in)
len_count = len_count // 2
list_cut = list_in [ 0 : len(list_in) - len_count : 1 ]
list_cut_rev = list_in [ -1 : -( len(list_in) + 1 - 2 ) : -1 ]
list_out = list( map( lambda x, y: x*y, list_cut, list_cut_rev ) )
print (list_out)