from math import sqrt
def pearson_correlation(x, y):
    n = len(x)

    if n != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    sum_x = sum(x)
    sum_y = sum(y)

    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_y_squared = sum(yi ** 2 for yi in y)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))

    if denominator == 0:
        return 0  # Избегаем деления на ноль

    return numerator / denominator

# Входные данные (два массива случайных величин)
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]

# Расчет корреляции Пирсона
correlation = pearson_correlation(array1, array2)

# Вывод результата
print(f"Корреляция Пирсона: {correlation}")
