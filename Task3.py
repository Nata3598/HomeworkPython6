# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

arr = list(int(x) for x in input('Введите последовательность: ').split())
if arr == []:
    arr = [1, 2, 3, 5, 1, 5, 3, 10]

arr = list( filter(lambda x: arr.count(x) == 1, arr ) )

print(arr)