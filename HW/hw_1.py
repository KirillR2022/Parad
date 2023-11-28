def sort_list_imperative(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                # Обмен значениями, если текущий элемент меньше следующего
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


# Пример использования:
numbers = [64, 34, 25, 12, 22, 11, 90]
sort_list_imperative(numbers)
print("Отсортированный массив в порядке убывания:", numbers)