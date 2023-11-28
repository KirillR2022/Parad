def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

# Пример использования:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный массив в порядке убывания:", sorted_numbers)