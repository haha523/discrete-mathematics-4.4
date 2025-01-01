from functools import reduce

def find_intersection(*sets):
    # Используем reduce для последовательного нахождения пересечения всех множеств
    return reduce(lambda x, y: x & y, sets)

# Пример использования
sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
result = find_intersection(*sets)
print(f"Пересечение множеств: {result}")
