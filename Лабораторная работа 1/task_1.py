numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_int = 0
for i in numbers:
    if i is not None:
        sum_int += i #находим сумму всех элементов списка кроме None
    else: ind_none = numbers.index(i) #находим индекс элемента None

average = sum_int/len(numbers) #находим среднее арифметическое
numbers[ind_none] = average
print(numbers)


