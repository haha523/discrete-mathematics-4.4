from itertools import chain, combinations

def generate_boolean_set(input_set):
    """
    Генерирует булеан множества.
    :param input_set: множество чисел (set)
    :return: список подмножеств
    """
    # Преобразуем множество в список для индексации
    elements = list(input_set)
    # Генерация всех подмножеств
    boolean_set = list(chain.from_iterable(combinations(elements, r) for r in range(len(elements) + 1)))
    return boolean_set

# Пример использования
input_set = {1, 2, 3}
boolean_set = generate_boolean_set(input_set)

print("Булеан множества:")
for subset in boolean_set:
    print(set(subset))
