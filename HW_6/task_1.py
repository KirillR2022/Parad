def binary_search(arr, target):
    # Инициализация границ массива
    low, high = 0, len(arr) - 1

    # Пока левая граница не превысит правую
    while low <= high:
        # Находим средний индекс
        mid = (low + high) // 2
        mid_value = arr[mid]

        # Если средний элемент равен искомому, возвращаем его индекс
        if mid_value == target:
            return mid
        # Если средний элемент меньше искомого, обновляем левую границу
        elif mid_value < target:
            low = mid + 1
        # Если средний элемент больше искомого, обновляем правую границу
        else:
            high = mid - 1

    # Элемент не найден, возвращаем -1
    return -1

# Пример использования
if __name__ == "__main__":
    # Входные данные: отсортированный массив
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Искомый элемент
    target_element = 7

    # Вызываем функцию бинарного поиска
    result = binary_search(sorted_array, target_element)

    # Выводим результат
    if result != -1:
        print(f"Элемент {target_element} найден в массиве. Индекс: {result}")
    else:
        print(f"Элемент {target_element} не найден в массиве.")
